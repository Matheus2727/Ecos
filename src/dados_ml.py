import random
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class DadosML:
    def __init__(self, DataFrame, outputs:list, scalar:bool=False):
        sc = StandardScaler()
        self.df = DataFrame
        dados_inp = self.df.drop(outputs, axis=1)
        dados_out = self.df[outputs]
        itrain, itest, otrain, otest = train_test_split(dados_inp, dados_out, test_size = 0.2, random_state = 42)
        self.itrain = itrain
        self.itest = itest
        self.otrain = otrain
        self.otest = otest
        if scalar:
            self.itrain =sc.fit_transform(self.itrain)
            self.itest = sc.fit_transform(self.itest)

def main():
    df = pd.read_csv("dados.csv", sep=";")
    for nome in df:
        for i, v in enumerate(df[nome]):
            df[nome][i] = df[nome][i]*random.choice([0.8, 1.3, 1.5])

    # print(df.head(20))
    bins = (2, 4.5, 6.5, 8)
    group_names = ["bad", "normal", "good"]
    df["quality"] = pd.cut(df["quality"], bins = bins, labels = group_names)
    label_quality = LabelEncoder() # 0 ou 1 pra bad ou good
    df["quality"] = label_quality.fit_transform(df["quality"])
    # print(df.head(20))
    dados = DadosML(df, ["quality"], True)
    return dados

if __name__ == "__main__":
    main()
