import pyfiglet
import time
import sys
import analisecarteira as ac
import calcularretornos as cr
#Importações para a realização desse código

def banner():
    f = pyfiglet.Figlet(font='big')
    print(f.renderText("Ponto Otimo"))
    #Criação do banner através do pyfiglet
def introducao():
    imprimir_letra_por_letra("Bem-vindo ao nosso otimizador de carteiras!")
    #O imprimir letra por letra foi uma ideia da nossa equipe, achamos que ia ficar bem esteticamente. O print sem nada logo depois é porque essa função não pula uma linha quando ela termina
    print()
    print() 
    #Função estética mesmo
def exibir_menu():
    while True:
        #Loop para sempre ficar repetindo o menu principal
        time.sleep(2) #Comando estético para fazer o código dormir/pausar por um determinado tempo
        imprimir_letra_por_letra("O que quer fazer? :")
        print()
        imprimir_letra_por_letra("1. Carteira de Investimentos ")
        print()
        imprimir_letra_por_letra("2. Ativos Disponíveis ")
        print()
        imprimir_letra_por_letra("3. Sair")
        print()
        escolha = input("Digite um número (Ex: 1) : ")
        #Imprimir o layout do menu principal e pedir através de um input a escolha que a pessoa quer
        if escolha == "1":
            imprimir_letra_por_letra("Antes de começarmos, é bom explicar que vão ser formadas duas carteiras uma privada")
            print()
            imprimir_letra_por_letra("e uma pública, ou seja uma com  2 ativos privados e outra com 2 públicos respectivamente.")
            print()
            imprimir_letra_por_letra("Outra informação importante é que todos os resultados que vão ser dados foram")
            print()
            imprimir_letra_por_letra("adquiridos a partir de uma análise histórica, entregando então um retorno esperado.")
            print()
            imprimir_letra_por_letra("Vamos começar! A escolha dos ativos foi feita a partir da maximização do coeficiente")
            print()
            imprimir_letra_por_letra("de variação, depois foi calculado o melhor índice de sharpe para cada alocação.")
            print()
            imprimir_letra_por_letra("Calculado a alocação foi calculado o retorno. Vamos para os resultados!")
            print()
            print()
            time.sleep(1) #Colocar o código para dormir/pausar
            ac.printcarteiras() #Puxar uma função de outro arquivo que realiza a escolha dos ativos e calcular o Índice de Sharpe
            print()
            cr.printretornosecomparacoes() #Puxar uma função de outro arquivo que realiza o cálculo dos retornos e vai fazer a comparação com alguns índices de mercado
            print()
        elif escolha == "2":
            imprimir_letra_por_letra("Em breve essa ferramenta estará disponível") #Aqui entraria uma outra função que mostraria todos os aitvos disponíveis e as informações individuais de cada um, será implementada se houver tempo
            print() # A ideia é que aqui também será o local em que você poderia adicionar e remover ativos, e logicamente seus dados, para entrar no programa de otimizador de carteiras. Pena que não teve tempo e precisaria de mais estudo sobre outras funções.
        elif escolha == "3":
            break #Opção de sair do programa
        else:
            imprimir_letra_por_letra("Escolha algum valor entre ( 1 , 2 ou 3)") #Aceita apenas os valores 1 2 e 3
            print()

def imprimir_letra_por_letra(texto):
    for letra in texto: #Inicia um loop for que itera sobre cada caractere na string texto. A variável letra é usada para armazenar cada caractere durante cada iteração.
        sys.stdout.write(letra) #Escreve o caractere atual (letra) na saída padrão (normalmente a tela). Isso permite que as letras sejam impressas uma por uma na mesma linha, sem pular para uma nova linha a cada caractere
        sys.stdout.flush() #Garante que a saída seja exibida imediatamente, em vez de ser armazenada em um buffer. Isso é útil para garantir que cada caractere seja exibido assim que for escrito, sem esperar até que o buffer esteja cheio
        time.sleep(0.05)  # Comando ja usado anteriormente que pausa o codigo por um determinado tempo

def main():#Execução das 3 funções principais
    banner()
    introducao()
    exibir_menu()

if __name__ == "__main__":
    main() #uma construção comum em Python e é frequentemente usada para determinar se o script está sendo executado como o programa principal (em oposição a ser importado como um módulo em outro script)
