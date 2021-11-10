import modelos_ml
import dados_ml

def main():
    dados = dados_ml.main()
    rfc = modelos_ml.RandomForestC(dados.itrain, dados.otrain)
    print(rfc([7.4,0.70,0.00,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4]))

main()
