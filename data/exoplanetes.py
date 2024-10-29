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
#répartition des années de découvertes de planètes
exo['Discovery Year'].plot.hist(bins=80,xlabel='année de découverte',ylabel='nombre de planètes');

# %%
#par nombre d'étoiles
exo['Number of Stars'].plot.hist(bins=100,xlabel="nombre d'étoiles de la planète",ylabel='nombre de planètes');
exo['Planet Radius [Earth Radius]'].dropna().hist(bins = [2*k for k in range(11)],width=1);

# %%
exo['Insolation Flux [Earth Flux]'].dropna().plot.hist(bins = [1*k for k in range(500)],width=1, xlabel='insolation rapportée à celle de la Terre', ylabel = 'nombre de planètes')

# %%
