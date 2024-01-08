# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:47:08 2023

@author: Davyd
"""

import streamlit as st

st.set_page_config(
        page_title="Home",
        page_icon="👋"
    )

# st.markdown(
#         """
#         <style>
#             [data-testid="stSidebarNav"] {
#                 background-image: url(https://besthqwallpapers.com/Uploads/10-11-2021/181670/thumb2-league-of-legends-dark-blue-logo-4k-lol-dark-blue-neon-lights-creative.jpg);
#         background-repeat: no-repeat;
#         background-position: center;
#         background-position: 0px 0px;
#         padding-top: 120px;
#         background-size: 350px;
        
#             }
#             [data-testid="stSidebarNav"]::before {
#                 content: "LOL Prediction Match";
#                 margin-left: 20px;
#                 margin-top: 20px;
#                 font-size: 30px;
#                 position: relative;
#                 text-align: center;
#                 top: 100px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.actuia.com/wp-content/uploads/2019/04/ENSAI-696x348.png
);
        background-repeat: no-repeat;
        background-position: center;
        background-position: 0px 0px;
        padding-top: 125px;
        background-size: 350px;
        
            }
            [data-testid="stSidebarNav"]::before {
                content: "Earthquake App";
                margin-left: 35px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                text-align: center;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
"""
<style>
div[role="listbox"] li:nth-of-type(1){
background-color: red;
}
div[role="listbox"] li:nth-of-type(2){
background-color: blue;
}

</style>
""",
unsafe_allow_html=True,
)

# Titre centré
# Div pour centrer le titre
st.markdown('<div style="text-align: center;"><h1>PROJET SERIE TEMPORELLE</h1></div>', unsafe_allow_html=True)


# Espace entre le titre et l'image
st.write("")

# Image avec lien hypertexte, centrée
image_url = "https://img.freepik.com/free-photo/broken-road-separating-into-two-parts-by-earthquake-city-ai-generative_123827-23739.jpg"
link_url = "https://www.freepik.com/free-photo/broken-road-separating-into-two-parts-by-earthquake-city-ai-generative_41368246.htm#query=earthquake&position=0&from_view=keyword&track=sph&uuid=a8e8333b-d036-4dbb-a9f5-df27a99fc490"

# Div pour centrer l'image
st.markdown(
    f'<div style="display: flex; justify-content: center;"><a href="{link_url}" target="_blank"><img src="{image_url}" alt="Image" style="width:100%; max-width:700px;"></a></div>',
    unsafe_allow_html=True
)


#st.image("",width=700,caption="https://pixabay.com")

st.write("## Prédire le nombre de séisme en Alaska au fur et à mesure des mois de l'année")

# Description
st.write("""Notre application se distingue en tant que plateforme novatrice dédiée à la prédiction du nombre de séismes en Alaska au fil des mois de l'année. À l'aide de méthodes classiques de séries temporelles, d'apprentissage automatique (Machine Learning) et de Deep Learning, notre modèle a été spécifiquement conçu pour anticiper de manière précise l'évolution du nombre de séismes en Alaska en fonction des différents mois. En exploitant vos propres ensembles de données, cette approche diversifiée et intégrée assure une adaptabilité optimale, garantissant des prévisions fiables et personnalisées pour cette région particulière. Notre solution complète et efficace s'érige ainsi comme une référence pour anticiper les événements sismiques, offrant une vision claire et détaillée de l'activité sismique mensuelle en Alaska.
""")

st.write("### Qui sommes-nous ?")
# Création de trois colonnes
col1,col2,col3 = st.columns(3)

with col1:
    # Photo et nom du premier membre
    st.markdown(
        '<a href="https://www.linkedin.com/in/davyd-bayard-7616a423a/"><img src="https://media.licdn.com/dms/image/D4E03AQGVOp1OztlUwA/profile-displayphoto-shrink_800_800/0/1677345039076?e=1706745600&v=beta&t=pN-c19RzfjN8G-9tUNzaFPSXE0AnlMK6_lQQVm7UHrM" alt="Davyd Bayard" style="width:100%"></a>',
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'><strong>Davyd Bayard</strong></p>", unsafe_allow_html=True)

with col2:
    # Photo et nom du deuxième membre
    st.markdown(
        '<a href="https://www.linkedin.com/in/guillaume-poirier-41231713a/"><img src="https://media.licdn.com/dms/image/D4E03AQEyJMrFoKxchQ/profile-displayphoto-shrink_800_800/0/1664483713894?e=1710374400&v=beta&t=-iWHV-2L04solVdvmlC3aonXrfkFQDJttuA2_GsbhDI" alt="Guillaume Poirier" style="width:100%"></a>',
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'><strong>Guillaume Poirier</strong></p>", unsafe_allow_html=True)

    
