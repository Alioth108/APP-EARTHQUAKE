# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:47:08 2023

@author: Davyd
"""

# %%----------IMPORT DES PACKAGES----------
import streamlit as st
import pandas as pd
import plotly.express as px

#%% -------------Structure de la page---------------
st.set_page_config(
        page_title="DVF en Graphiques",
        page_icon="📊"
    )

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.institutdesactuaires.com/ressources/temp/images/100_400_04494887066x247_21878862794_3091717026_2023095321-ia.webp);
        background-repeat: no-repeat;
        background-position: center;
        background-position: 0px 0px;
        padding-top: 125px;
        background-size: 350px;
        
            }
            [data-testid="stSidebarNav"]::before {
                content: "ActuariaView Pro";
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

 

#%% -------------Elément de base de la page

st.title("Exploration Visuelle : Tendances et Risques Immobiliers avec DVF")


# Image avec lien hypertexte
image_url = "https://presidence.gouv.tg/wp-content/uploads/2019/10/Climat-des-affaires-une-politique-de-gestion-du-foncier-adaptée-à-la-modernité-1024x682.jpg"
link_url = "https://presidence.gouv.tg/2019/10/20/climat-des-affaires-une-politique-de-gestion-du-foncier-adaptee-a-la-modernite/"

# Affichage de l'image avec le lien hypertexte et redimensionnement
st.markdown(f'<a href="{link_url}" target="_blank"><img src="{image_url}" alt="Image" style="width:100%; max-width:700px;"></a>', unsafe_allow_html=True)

# Introduction
st.write("Ci-dessous sont présentés la description de la base de données 'Demande de valeurs foncières' et la partie Data Viz associée.")

with st.expander("Description de la Base de Données"):
    # Description du texte (structure)
    st.write("""
    ### Description de la Base de Données - Demande de valeurs foncières

    La base de données "Demande de Valeurs Foncières" (DVF) offre une vision détaillée des transactions immobilières en France. Les informations incluent des données telles que le code de service, la référence du document, la date de mutation, la nature de la mutation (vente, adjudication, etc.), la valeur foncière déclarée, l'adresse complète (numéro de voie, type de voie, code postal, commune, etc.), les détails cadastraux (préfixe de section, section, etc.), les caractéristiques des lots de copropriété (surface Carrez, nombre de pièces, etc.), et des détails sur la nature du terrain. La base est mise à jour semestriellement et fournit une richesse d'informations sur les biens immobiliers, facilitant ainsi l'analyse des tendances du marché et des variations de valeurs foncières.
    """)

    # Tableau des attributs
    # Tableau des attributs
    st.write("""
#### Variables

| Colonne            | Description                                                      |
|--------------------|------------------------------------------------------------------|
| cod_nat_catnat     | Code unique identifiant une reconnaissance (code national généré par Gaspar) |
| cod_commune        | Code de la commune concernée                                     |
| lib_commune        | Nom de la commune concernée                                      |
| num_risque_jo      | Numéro du risque mentionné                                      |
| lib_risque_jo      | Libellé du risque mentionné dans le journal officiel             |
| dat_deb            | Date de début de l'événement                                     |
| dat_fin            | Date de fin de l'événement                                       |
| dat_pub_arrete     | Date de l'arrêté                                                 |
| dat_pub_jo         | Date de publication au journal officiel                          |
| dat_maj            | Date de mise à jour de la fiche GASPAR                           |

