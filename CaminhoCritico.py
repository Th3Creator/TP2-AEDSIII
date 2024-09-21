import csv
import networkx as nx

# Função para carregar o arquivo CSV e construir o grafo
def grafo_csv(nomeArquivo):
    G = nx.DiGraph()  # Criando um grafo direcionado

    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Ignorar o cabeçalho, se houver
            for row in reader:
                if len(row) >= 3:
                    source, target, weight = row[0], row[1], int(row[2])
                    G.add_edge(source, target, weight=weight)
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
