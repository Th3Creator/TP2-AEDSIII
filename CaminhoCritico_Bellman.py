import csv
import networkx as nx
import math

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
                G.add_node(codigo, nome=row['Nome'], periodo=int(row['Período']), duracao=int(row['Duração']))

                dependencias = row['Dependências'].split(';') if row['Dependências'] else []
                for dependencia in map(str.strip, dependencias):
                    G.add_edge(dependencia, codigo, weight=int(row['Duração']))

    except FileNotFoundError:
        print(f"Erro: Arquivo {nomeArquivo} não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None

    return G

# Função para encontrar o caminho crítico
def encontrar_caminho_critico(G):
    # Acha a fonte do grafo (nó sem predecessores)
    sources = [n for n in G.nodes if G.in_degree(n) == 0]
    
    max_path = []
    max_duration = -math.inf

    for source in sources:
        try:
            # Tenta encontrar todos os caminhos a partir dessa fonte
            for target in G.nodes:
                if nx.has_path(G, source, target):
                    path = nx.bellman_ford_path(G, source, target, weight='weight')
                    path_duration = sum(G.nodes[node]['duracao'] for node in path)
                    
                    # Verifica se o caminho é mais longo
                    if path_duration > max_duration or (path_duration == max_duration and len(path) > len(max_path)):
                        max_duration = path_duration
                        max_path = path
                        
        except nx.NetworkXUnbounded:
            print("Erro: O grafo contém um ciclo de dependência.")
            return None, None

    # Ordenar o caminho crítico pelo período
    max_path.sort(key=lambda x: G.nodes[x]['periodo'])

    return max_path, max_duration

# Função para imprimir o caminho crítico com os nomes dos cursos
def imprimir_caminho_critico(G, caminho_critico, duracao_total):
    print("\nCaminho Crítico:")
    for curso in caminho_critico:
        print(f"- {G.nodes[curso]['nome']}")

    print(f"\nTempo Mínimo: {duracao_total}")

# Função principal de interação com o usuário
def main():
    while True:
        nomeArquivo = input("Informe o arquivo (0 para sair): ")
        if nomeArquivo == '0':
            print("Encerrando o programa.")
            break
        
        print("Processando ...")
        grafo = grafo_csv(nomeArquivo)

        if grafo:
            caminho_critico, duracao_total = encontrar_caminho_critico(grafo)
            if caminho_critico:
                imprimir_caminho_critico(grafo, caminho_critico, duracao_total)
            else:
                print("Não foi possível encontrar o caminho crítico.")
        else:
            print("Não foi possível carregar o grafo.")

if __name__ == "__main__":
    main()
