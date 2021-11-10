import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import random

class Modelo:
    def __init__(self, input_train, output_train):
        self.input_train = input_train
        self.output_train = output_train
        self.mod = None
    
    def testar(self, input_test, output_test):
        resultado = self.mod.predict(input_test)
        print(classification_report(output_test, resultado))
    
    def __call__(self, input:list)-> list:
        output = self.mod.predict([input])
        return output

class RandomForestC(Modelo):
    def __init__(self, input_train, output_train):
        super().__init__(input_train, output_train)
        self.mod = RandomForestClassifier(n_estimators=200)
        self.mod.fit(self.input_train, self.output_train)

class SupportVectorC(Modelo):
    def __init__(self, input_train, output_train):
        super().__init__(self, input_train, output_train)
        self.mod = svm.SVC()
        self.mod.fit(self.input_train, self.output_train)

class MultilayerPerceptronC(Modelo):
    def __init__(self, input_train, output_train, nodes:tuple):
        super().__init__(self, input_train, output_train)
        self.mod = MLPClassifier(hidden_layer_sizes=nodes, max_iter=500)
        self.mod.fit(self.input_train, self.output_train)
