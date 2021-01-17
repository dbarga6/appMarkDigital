# Estudio de Redes para Marketing Digital

## INDICE
1. [Descripción](#Descripción)
2. [Lenguaje](#Lenguaje y Tecnologías)
3. [Instalaccion](#Instalaccion)
4. [FAQs](#faqs)



## Descripción

Aplicación para el estudio de las redes sociales en el ámbito de Marketing digital, aportando la potencia de Big Data y el Análisis de Sentimientos mediante el estudio de Proceso de Lenguaje Natural.

El lenguaje de programación utilizado en la aplicación es Python principalmente, apoyándonos en el microframework Flask, para la creación de la aplicación Web. Obteniendo los datos de la red social Twitter, accediendo a ella a través de su API en su parte gratuita y el posterior almacenamiento de información en la base de datos Mongodb.

El resultado final será un estudio de los tweets obtenidos a partir de un filtro de búsqueda. 
Estudio que consistirá en el análisis de sentimientos de dichos Tweets así como el momento en el que más activos están los usuarios y un desglose de palabras mas utilizadas, obteniendo su WordCloud.

También se realizará un modelado por temas de los tweets obtenidos. 


## Lenguaje y Tecnologías

La aplicación se ha realizado en lengua de programación Python[1], debido a su gran auge en la actualidad, la sencillez de uso del lenguaje y porque es uno de los lenguajes que más se usan en Big Data & Business Analytics. 
Al tratarse de una aplicación web, existe código desarrollado en JavaScript y HTML.
	Librerías de Python utilizadas en el desarrollo del proyecto:

-	[Flask](https://www.python.org/): microframework escrito en Python, que facilita la creación de aplicaciones web bajo el patrón MVC. (Modelo, Vista y Controlador)
-	[Tweepy](https://www.tweepy.org/): Librería para una fácil conexión y uso de la API de Twitter.
-	Pymongo[7]: Librería para la conexión y uso de la base de datos MongoDB.
-	NLTK[13]: Kit de herramientas de lenguaje natural. Conjunto de librerías y programas para el procesamiento del lenguaje natural. 
-	Wordcloud[10]: Librería para la generación visual de nubes de palabras.
-	Pandas: Librería que proporciona estructura de datos y herramientas de análisis de datos fáciles de usar. 
-	Textblob [9]: Librería para el proceso de datos textuales. Proporciona una API para las tareas comunes de procesamiento de lenguaje natural (PLN o NLP)
-	Sklearn [17]: librería de aprendizaje automático de software libre. Cuenta con varios algoritmos de clasificación, regresión y clustering. 
-	Seaborn [18]: Librería basada en Matplotlib. Sirve para la parte visual del estudio de datos, permitiendo dibujar gráficos estadísticos. 
-	Plotly [12]: Librería para la visualización de gráficos, usada dentro de la aplicación web, por su fácil integración con Flask.
-	Matplotlib [14]:  Liberia de gráficos en 2D. 



## Faqs