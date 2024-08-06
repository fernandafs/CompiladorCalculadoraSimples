# Calculadora Simples

  Este projeto baseia-se no desenvolvimento de um compilador para uma calculadora simples, com capacidade de interpretar e executar expressões matemáticas básicas. Este projeto é desenvolvido no contexto da disciplina de Compiladores e Interpretadores da Universidade Federal do ABC (UFABC).

  Este projeto visa combinar o aprendizado teórico da disciplina de Compiladores e Interpretadores com uma aplicação prática. Através deste projeto, espera-se adquirir uma compreensão mais profunda dos processos envolvidos na criação de compiladores e interpretadores, bem como habilidades práticas em desenvolvimento de software.

## Integrante

- Nome: Fernanda Felix.
- RA: 11201921613.

## Objetivos
Desenvolver um analisador léxico e sintático:

- Utilizar ferramentas de parsing para analisar e interpretar expressões matemáticas.
- Garantir que a calculadora possa lidar com operações básicas como adição, subtração, multiplicação e divisão.
- Implementar a gestão de erros que informe ao usuário sobre erros de sintaxe ou léxicos nas expressões inseridas.

## Funcionalidades

- Análise Léxica: Reconhecimento de tokens como números, operadores e parênteses e conversão de expressões em uma sequência de tokens para posterior análise.
- Análise Sintática: Construção de um analisador sintático que valide a estrutura das expressões matemáticas.
- Suporte a operações aritméticas básicas: `+`, `-`, `*`, `/` e `^`.
- Suporte a parênteses para expressões complexas.
- Atribuição e uso de variáveis.
- Botão de "Clear" para limpar a entrada.
- Botão de "Backspace" para apagar o último caractere.
- Entrada via teclado e via interface gráfica (Permite-se que use a interface para escrever a expressão, assim como é possível utilizar o teclado também para a entrada dos dados).
- Interface gráfica para facilitar o uso.

## Requisitos

- Python 3.x.
- Biblioteca PLY (localizado no requirements.txt).
- Biblioteca Tkinter (inclusa no Python padrão).

## Execução via web

- Replit: Replit é uma plataforma online que suporta uma grande variedade de linguagens de programação e oferece um ambiente de desenvolvimento integrado (IDE) na web.
- Link:[ Replit](https://replit.com/~)
- Como Usar:
    1. Na home do Replit, utilize a opção "Import from GitHub";
    2. Conecte-se a sua conta, procure o projeto pela URL e faça a importação;
    3. Adicione, em comandos, a seguinte linha: "python main.py" e confirme;
    4. Execute o código utilizando o botão de run.
 
## Bibliografia 

- Documentação PLY: https://ply.readthedocs.io/en/latest/
- Documentação Tkinter: https://docs.python.org/pt-br/dev/library/tkinter.html
