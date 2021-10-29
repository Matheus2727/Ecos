import eco
import dados
import ambiente
import arquivos
import integracao_sql as isq
import implementar_barreira as imb
import implementar_interface as imi

def iniciar_pops(mundo):
    pops = []
    n = 0
    for _ in range(10):
        nome = str(n)
        pop = eco.Eco(nome, "aaa", mundo, 100, 100, [40,90])
        pops.append(pop)
        n += 1

    mundo.add_pops(pops)

def main():
    dimensoes = [500, 500]
    dimensoes_janela = [900, 500]
    arq = arquivos.Arquivos()
    try:
        integrador = isq.Integrador_SQL("Ecos", arq)
    
    except:
        integrador = ""
        print("integrador nao encontrado, informe outro")

    da = dados.Dados([], integrador)
    amb = ambiente.Ambiente(dimensoes, [], da)
    barreira = imb.main([0, dimensoes[0]], [0, dimensoes[1]], "i")
    amb.add_barreiras([barreira])
    iniciar_pops(amb)
    janela = imi.main(dimensoes_janela, amb, da, arq)
    amb.janela = janela
    janela.main_loop()

if __name__ == "__main__":
    main()
