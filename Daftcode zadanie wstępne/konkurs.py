# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 01:06:29 2017

@author: piotr
"""

import numpy as np
import pandas as pd
dataset = pd.read_csv("conferences_data.csv", sep=';')

#Zadanie 1
#1. Ilu uczestników było na więcej niż jednej konferencji?
dataset.columns = [c.replace(' ', '_') for c in dataset.columns]
unique_0 = dataset.konferencja_0.unique()
unique_1 = dataset.konferencja_1.unique()
unique_2 = dataset.konferencja_2.unique()
unique_3 = dataset.konferencja_3.unique()
unique_4 = dataset.konferencja_4.unique()
unique_5 = dataset.konferencja_5.unique()

df = pd.read_csv("wektor.csv", sep=';')
