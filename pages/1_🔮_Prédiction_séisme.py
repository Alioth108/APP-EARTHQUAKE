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
        page_title="Earthquake App",
        page_icon="🔮"
    )

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


#%% -------------Elément de base de la page

st.title("Anticipation de l'évolution du nombre de séismes mois après mois en Alaska")
    
# Image avec lien hypertexte
image_url = "https://media.istockphoto.com/id/527890380/photo/seismograph-and-earthquake.jpg?s=612x612&w=0&k=20&c=uBp9YM7Aa76NJKEDa37i6OhgT1bmAua8ao5-Z0FHR4E="
link_url = "https://www.istockphoto.com/fr/photo/séismographe-et-du-tremblement-de-terre-gm527890380-92846651"

# Affichage de l'image avec le lien hypertexte et redimensionnement
st.markdown(f'<a href="{link_url}" target="_blank"><img src="{image_url}" alt="Image" style="width:100%; max-width:700px;"></a>', unsafe_allow_html=True)


import pandas as pd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data_COMPLET_clean_feature_engineering.csv",sep=";")
df.drop(columns=["Unnamed: 0"],inplace=True)


# Sélectionner la variable cible
y = df["Count"].values

# Normalisation des données
scaler = MinMaxScaler()
y_scaled = scaler.fit_transform(y.reshape(-1, 1)).flatten()

# Créer des séquences pour l'entraînement du modèle
window_size = 12
X, y = [], []

for i in range(len(y_scaled) - window_size):
    X.append(y_scaled[i:i+window_size])
    y.append(y_scaled[i+window_size])

X, y = np.array(X), np.array(y)

# Diviser les données en ensembles d'entraînement et de test
X_train, y_train = X[:-window_size], y[:-window_size]
X_test, y_test = X[-window_size:], y[-window_size:]

# Reshape pour tenir compte de la structure d'entrée de LSTM
X_train = X_train.reshape((X_train.shape[0], window_size, 1))
X_test = X_test.reshape((X_test.shape[0], window_size, 1))


from keras.models import load_model
# Charger le modèle
loaded_model =  load_model("LSTM.h5", compile=False)
loaded_model.compile(optimizer='adam', loss='mean_squared_error')

# Calculer les prédictions du modèle sur l'ensemble de test
predictions_scaled = loaded_model.predict(X_test)
predictions = scaler.inverse_transform(predictions_scaled.reshape(-1, 1)).flatten()

#Arrondir à l'entier car on traite des nombres
predictions = np.round(predictions).astype(int)


y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()


import matplotlib.pyplot as plt
import seaborn as sns
data_test = df.tail(12)
data_test['year_month'] = pd.to_datetime(data_test['year_month'])


# Utiliser un style personnalisé pour ressembler à Plotly
sns.set_theme(style="whitegrid", rc={"grid.linewidth": 0.1, 'axes.labelsize': 12, 'axes.titlesize': 14, 'xtick.labelsize': 10, 'ytick.labelsize': 10})

# Tracer les données de test réelles
plt.plot(data_test["year_month"], y_test_actual, label='Données de test réelles', color='blue')

# Tracer les prédictions
plt.plot(data_test["year_month"], predictions, label='Prédictions', color='red')

# Ajouter des labels et une légende
plt.xlabel('Date')
plt.ylabel('Nombre de séisme')
plt.title('Ajustement des prédictions aux données de test')
plt.legend()


# Afficher le graphique
plt.show()
