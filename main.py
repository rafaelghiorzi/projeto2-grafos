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
import matplotlib.pyplot as plt

def variacao_gale_shapley():
    """
    Função para implementar uma variação do algoritmo de Gale-Shapley
    para emparelhamento estável máximo entre alunos e projetos.

    Passos:
    ↣ 1. Ler os dados de entrada disponibilizados
    ↣ 2. Organizar as filas de preferências
    ↣ 3. Emparelhar alunos e projetos com base nas preferências
    ↣ 4. Visualizar o grafo bipartido e os emparelhamentos
    """

