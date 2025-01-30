from fasthtml.common import *


def gerar_titulo(titulo, subtituilo):
    return Div(
        H1(titulo),
        P(subtituilo),
        P("Esse e um componente")
    )

def gerar_formulario():
    formulario = Form(
        Input(type="text", name="tarefa", placeholder="Insira a tarefa a ser adcionada"),
        Button("Enviar"),
        method="post",
        action="/adcionar_tarefa",
        hx_post="/adcionar_tarefa",
        hx_target="#lista_tarefas",
        hx_swap="outerHTML"
    )
    return formulario

def gerar_lista_tarefas(lista_tarefas):

    itens_lista = [Li(tarefa, " - ", A("Excluir", 
                                    hx_get=f"/deletar/{i}",
                                    hx_target="#lista_tarefas",
                                    hx_swap="outerHTML"
                                    )) for i, tarefa in enumerate(lista_tarefas) ]

    lista = Ul(
        *itens_lista, id="lista_tarefas"
    )
    return lista