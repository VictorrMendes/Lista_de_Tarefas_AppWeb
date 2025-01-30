# Lista de Tarefas

Este projeto é um aplicativo web simples de Lista de Tarefas (To-Do List) desenvolvido com **Python** e **FastHTML**.

## Tecnologias Utilizadas
- Python
- FastHTML
- HTMX (para requisições assíncronas)

## Instalação e Execução

```sh
# Clone o repositório
- git clone https://github.com/VictorrMendes/Lista_de_Tarefas_AppWeb.git
- cd Lista_de_Tarefas_AppWeb
////////////
# Instale as dependências necessárias
- pip install fasthtml
///////////
# Execute o aplicativo
- python aplicativo.py
///////////
Acesse a aplicação no navegador em:
http://localhost:8000
```




```sh
```

## Funcionalidades

- **Adicionar Tarefa**: O usuário pode inserir uma nova tarefa na lista.
- **Listar Tarefas**: Exibição dinâmica das tarefas cadastradas.
- **Excluir Tarefa**: Permite remover uma tarefa específica da lista.

## Estrutura do Código

- `aplicativo.py`: Contém as rotas e a lógica principal da aplicação.
- `componentes.py`: Define os componentes reutilizáveis da interface, como formulário e lista de tarefas.

## Endpoints

- `/` - Página inicial com o formulário e a lista de tarefas.
- `/adcionar_tarefa` - Endpoint para adicionar novas tarefas (método **POST**).
- `/deletar/{posicao}` - Endpoint para excluir uma tarefa com base na posição na lista.

## Exemplo de Uso

1. Acesse a página inicial.
2. Digite uma tarefa no campo de entrada e clique em "Enviar".
3. A tarefa será adicionada dinamicamente à lista.
4. Clique em "Excluir" para remover uma tarefa específica.

## Melhorias Futuras
- Armazenamento persistente (banco de dados ou arquivo JSON).
- Interface mais estilizada com CSS.
- Implementação de autenticação para usuários.

---
Desenvolvido por **Victor Mendes de Souza**.

