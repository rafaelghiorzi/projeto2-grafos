# Sistema de Emparelhamento Estável - Projetos e Alunos

## Descrição do Projeto

Este projeto implementa um sistema de emparelhamento estável entre alunos e projetos de pesquisa utilizando uma variação do algoritmo de Gale-Shapley. O sistema foi desenvolvido para resolver o problema de alocação de 200 alunos em 50 projetos de pesquisa, considerando as preferências dos alunos e os requisitos mínimos dos projetos.

A mostra do funcionamento do algoritmo pode ser visualizada no notebook [main.ipynb](main.ipynb).

## Variação do Algoritmo Gale-Shapley Implementada

### Diferenças do Algoritmo Original

O algoritmo implementado é uma **variação orientada por qualificação** do Gale-Shapley clássico:

- **Algoritmo Original**: Projetos possuem listas de preferências explícitas sobre os alunos
- **Nossa Variação**: Projetos têm apenas uma **nota mínima de entrada** e aceitam os melhores alunos qualificados

### Lógica da Implementação

1. **Fase de Propostas**: Alunos fazem propostas para projetos em ordem de preferência
2. **Critério de Aceitação**: Projetos aceitam alunos com nota ≥ nota mínima exigida
3. **Critério de Seleção**: Quando um projeto está lotado, alunos com maiores notas substituem os com menores notas
4. **Estabilidade**: O processo garante que nenhum aluno pode melhorar sua situação fazendo uma nova proposta

## Estrutura dos Dados

### Alunos

- **Formato**: `(A1):(P1, P30, P50) (5)`
- **Código**: Identificador único (A1, A2, ...)
- **Preferências**: Lista de até 3 projetos em ordem de preferência
- **Nota**: Valor inteiro de 3 a 5 (3=suficiente, 4=muito boa, 5=excelente)

### Projetos

- **Formato**: `(P1, 2, 5)`
- **Código**: Identificador único (P1, P2, ...)
- **Vagas**: Número máximo de alunos aceitos
- **Nota Mínima**: Requisito mínimo para participação

## Arquivos do Projeto

```
d:\UnB\TAG\projeto2\
├── main.py                           # Código principal
├── alunos.txt                        # Dados dos alunos
├── projetos.txt                      # Dados dos projetos
├── matriz_emparelhamento_final.csv   # Resultado final
└── README.md                         # Este arquivo
```

## Autor

Projeto desenvolvido para a disciplina de Teoria e Aplicação de Grafos (TAG) - UnB
