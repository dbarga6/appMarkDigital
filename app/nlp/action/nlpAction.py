import pandas as pd
import nltk
import re
from unicodedata import normalize

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

'''
Clase que se encarga del proceso de NLP de los tweets obtenidos. 
Devuelve un fichero con el dataframe procesado y un dataframe para poder mostrar en el portal
'''

class NLPAction():

    def __init__(self,fichero):
        self.fichero = fichero
        self.df_tweets = self.dame_dataframe()

    '''
     función para limpiar los datos obtenidos antes de trabajar con ellos.
     Regular Expression/Normalization — lowercase the words, remove punctuation and remove numbers
    '''
    def proceso_nlp(self):
        self.limpieza()
        return self.df_tweets

    def limpieza(self):
        
        # Creamos una nueva columna  con los tweets limpios y en minúscula
        self.df_tweets['Tweet_limpio'] = self.df_tweets["Tweet"].str.lower().apply(
            self.process_tweet_sp)
        
        self.df_tweets["Longitud"] = self.df_tweets["Tweet"].str.len()
        self.df_tweets["Palabras"] = self.df_tweets["Tweet"].str.split().str.len()
        self.df_tweets = self.df_tweets.drop(self.df_tweets.columns[0],axis="columns")
        self.df_tweets.to_csv("app/nlp/static/docs/tweets_limpios.csv")


    def tokenizacion(self):
        self.df_tweets["Tokenizado"] = self.df_tweets["Tweet_limpio"].str.lower().apply(
            self.process_token_tweet_es)
        self.df_tweets = self.df_tweets.drop(self.df_tweets.columns[0],axis="columns")
        self.df_tweets.to_csv("app/nlp/static/docs/proceso_tokenizacion.csv")

 
    """
       proceso de limpieza
    """
    def process_tweet_sp(self, tweet):        
        # eliminar links
        tweet = re.sub(r"http\S+|www\S+|https\S+",
                       '', tweet, flags=re.MULTILINE)
        # eliminar los hashtag
        tweet = re.sub(r'\@\w+|\#', '', tweet)

        #Quitamos usuarios que salgan en el tweet
        tweet = re.sub(r'@[A-Za-z0-9_]+', '',tweet)

        # Normalizamos para que nos quite las tildes y mantenga las ñ
        tweet = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                       normalize( "NFD", tweet), 0, re.I)
        
        # Quitamos todo aquello que no sean letras
        tweet = re.sub('[^a-zA-Z]', ' ', tweet)

        return tweet

    """
       process_token_tweet_es.- Función de tokenización en español
       
    """    
    
    def process_token_tweet_es(self,tweet):
       
        # Tokenizar las palabras
        tokenized = word_tokenize(tweet)

        # Eliminar las stop words
        tokenized = [
            token for token in tokenized if token not in stopwords.words("spanish")]

        # Lematize the words
        lemmatizer = WordNetLemmatizer()
        tokenized = [lemmatizer.lemmatize(token, pos='a')
                     for token in tokenized]

        # eliminacion de los caracteres no alfabeticos
        tokenized = [token for token in tokenized if token.isalpha()
                     and len(token) > 2]

        return tokenized

    def dame_dataframe(self):
        file_tweets = "app/nlp/static/docs/" + self.fichero
        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
        return df_tweets


    def palabras_frecuentes(self):
       
        file_tweets = "app/nlp/static/docs/proceso_tokenizacion.csv"

        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])

        
        stops =  set(stopwords.words('spanish')+['com'])
        co = CountVectorizer(stop_words=stops)
        counts = co.fit_transform(df_tweets.Tweet_limpio)
        df_palabras = pd.DataFrame(counts.sum(axis=0),columns=co.get_feature_names()).T.sort_values(0,ascending=False).head(50)
        df_palabras.to_csv("app/nlp/static/docs/palabras_frecuentes.csv")

        self.pareja_palabras(df_tweets,stops)
        self.sacar_hashtag(df_tweets)
        self.sacar_topic(df_tweets,stops)

    def pareja_palabras(self,df_tweets,stops):
       
        co = CountVectorizer(ngram_range=(2,2),stop_words=stops)
        counts = co.fit_transform(df_tweets.clean_text)
        df_palabras =pd.DataFrame(counts.sum(axis=0),columns=co.get_feature_names()).T.sort_values(0,ascending=False).head(50)
        df_palabras.to_csv("app/nlp/static/docs/pareja_palabras_frecuentes.csv")
    
    def sacar_hashtag(self,df_tweets):
       
        print(df_tweets.Tweet.str.extractall(r'(\#\w+)')[0].value_counts().head(20))

    def sacar_topic(self,df_tweets,stops):
        from sklearn.decomposition import LatentDirichletAllocation, NMF
        vectorizer = CountVectorizer(stop_words=stops)
        model = vectorizer.fit(df_tweets.clean_text)
        docs = vectorizer.transform(df_tweets.clean_text)
        lda = LatentDirichletAllocation(20)
        lda.fit(docs)
        self.print_top_words(lda,vectorizer.get_feature_names(),10)

    def print_top_words(self,model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            message = "Topic #%d: " % topic_idx
            message += " ".join([(feature_names[i])
                                for i in topic.argsort()[:-n_top_words - 1:-1]])
            print(message)
        
    
