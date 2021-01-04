from textblob import TextBlob
import pandas as pd

class AnalisisSentimientos():
    def analyse_polarity(self,polarity):
        if polarity > 0:
            return "Positive"
        if polarity  == 0:
            return "Neutral"
        if polarity < 0:
            return "Negative"

    def polaridad(self):
        df_tweets = pd.read_csv("app/nlp/static/docs/proceso_tokenizacion.csv", parse_dates =["fecha"])
        df_tweets["Polarity"] = df_tweets["Tokenizado"].apply(lambda word: TextBlob(word).sentiment.polarity)
        df_tweets["Subjectivity"] = df_tweets["Tokenizado"].apply(lambda word: TextBlob(word).sentiment.subjectivity)
         # La clasificación la almacenamos es nueva columna del dataframe
        df_tweets["Polarity Scores"] = df_tweets["Polarity"].apply(self.analyse_polarity)
        df_tweets.to_csv("app/nlp/static/docs/tweets_analisis_sentimientos.csv")
        return df_tweets
       
