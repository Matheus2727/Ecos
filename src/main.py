import eco
import dados
import ambiente
import arquivos
import integracao_sql as isq
import implementar_barreira as imb
import implementar_interface as imi

def iniciar_pops(mundo):
    """recebe um objeto Ambiente, cria objetos Eco (individuos) e adiciona esses
    individuos no ambiente"""
    pops = []
    n = 0
    for _ in range(10):
        nome = str(n)
        pop = eco.Eco(nome, "aaa", mundo, 100, 100, [40,90])
        pops.append(pop)
        n += 1

    mundo.add_pops(pops)

def main():
    """cria os objetos iniciais do programa. se o integrador não puder ser criado, o programa
    ainda abrirá a interface."""
    dimensoes = [500, 500]
    dimensoes_janela = [900, 500]
    arq = arquivos.Arquivos()
    try: # tenta criar o integrador
        integrador = isq.Integrador_SQL("Ecos", arq)
    
    except:
        integrador = ""
        print("integrador nao encontrado, informe outro servidor")

    da = dados.Dados([], integrador)
    amb = ambiente.Ambiente(dimensoes, [], da)
    barreira = imb.main([0, dimensoes[0]], [0, dimensoes[1]], "e")
    amb.add_barreiras([barreira])
    iniciar_pops(amb)
    janela = imi.main(dimensoes_janela, amb, da, arq)
    amb.janela = janela
    janela.main_loop()

if __name__ == "__main__":
    main()
