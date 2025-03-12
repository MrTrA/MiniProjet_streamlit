# import the streamlit library

import streamlit as st

# ajouter image

from PIL import Image
img = Image.open("/workspaces/MiniProjet_streamlit/.venv/imc.png")
st.image(img, width=400)

# give a title to our app

st.title("Application de santé pour calculer et interpréter l'indice de masse corporel")

# TAKE WEIGHT INPUT in kgs

weight = st.number_input("Entrez Votre Poids (en kgs)")

# TAKE HEIGHT INPUT

# radio button to choose height format
status = st.radio('Selectionnez votre format de taille : ', ('centimètre', 'mètre', 'pieds'))

if(status == 'centimètre'):
    height = st.number_input('Centimètre')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Entrez une valeur de taille")

elif(status == 'mètre'):
    # take height input in meters
    height = st.number_input('Mètre')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Entrez une valeur de taille")
else:
    height = st.number_input('Pieds')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Entrez une valeur de taille")

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

# ajouter bouton sans action
st.button("Application de santé")

# ajouter un menu multi selection

MultiSelect = st.multiselect("Type de IMC: ",['Sous-poids', 'Normal', 'Sur-poids'])
st.write("Vous avez selectionné", len(MultiSelect), 'Type de IMC')
