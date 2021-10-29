import interface
import grafico


def exemplo(**kwargs):
    """função de exemplo para ser usada em um botão"""
    print("a")


def receber_dados(**kwargs):
    janela = kwargs["janela"]
    dados = kwargs["dados"]
    inter = ""
    pops = ""
    for input in janela.inputs:
        if input.nome == "inter":
            inter = input.input
        
        elif input.nome == "pops":
            pops = input.input
    
    da = dados.receber_dados_SQL(**{"inter":inter, "pops":pops})
    gr = grafico.Grafico_Vetores(da[0])
    gr.add_vetores(da[1])
    gr.plotar()


def setarbots(janela: interface.Janela, ambiente, dados):
    """função para criar e adicionar botões na janela"""
    bot_pausar = interface.Botao(520, 130, 0, 0, "pausar", "", 30, [120, 120, 120], ambiente.mudar_pause)
    bot_plotar = interface.Botao(520, 290, 0, 0, "plotar", "", 30, [120, 120, 120], receber_dados, {"janela":janela, "dados":dados})
    janela.addBotões([bot_pausar, bot_plotar])


def setartextos(janela: interface.Janela):
    """função para criar e adicionar textos na janela"""
    text_simulacao = interface.Texto(510, 90, 30, "simulação:", "")
    text_grafico = interface.Texto(510, 170, 30, "grafico:", "")
    text_inter = interface.Texto(520, 210, 30, "intervalo t:", "")
    text_pops = interface.Texto(520, 170, 30, "pops:", "")
    janela.addTextos([text_simulacao, text_grafico, text_inter, text_pops])


def setarinputs(janela: interface.Janela):
    """função para criar e adicionar inputs na janela"""
    inpu_inter = interface.Inp(690, 130, 10, 30, "0-50", "inter")
    inpu_pops = interface.Inp(690, 170, 10, 30, "1, 2", "pops")
    janela.addInputs([inpu_inter, inpu_pops])


def setarquads(janela: interface.Janela, ambiente):
    """função para criar e adicionar quadrados na janela"""
    quads = []
    for pop in ambiente.pops["eco"]:
        quads.append(interface.Quadrado(pop.x, pop.y, 10, [10, 10, 10], pop.nome))

    janela.addQuads(quads)


def main(dimensoes, ambiente, dados):
    """inicia um objeto Janela, seta suas caracteristicas iniciais, 
    assim como seu botões, textos inputs e imagens. retorna o objeto"""
    janela = interface.Janela(dimensoes[0], dimensoes[1], "Ecos", [ambiente.step])
    setarbots(janela, ambiente, dados)
    setartextos(janela)
    setarinputs(janela)
    setarquads(janela, ambiente)
    janela.iniciar()
    return janela
