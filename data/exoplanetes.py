# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
#on extrait les noms des paramètres du fichier csv
titres=pd.read_csv('exoplanete.csv',sep='# COLUMNS',skipfooter=36484,skiprows=3,engine='python',names=['paramètre'])['paramètre'].tolist()
titres=[a.split(':',1)[1].strip() for a in titres]

# %%
#si jamais deux colonnes ont le même nom, on cherche lesquelles
set([x for x in titres if titres.count(x)>1])

# %%
#deux sont en double => on en renomme une des deux pour pouvoir les utiliser comme noms de colonne dans le dataframe (on voit qu'il s'agit du jupiter radius en regardant le fichier originel)
titres[26]='Planet Radius Limit Flag [Jupiter Radius]'

# %%
exo=pd.read_csv('exoplanete.csv',skiprows=97,names=titres,index_col='Planet Name')

# %%
#si jamais il y a des lignes ou colonnes vides
exo.dropna(how='all',axis=0,inplace=True)
exo.dropna(how='all',axis=1,inplace=True)

# %%
#certaines séries sont elles en double ?
print(exo.duplicated().value_counts())

# %% jupyter={"source_hidden": true}
#oui => on supprime les doublons
exo=exo.drop_duplicates()

# %%
#tri de la dataframe par date de découverte
exo.sort_values("Discovery Year",inplace=True)
exo


# %%
Idée du projet : 
-En recueillant les données de la Nasa, notre idée était d'identifier les planètes avec des conditions proches de celles de la Terre de sorte que ces planètes soient potentiellement habitable. On voulait donc trier la dataframe en ajoutant des conditions sur des colonnes intéressantes comme la température, la distance à la Terre...
-On à tracé à chaque fois la répartition du nombre de planètes en fonction de chaque caractéristique, les tracés suivants se faisant sur les dataframes modifiés par les conditions précédantes
-Nous n'avons pas réussi à tracer les graphes pour toutes les colones.

-

# %%

# %%
exo.columns

# %%

# %%

# %%

# %%
#TEMP2RATURE !!!!!!!

#on change la dataframe en ne gardant que les planètes dont la température est comprise entre 200 et 1000

df2 = exo[(exo['Equilibrium Temperature [K]'] < 1000) & (exo['Equilibrium Temperature [K]'] > 200)]

df2['Equilibrium Temperature [K]'].plot.hist()
plt.show()


# %%
#RAYON !!!!!!!

#on choisi un rayon qui soit compris entre 0,5 et 6 fois celui de la TERRE
df3 = df2[df2['Planet Radius [Earth Radius]'].dropna()]
df4 = df3[(df3['Planet Radius [Earth Radius]'] < 6) & (df3['Planet Radius [Earth Radius]'] > 0,5)]

df3['Planet Radius [Earth Radius]'].plot.hist()
plt.show()


# %%

# %%
df3['Planet Radius [Earth Radius]'].unique()

# %%
#répartition des années de découvertes de planètes
exo['Discovery Year'].plot.hist(bins=80,xlabel='année de découverte',ylabel='nombre de planètes');

# %%
#par nombre d'étoiles
exo['Number of Stars'].plot.hist(bins=100,xlabel="nombre d'étoiles de la planète",ylabel='nombre de planètes');
exo['Planet Radius [Earth Radius]'].dropna().hist(bins = [2*k for k in range(11)],width=1);

# %%
exo['Insolation Flux [Earth Flux]'].dropna().plot.hist(bins = [1*k for k in range(500)],width=1, xlabel='insolation rapportée à celle de la Terre', ylabel = 'nombre de planètes')

# %%
