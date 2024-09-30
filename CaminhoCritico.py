import csv
import networkx as nx

# Função para carregar o arquivo CSV e construir o grafo
def grafo_csv(nomeArquivo):
    G = nx.DiGraph()  # Criando um grafo direcionado

    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Verificação dos cabeçalhos
            expected_headers = ['Código', 'Nome', 'Período', 'Duração', 'Dependências']
            if reader.fieldnames != expected_headers:
                print(f"Erro: O arquivo deve conter os cabeçalhos {expected_headers}.")
                return None

            for row in reader:
                codigo = row['Código']
                nome = row['Nome']
                periodo = int(row['Período'])
                duracao = int(row['Duração'])
                dependencias = row['Dependências']

                # Adiciona o nó correspondente ao curso
                G.add_node(codigo, nome=nome, periodo=periodo, duracao=duracao)

                # Se houver dependências, adiciona arestas entre os cursos
                if dependencias:
                    for dependencia in dependencias.split(','):
                        G.add_edge(dependencia.strip(), codigo)

    except FileNotFoundError:
        print(f"Erro: Arquivo {nomeArquivo} não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None

    return G

# Função principal de interação com o usuário
def main():
    while True:
        nomeArquivo = input("Informe o arquivo (0 para sair): ")

        if nomeArquivo == '0':
            print("Encerrando o programa.")
            break
        
        print("Processando ...")
        
        # Carregar o grafo a partir do arquivo CSV
        grafo = grafo_csv(nomeArquivo)

        if grafo is not None:
            print(f"Grafo carregado com {grafo.number_of_nodes()} nós e {grafo.number_of_edges()} arestas.")
        else:
            print("Não foi possível carregar o grafo.")

if __name__ == "__main__":
    main()

