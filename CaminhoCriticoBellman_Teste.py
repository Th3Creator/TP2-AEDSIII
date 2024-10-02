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
                nome = row['Nome']
                periodo = int(row['Período'])
                duracao = int(row['Duração'])
                dependencias = row['Dependências']

                # Adiciona o nó correspondente ao curso
                G.add_node(codigo, nome=nome, periodo=periodo, duracao=duracao)

                # Se houver dependências, adiciona arestas entre os cursos
                if dependencias:
                    for dependencia in dependencias.split(';'):  # Modificado para ';' em vez de ','
                        G.add_edge(dependencia.strip(), codigo, weight=duracao)  # Peso positivo para a duração

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

    # Inicializar as variáveis
    longest_path = []
    max_duration = -math.inf

    # Percorre cada nó fonte e aplica o Bellman-Ford para encontrar o caminho mais longo
    for source in sources:
        try:
            # Tenta encontrar o caminho mais longo a partir dessa fonte
            distancias = nx.single_source_bellman_ford_path_length(G, source, weight='weight')
            for node, distance in distancias.items():
                if distance > max_duration:
                    max_duration = distance
                    longest_path = nx.bellman_ford_path(G, source, node, weight='weight')
        except nx.NetworkXUnbounded:
            print("Erro: O grafo contém um ciclo de dependência.")
            return None, None

    # Ordenar pelo período para garantir que os cursos estão na ordem temporal correta
    longest_path = sorted(longest_path, key=lambda x: G.nodes[x]['periodo'])
    
    # Calcular a duração total do caminho crítico com base na soma das durações dos cursos
    duracao_total = sum(G.nodes[curso]['duracao'] for curso in longest_path)

    return longest_path, duracao_total

# Função para imprimir o caminho crítico com os nomes dos cursos
def imprimir_caminho_critico(G, caminho_critico, duracao_total):
    print("\nCaminho Crítico:")
    for curso in caminho_critico:
        nome_curso = G.nodes[curso]['nome']
        print(f"- {nome_curso}")

    print(f"\nTempo Mínimo: {duracao_total}")

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
            caminho_critico, duracao_total = encontrar_caminho_critico(grafo)
            if caminho_critico:
                imprimir_caminho_critico(grafo, caminho_critico, duracao_total)
            else:
                print("Não foi possível encontrar o caminho crítico.")
        else:
            print("Não foi possível carregar o grafo.")

if __name__ == "__main__":
    main()
