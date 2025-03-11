# import the streamlit library

import streamlit as st

# give a title to our app

st.title('Bienvenue dans le calculateur d Indice de masse corporel (IMC)')

# TAKE WEIGHT INPUT in kgs

weight = st.number_input("Entrez Votre Poids (en kgs)")

# TAKE HEIGHT INPUT

# radio button to choose height format
status = st.radio('Selectionnez votre format de taille : ', ('cms', 'meters', 'feet'))

if(status == 'cms'):
    height = st.number_input('Centimetre')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Entrez une valeur de taille")

elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Metre')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Entrez une valeur de taille")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if(st.button('IMC Calculé')):
    # print the BMI INDEX
    st.text("Votre indice IMC est {}.".format(bmi))
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("Vous êtes extrêment en sous poids")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("Vous êtes en sous poids")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("En bonne santé")
    elif(bmi >= 25 and bmi < 30):
        st.warning("En sur poids")
    elif(bmi >= 30):
        st.error("Extrement en sur poids")