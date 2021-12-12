import streamlit as st
import base64
import requests
import streamlit.components.v1 as components 

 
apikey1="e0184b370f7844128258301878df2613"





st.title("Food Web")
option = st.selectbox(
    'Choose an Option',
    ('Choose here','Get an Random Food Trivia','Get an Random Food Joke','Get an Random Recipe','Get an Random Vegan Recipe','Get an Random Chinese Recipe','Get an Random Indian Recipe','Get an Random Italian Recipe'))



def trivia():
    response= requests.get("https://api.spoonacular.com/food/trivia/random?apiKey="+apikey1)
    a=response.json()
    trivia=(a["text"])
    st.write(trivia)


def joke():
    response= requests.get("https://api.spoonacular.com/food/jokes/random?apiKey="+apikey1)
    a=response.json()
    joke=(a["text"])
    st.title(joke)

def veganrecipe():
    response= requests.get("https://api.spoonacular.com/recipes/random?number=1&tags=vegan&apiKey="+apikey1)
    a=response.json()
    title=(a['recipes'][0]['title'])
    st.title(title)
    image=(a['recipes'][0]['image'])
    st.image(image)
    summary=(a['recipes'][0]['summary'])
    recipe=(a['recipes'][0]['instructions'])
    html_string='''
    <body>
{}
{}
    </body>
    '''.format(summary,recipe)
    st.markdown(html_string, unsafe_allow_html=True)

def chinese():
    response= requests.get("https://api.spoonacular.com/recipes/random?number=1&tags=chinese&apiKey="+apikey1)
    a=response.json()
    title=(a['recipes'][0]['title'])
    st.title(title)
    image=(a['recipes'][0]['image'])
    st.image(image)
    summary=(a['recipes'][0]['summary'])
    recipe=(a['recipes'][0]['instructions'])
    html_string='''
    <body>
{}
{}
    </body>
    '''.format(summary,recipe)
    st.markdown(html_string, unsafe_allow_html=True)
def indian():
    response= requests.get("https://api.spoonacular.com/recipes/random?number=1&tags=indian&apiKey="+apikey1)
    a=response.json()
    title=(a['recipes'][0]['title'])
    st.title(title)
    image=(a['recipes'][0]['image'])
    st.image(image)
    summary=(a['recipes'][0]['summary'])
    recipe=(a['recipes'][0]['instructions'])
    html_string='''
    <body>
{}
{}
    </body>
    '''.format(summary,recipe)
    st.markdown(html_string, unsafe_allow_html=True)
def italian():
    response= requests.get("https://api.spoonacular.com/recipes/random?number=1&tags=italian&apiKey="+apikey1)
    a=response.json()
    title=(a['recipes'][0]['title'])
    st.title(title)
    image=(a['recipes'][0]['image'])
    st.image(image)
    summary=(a['recipes'][0]['summary'])
    recipe=(a['recipes'][0]['instructions'])
    html_string='''
    <body>
{}
{}
    </body>
    '''.format(summary,recipe)
    st.markdown(html_string, unsafe_allow_html=True)
def recipe():
    response= requests.get("https://api.spoonacular.com/recipes/random?number=1&apiKey="+apikey1)
    a=response.json()
    title=(a['recipes'][0]['title'])
    st.title(title)
    image=(a['recipes'][0]['image'])
    st.image(image)
    summary=(a['recipes'][0]['summary'])
    recipe=(a['recipes'][0]['instructions'])
    html_string='''
    <body>
{}
{}
    </body>
    '''.format(summary,recipe)
    st.markdown(html_string, unsafe_allow_html=True)

if option=="Get an Random Food Trivia":
    trivia()


if option=="Get an Random Food Joke":
    joke()
 

if option=="Get an Random Vegan Recipe":
    veganrecipe()

if option=="Get an Random Recipe":
    recipe()

if option=="Get an Random Chinese Recipe":
    chinese()
if option=="Get an Random Indian Recipe":
    indian()
if option=="Get an Random Italian Recipe":
    italian()
 
 
