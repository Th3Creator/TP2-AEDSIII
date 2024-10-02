# TP2-AEDSIII

# Caminho Crítico

## Descrição do Projeto

Este projeto visa carregar um arquivo CSV contendo informações de cursos e suas dependências, construindo um grafo direcionado que representa as relações entre os cursos. A partir desse grafo, o programa identifica o **caminho crítico**, que é a sequência mais longa de cursos levando em consideração suas durações, e exibe o tempo mínimo para conclusão do projeto (currículo).

## Funcionalidades Principais

- **Carregar o Grafo a partir de um CSV**: O programa lê o arquivo CSV e constrói um grafo direcionado utilizando a biblioteca `NetworkX`. Os nós representam os cursos, e as arestas, as dependências entre eles, com pesos baseados na duração dos cursos.

- **Encontrar o Caminho Crítico**: Utilizando o algoritmo de Bellman-Ford adaptado, o programa calcula o caminho crítico (caminho mais longo), que determina o tempo mínimo para conclusão dos cursos.

- **Exibir o Caminho Crítico**: O caminho crítico é impresso no terminal, exibindo a sequência de cursos na ordem correta e o tempo total necessário.

## Como Funciona

### Estrutura do Código

1. `grafo_csv(nomeArquivo)`: 
   - Carrega o arquivo CSV e constrói um grafo direcionado onde os cursos são representados por nós e suas dependências por arestas.
   
2. `encontrar_caminho_critico(G)`: 
   - Utiliza o algoritmo de Bellman-Ford para encontrar o caminho crítico, que é o caminho mais longo dentro do grafo.
   
3. `imprimir_caminho_critico(G, caminho_critico, duracao_total)`:
   - Imprime a sequência dos cursos no caminho crítico e a duração total.

4. `main()`:
   - Função principal que interage com o usuário, solicitando o nome do arquivo CSV e exibindo o caminho crítico com base nos dados fornecidos.

### Instruções de Execução

1. Certifique-se de que o arquivo CSV está no formato correto (Código,Nome,Período,Duração,Dependências).
2. Execute o script.
3. Insira o arquivo, seguindo o modelo "arquivos_csv/nomeArquivo.csv".
4. O programa carregará os dados e exibirá o caminho crítico com o tempo mínimo de conclusão.

## Autores

Felipe Fialho e Christian Daniel
