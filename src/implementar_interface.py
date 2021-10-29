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


def atualizar_infos(**kwargs):
    janela = kwargs["janela"]
    arquivos = kwargs["arquivos"]
    for input in janela.inputs:
        if input.nome == "server":
            texto = input.input
    
    texto = "server=" + texto + "\n"
    arquivos.refazer_arq("infos.txt", texto)


def texto_ajuda():
    conteudo = ""
    conteudo += "informe o server local a ser conectado\n"
    conteudo += "pelo SQL. para usar as alterações\n"
    conteudo += "deve-se reiniciar o software. informe\n"
    conteudo += "um intervalo e uma lista de individuos\n"
    conteudo += "como indicados no default."
    return conteudo


def atualizar_texto(**kwargs):
    janela = kwargs["janela"]
    texto = kwargs["texto"]
    nome = kwargs["nome"]
    for t in janela.textos:
        if t.nome == nome:
            objeto = t
    
    objeto.conteudo = texto


def setarbots(janela: interface.Janela, ambiente, dados, arquivos):
    """função para criar e adicionar botões na janela"""
    bot_atualizar = interface.Botao(520, 50, 0, 0, "atualizar", "", 30, [120, 120, 120], atualizar_infos, {"janela":janela, "arquivos":arquivos})
    bot_pausar = interface.Botao(520, 130, 0, 0, "pausar", "", 30, [120, 120, 120], ambiente.mudar_pause)
    bot_plotar = interface.Botao(520, 290, 0, 0, "plotar", "", 30, [120, 120, 120], receber_dados, {"janela":janela, "dados":dados})
    bot_ajuda = interface.Botao(510, 330, 0, 0, "ajuda", "", 30, [120, 120, 120], atualizar_texto, {"janela":janela, "texto":texto_ajuda(), "nome": "ajuda"})
    janela.addBotões([bot_atualizar, bot_pausar, bot_plotar, bot_ajuda])


def setartextos(janela: interface.Janela):
    """função para criar e adicionar textos na janela"""
    text_banco = interface.Texto(510, 10, 30, "banco de dados:", "")
    text_nome = interface.Texto(520, 50, 30, "nome:", "")
    text_simulacao = interface.Texto(510, 90, 30, "simulação:", "")
    text_grafico = interface.Texto(510, 170, 30, "grafico:", "")
    text_inter = interface.Texto(520, 210, 30, "intervalo t:", "")
    text_pops = interface.Texto(520, 250, 30, "pops:", "")
    text_ajuda = interface.Texto(510, 370, 20, "", "ajuda")
    janela.addTextos([text_banco, text_nome, text_simulacao, text_grafico, text_inter, text_pops, text_ajuda])


def setarinputs(janela: interface.Janela):
    """função para criar e adicionar inputs na janela"""
    inpu_server = interface.Inp(690, 50, 8, 30, "", "server")
    inpu_inter = interface.Inp(690, 210, 8, 30, "0-50", "inter")
    inpu_pops = interface.Inp(690, 250, 8, 30, "1, 2", "pops")
    janela.addInputs([inpu_server, inpu_inter, inpu_pops])


def setarquads(janela: interface.Janela, ambiente):
    """função para criar e adicionar quadrados na janela"""
    quads = []
    for pop in ambiente.pops["eco"]:
        quads.append(interface.Quadrado(pop.x, pop.y, 10, [10, 10, 10], pop.nome))

    janela.addQuads(quads)


def main(dimensoes, ambiente, dados, arquivos):
    """inicia um objeto Janela, seta suas caracteristicas iniciais, 
    assim como seu botões, textos inputs e imagens. retorna o objeto"""
    janela = interface.Janela(dimensoes[0], dimensoes[1], "Ecos", [ambiente.step])
    setarbots(janela, ambiente, dados, arquivos)
    setartextos(janela)
    setarinputs(janela)
    setarquads(janela, ambiente)
    janela.iniciar()
    return janela
