"""
Considere para efeito deste projeto que uma determinada universidade oferece anualmente uma lista de
cinquenta (50) projetos financiados e abertos a participação de alunos, com um máximo de 80 vagas.
Cada projeto é orientado e gerenciado por professores que estabelecem as quantidades mínima e
máxima de alunos que podem ser aceitos em determinado projeto, bem como requisitos de histórico e
tempo disponível que os alunos devem possuir para serem aceitos. Esses requisitos de histórico e tempo
são pré-avaliados e cada aluno possui uma Nota agregada inteira de [3, 4, 5], sendo 3 indicando
suficiente, 4 muito boa, e 5 excelente. Neste ano, duzentos (200) alunos se candidataram aos projetos. O
ideal é que o máximo de projetos sejam realizados, mas somente se o máximo de alunos qualificados
tenham tido o interesse para tal. Para uma seleção impessoal e competitiva um algoritmo que realize um
emparelhamento estável máximo deve ser implementado. Este projeto pede a elaboração,
implementação e testes com a solução final de emparelhamento máximo estável para os dados
fornecidos. Os alunos podem indicar no máximo três (3) preferências em ordem dos projetos. Variações
do algoritmo Gale-Shapley devem ser usadas, com uma descrição textual no arquivo README do
projeto indicando qual variação/lógica foi utilizada/proposta.

O programa deve implementar uma interface com visualização colorida do grafo bipartido e das
soluções propostas de emparelhamento, ao longo da evolução com dez (10) iterações de
emparelhamento em laço, organizando as saídas até a alocação final. Um índice de preferência por
projeto deve ser calculado, bem como visualizada uma matriz final dos emparelhamentos com as ordens
de escolhas de emparelhamentos finais dos alunos.

As soluções dadas em (Abraham, Irving & Manlove, 2007) são úteis e qualquer uma pode ser
implementada com variações pertinentes. Um arquivo entradaProj2.25TAG.txt com as indicações de
código do projeto, número de vagas, requisito mínimo das vagas, bem como dos alunos com suas
preferências de projetos na ordem e suas notas indviduais, é fornecido como entrada. Uma versão
pública do artigo de (Abraham, Irving & Manlove, 2007) é fornecida para leitura.
"""
import re
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
from visualizar_Grafo_inicial import exibir_grafo 

class Emparelhamento:
    """ 
        Classe para implementação de emparelhamento estável utilizando
        variações do algoritmo Gale-Shapley. Contém funções suporte para
        organização e mostra dos dados.

        Passos:
        ↣ 1. Ler os dados de entrada disponibilizados
        ↣ 2. Organizar as filas de preferências
        ↣ 3. Emparelhar alunos e projetos com base nas preferências
        ↣ 4. Visualizar o grafo bipartido e os emparelhamentos
    """
    def construir_grafo_inicial(self):
        """
        Constrói o grafo bipartido inicial, adicionando nós para alunos e projetos,
        e arestas entre eles com base nas preferências dos alunos e requisitos de nota dos projetos.
        """
        # 1. Adiciona nós para os alunos
        for codigo_aluno in self.alunos.keys():
            self.grafo.add_node(codigo_aluno, bipartite=0) # '0' representa o conjunto dos alunos

        # 2. Adiciona nós para os projetos
        for codigo_projeto in self.projetos.keys():
            self.grafo.add_node(codigo_projeto, bipartite=1) # '1' representa o conjunto dos projetos
        print("Nós de alunos e projetos criados no grafo.")

        # 3. Adiciona arestas com as combinações possíveis
        for codigo_aluno, info_aluno in self.alunos.items():
            nota_aluno = info_aluno['nota']
            preferencias_aluno = info_aluno['preferencias']

            for projeto_preferido_id in preferencias_aluno:
                # Verifica se o projeto preferido existe no dicionário de projetos
                if projeto_preferido_id in self.projetos:
                    info_projeto = self.projetos[projeto_preferido_id]
                    nota_min_projeto = info_projeto['nota_min']

                    # Verifica se a nota do aluno atende ao requisito mínimo do projeto
                    if nota_aluno >= nota_min_projeto:
                        # Adiciona a aresta entre o aluno e o projeto
                        # Você pode adicionar atributos à aresta se quiser, como a nota do aluno
                        self.grafo.add_edge(codigo_aluno, projeto_preferido_id, nota=nota_aluno)
        print("Arestas qualificadas adicionadas ao grafo.")
        print(f"Grafo inicial construído com {self.grafo.number_of_nodes()} nós e {self.grafo.number_of_edges()} arestas.")    
        return self.grafo
    
    def __init__(self, grafo: nx.Graph):
        self.grafo = grafo
        self.alunos = {}
        self.projetos = {}

    def organiza_dados(self, alunos_txt: str = "alunos.txt", projetos_txt: str = "projetos.txt") -> None:
        """
        Função para extrair os dados de entrada e atualizar os dicionários de alunos e projetos.
        
        Args:
            alunos (str): caminho para o txt dos alunos
            projetos (str): caminho para o txt dos projetos
        """
        try:
            # Lendo o arquivo de projetos
            with open(projetos_txt, encoding="utf-8") as f:
                linhas = f.readlines()
            for linha in linhas:
                linha = linha.strip()
                if linha or not linha.startswith("//"):
                    # Aplica um regex para extrair os dados
                    match = re.match(r"\((P\d+),\s*(\d+),\s*(\d+)\)", linha)
                    if match:
                        codigo, vagas, nota_min = match.groups()
                        # Atualiza o dicionário com as informações necessárias
                        self.projetos[codigo] = {"vagas": int(vagas), "nota_min": int(nota_min)}

            # Lendo o arquivo de alunos
            with open(alunos_txt, encoding="utf-8") as f:
                linhas = f.readlines()
            for linha in linhas:
                linha = linha.strip()
                if linha or not linha.startswith("//"):
                    # Aplica outro regex para extrair os dados
                    match = re.match(r"\((A\d+)\):\(([^)]+)\)\s*\((\d+)\)", linha)
                    if match:
                        codigo, prefs, nota = match.groups()
                        preferencias = [pref.strip() for pref in prefs.split(",")]
                        self.alunos[codigo] = {"preferencias": preferencias, "nota": int(nota)}

            print("Dados organizados com sucesso!")

            for codigo, projeto in self.projetos.items():
                print(f"Projeto {codigo}: Vagas={projeto['vagas']}, Nota Mínima={projeto['nota_min']}")
            for codigo, aluno in self.alunos.items():
                print(f"Aluno {codigo}: Preferências={aluno['preferencias']}, Nota={aluno['nota']}")

        except Exception as e:
            print(f"Algo deu errado! {e}")

#    def visualizar_grafo(self) -> None:
#        """
#        Função para visualizar o grafo bipartido de alunos e projetos.
#        """
        # TODO, precisamos implementar a lógica de visualização do grafo aqui

    def gale_shapley(self) -> None:
        """
        Variação do algoritmo Gale-Shapley para emparelhamento estável entre alunos e projetos.

        Args:
            projetos (dict): Dicionário com os projetos e suas informações.
            alunos (dict): Dicionário com os alunos e suas preferências.
        Returns:
            nx.Graph: Grafo bipartido com os emparelhamentos estáveis.
        """
        # TODO, precisamos implementar a lógica do algoritmo Gale-Shapley aqui

if __name__ == "__main__":
    # Criação do grafo bipartido
    emparelhamento = Emparelhamento(nx.Graph())
    emparelhamento.organiza_dados()
    grafo_inicial = emparelhamento.construir_grafo_inicial()
    exibir_grafo(grafo_inicial)
