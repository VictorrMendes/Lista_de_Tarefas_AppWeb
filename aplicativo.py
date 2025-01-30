from fasthtml.common import *
from componentes import *


app, routes = fast_app()

lista_tarefas = []

#Pagina Inicial
@routes("/")
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
    return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)

#adcionar tarefa
@routes("/adcionar_tarefa", methods=["post"])
def adcionar_tarefa(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
    
    return gerar_lista_tarefas(lista_tarefas)

@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefas) > posicao:
        lista_tarefas.pop(posicao)
    return gerar_lista_tarefas(lista_tarefas)

@routes("/blog")
def homepage():
    return gerar_titulo("Homepage","Lista To_do")

serve()