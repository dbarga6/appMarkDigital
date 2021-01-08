import nltk
nltk.download('vader_lexicon') # Obligatorio para usar SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

import hunspell # Nos ayudará con los diccionarios en español
# Buscar diccionarios en carpeta de instalacion
# Más diccionarios de idiomas disponibles en: https://github.com/wooorm/dictionaries/tree/master/dictionaries
diccionario = hunspell.HunSpell('/content/es.dic','/content/es.aff')




def corregir_palabras(corrector, palabras, agregarPrimero=[]):   
    #codificacion = corrector.get_dic_encoding()   # obtenemos la codificacion para usarla luego

    # agregamos las palabras aleatorias al diccionario
    for palabra in agregarPrimero:
        corrector.add(palabra)

    # autocorreccion de palabras
    corregida = []
    for p in palabras:
        ok = corrector.spell(p)   # verificamos ortografia
        if not ok:
            sugerencias = corrector.suggest(p)
            if len(sugerencias) > 0:  # hay sugerencias
                # tomamos la  mejor sugerencia(decodificada a string)
                mejor_sugerencia = sugerencias[0]   
                corregida.append(mejor_sugerencia)
            else:
                corregida.append(p)  # no hay ninguna sugerecia para la palabra
        else:
            corregida.append(p)   # esta palabra esta corregida

    return corregida


def corregir_oracion(corrector,string):
    oracion_fixed=''
    if len(string)>0:
        oracion_dirty=string.split()
        oracion_fixed=corregir_palabras(corrector, oracion_dirty,[''])
        oracion_fixed=' '.join(oracion_fixed)
    else:
      print('error')
    return oracion_fixed

def get_polarity():
  for i in range(len(df)):#len(df)
      try:
          temp=df['RelatoFixedTranslated'][i]    
          # translation= translate_client.translate(temp,target_language='en',source_language='es') # Already translated
          # translation=translation['translatedText'] # Already translated
          p=sid.polarity_scores(str(temp))['compound']
          neg=sid.polarity_scores(str(temp))['neg']
          neu=sid.polarity_scores(str(temp))['neu']
          pos=sid.polarity_scores(str(temp))['pos']
          df.loc[i,'polarity']=p
          df.loc[i,'neg']=neg
          df.loc[i,'neu']=neu
          df.loc[i,'pos']=pos
          #df.loc[i,'translated']=str(translation) # Already translated
          print(i,end=' - ')
          #sleep(0.1+random.random()/2) # Already translated
      except Exception as e:
          print('Error {}:{}'.format(i,e))