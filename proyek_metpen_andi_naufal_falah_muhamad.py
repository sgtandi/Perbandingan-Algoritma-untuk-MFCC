# -*- coding: utf-8 -*-
"""Proyek Metpen_Andi Naufal Falah Muhamad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3UZ-v58LoVcPQTXMITjgbv7IdbD4Sws
"""

import pandas as pd
import numpy as np

from google.colab import files
data = files.upload()
for fn in data.keys():
  print ('Nama file "{name}" dengan panjang {length} bytes'.format(
      name=fn, length=len(data[fn])))

data = pd.read_csv('accent-mfcc-data-1.csv')

data.head(329)

"""NORMALISASI"""

def cetak_rentang(df_input):
  list_fitur = df_input.columns[1:] #mengambil nama kolom, kecuali yang terakhir (kelas)
  for fitur in list_fitur:
    max = df_input[fitur].max()
    min = df_input[fitur].min()
    print("Rentang fitur ", fitur, " adalah ", max-min)

cetak_rentang(data)

def minmax(df_input):
  list_fitur = df_input.columns[1:]
  for fitur in list_fitur:
    max = df_input[fitur].max()
    print("Max dari",fitur, "adalah ",max)
    min = df_input[fitur].min()
    print("Min dari",fitur, "adalah ",min)
    df_input[fitur] = (df_input[fitur]-min)/(max-min)
    print("")
  return df_input

data_normal = minmax(data)

data_normal.head()

cetak_rentang(data_normal)

"""# Naive Bayes"""

X = data_normal.drop('language', axis=1)
y = data_normal['language']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
accuracy

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))

"""# Decision Trees"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""# SVM"""

from sklearn.svm import SVC

SVM_Model = SVC(gamma='auto')

SVM_Model.fit(X_train,y_train)

print (f'Accuracy - : {SVM_Model.score(X,y):.3f}')

SVM_pred = SVM_Model.predict(X_test)

print(classification_report(y_test, SVM_pred))