| Colonne            | Description                                                      |
|--------------------|------------------------------------------------------------------|
| Code service       | Données non restituées en application du décret n° 2018-1350 du 28 décembre 2018 |
| Référence document | Article CGI 1                                                    |
| Article CGI 2      | Article CGI 3                                                    |
| Article CGI 5      | N° de disposition dans le cas des actes comprenant plusieurs mutations – appelées « dispositions » –, seules celles concernant les mutations à titre onéreux sont restituées dans le fichier. |
| Date de mutation   | Date de signature de l’acte (format JJ/MM/AAAA) – Restitution au format AAAA/MM/JJ (norme ISO 8601) prévue à partir d'octobre 2019. |
| Nature de mutation  | Vente, vente en l’état futur d’achèvement, vente de terrain à bâtir, adjudication, expropriation ou échange |
| Valeur foncière    | Montant ou évaluation déclaré(e) dans le cadre d’une mutation à titre onéreux. Inclut les frais d'agence (si à la charge du vendeur), éventuelle TVA ; exclut les frais d'agence (si à la charge de l'acquéreur), frais de notaires, valeur des biens meubles stipulée dans l'acte de mutation. |
| N° de voie         | Numéro dans la voie                                              |
| B/T/Q              | Indice de répétition                                             |
| Type de voie       | Exemple : Rue, avenue, etc.                                      |
| Code voie          | Code Rivoli (répertoire informatisé codifiant, par commune, les voies, les lieux-dits et les ensembles immobiliers) |
| Voie               | Libellé de la voie                                               |
| Code postal        | Code postal                                                      |
| Commune            | Libellé de la commune                                            |
| Code département   | Référence cadastrale de la parcelle                              |
| Code commune       | Code commune                                                     |
| Préfixe de section |                                                               |
| Section            |                                                               |
| N° de plan         |                                                               |
| N° de volume       |                                                               |
| 1er lot            | Un lot de copropriété est constitué d’une partie privative (appartement, cave, etc.) et d’une quote-part de partie commune (tantièmes). Seuls les 5 premiers lots sont mentionnés. Si le nombre de lots est supérieur à 5, ils ne sont pas restitués. |
| Surface Carrez du 1er lot |                                               |
| 2e lot             |                                                               |
| Surface Carrez du 2e lot |                                                |
| 3e lot             |                                                               |
| Surface Carrez du 3e lot |                                                |
| 4e lot             |                                                               |
| Surface Carrez du 4e lot |                                                |
| 5e lot             |                                                               |
| Surface Carrez du 5e lot |                                                |
| Nombre de lots     | Nombre total de lots par disposition.                            |
| Code type local    | 1 : maison ; 2 : appartement ; 3 : dépendance (isolée) ; 4 : local industriel et commercial ou assimilés |
| Type local         |                                                               |
| Identifiant local  |                                                               |
| Surface réelle bâti | La surface réelle est la surface mesurée au sol entre les murs ou séparations et arrondie au mètre carré inférieur. Les surfaces des dépendances ne sont pas prises en compte. |
| Nombre de pièces principales | Les cuisines, salles d’eau et dépendances ne sont pas prises en compte. |
| Code nature culture | Voir dans le présent document la table de références « nature de culture » |
| Nature culture spéciale | Voir dans le présent document la table de références « nature de culture spéciale » |
| Surface terrain    | Contenance du terrain                                            |
""")
    
import streamlit as st
import pandas as pd

# Données de test
data = {
    'Categorie': ['A', 'B', 'C', 'D'],
    'Graph1': [10, 20, 15, 25],
    'Graph2': [30, 15, 25, 10]
}

df = pd.DataFrame(data)


# Utiliser st.expander avec l'argument layout pour ajuster la largeur
with st.expander("Data Viz"):
    import streamlit as st
    import pandas as pd
    import plotly
    
    # Load your data (replace with your actual data source)
    data = pd.DataFrame({
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Location': ['NY', 'CA', 'TX', 'NY', 'CA'],
        'Age': [25, 30, 35, 40, 45],
    })
    
    gender_filter = st.multiselect('Select Gender', options=list(data['Gender'].unique()), default=list(data['Gender'].unique()))
    location_filter = st.multiselect('Select Location', options=list(data['Location'].unique()), default=list(data['Location'].unique()))
    
    filtered_data = data[data['Gender'].isin(gender_filter) & data['Location'].isin(location_filter)]
    
    data_container = st.container()
    
    
    tab1, tab2 = st.tabs(["Data", "Chart"])

    with tab1:
        st.table(filtered_data)
    
    with tab2:
        import plotly.express as px
        fig = px.bar(filtered_data, x='Location', y='Age', color='Gender')
        fig.update_layout(margin={"t": 30, "b": 0})
        st.plotly_chart(fig, use_container_width=True)
    
    
    
    

    
