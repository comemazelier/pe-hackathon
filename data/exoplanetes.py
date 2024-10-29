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
#on en renomme une des deux pour pouvoir les utiliser comme noms de colonne dans le dataframe
titres[26]='Planet Radius Limit Flag 2'

# %%
exo=pd.read_csv('exoplanete.csv',skiprows=97,names=titres,index_col='Planet Name')

# %%
#si jamais il y a des lignes ou colonnes vides
exo.dropna(how='all',axis=0,inplace=True)
exo.dropna(how='all',axis=1,inplace=True)

# %%
exo

# %%