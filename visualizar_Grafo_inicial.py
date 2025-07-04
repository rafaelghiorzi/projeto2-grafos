import matplotlib.pyplot as plt
import networkx as nx

def exibir_grafo(grafo: nx.Graph, titulo: str = "Grafo Bipartido Inicial") -> None:
    """
    Exibe um grafo bipartido com rótulos
    """
    if not grafo.nodes():
        print("O grafo fornecido para visualização está vazio.")
        return

    # Identifica os conjuntos bipartidos com base no atributo 'bipartite'
    set_alunos = {n for n, d in grafo.nodes(data=True) if d.get("bipartite") == 0}
    set_projetos = {n for n, d in grafo.nodes(data=True) if d.get("bipartite") == 1}

    # Se a identificação bipartida falhar, tentamos inferir com base nos nomes ou total de nós.
    if not set_alunos and not set_projetos:
        set_alunos = {n for n in grafo.nodes() if n.startswith('A')}
        set_projetos = {n for n in grafo.nodes() if n.startswith('P')}
        if not set_alunos or not set_projetos:
            print("Aviso: Não foi possível identificar as partições bipartidas (bipartite=0/1 ou 'A'/'P' no nome).")
            print("O layout bipartido pode não ser aplicado corretamente.")
            # Se ainda assim não der, use um layout genérico
            pos = nx.spring_layout(grafo)
        else:
            # Caso os atributos não existam, mas os nomes sigam o padrão 'A'/'P'
            pos = nx.bipartite_layout(grafo, set_alunos)
    else:
        # Caso os atributos estejam corretos, use o layout bipartido
        pos = nx.bipartite_layout(grafo, set_alunos)

    # Determina o espaçamento vertical e a altura da figura de forma dinâmica
    # para melhor acomodar a quantidade de nós.
    num_max_nodes_side = max(len(set_alunos), len(set_projetos))
    espacamento_vertical = 1.0 # Espaçamento base entre os nós
    
    # Ajusta o node_size e font_size com base no número de nós
    if num_max_nodes_side > 100:
        node_size = 150
        font_size = 5
    elif num_max_nodes_side > 50:
        node_size = 250
        font_size = 6
    else:
        node_size = 400
        font_size = 7

    altura_figura = max(10, num_max_nodes_side * espacamento_vertical * 0.2) 

    plt.figure(figsize=(15, altura_figura)) # Aumentei um pouco a largura para rótulos

    # Desenha os nós dos alunos
    nx.draw_networkx_nodes(grafo, pos, nodelist=list(set_alunos), node_color="#87CEFA", # Azul claro
                           node_size=node_size, edgecolors='black', label="Alunos", alpha=0.9)
    
    # Desenha os nós dos projetos
    nx.draw_networkx_nodes(grafo, pos, nodelist=list(set_projetos), node_color="#98FB98", # Verde claro
                           node_size=node_size, edgecolors='black', label="Projetos", alpha=0.9)

    # Desenha as arestas
    nx.draw_networkx_edges(grafo, pos, width=0.8, alpha=0.5, edge_color="gray")

    # Desenha os rótulos dos nós
    nx.draw_networkx_labels(grafo, pos, font_size=font_size, font_weight='bold')

    plt.title(titulo, fontsize=16, pad=20) # Título maior e com mais espaçamento
    plt.axis("off") # Desliga os eixos
    plt.tight_layout() # Ajusta o layout para evitar sobreposição
    plt.show() # Exibe a janela do grafo