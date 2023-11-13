import numpy as np
import pandas as pd
import statistics
import ativos as at
import indices
import analisecarteira as ac
import pontootimo as po
import matplotlib.pyplot as plt

def rendadis():
    rendadisponivel = float(input("Qual o montante você ira colocar nas carteiras?(Ex: R$2000 ):  ").replace("R", "").replace("$", ""))
    return rendadisponivel
    #   Função que vai perguntar a renda disponível que vai ser investida
def retornos():
    rendadisponivel = rendadis()
    ativosprivados = ac.escolha_dos_ativos_privados() #Lista puxando as informações dos ativos escolhidos
    ativospublicos = ac.escolha_dos_ativos_publicos() #Lista puxando as informações dos ativos escolhidos
    alocacaoprivadaA = round(ac.sharpe_privado()[1],3) #Alocações
    alocacaopublicaA = round(ac.sharpe_publico()[1],3) #Alocações
    alocacaoprivadaB = round(1 - alocacaoprivadaA,3) #Alocações
    alocacaopublicaB = round(1 - alocacaopublicaA,3) #Alocações
    rendadisponivel = rendadisponivel/2 #Dividir a renda por dois, pois será alocado igualmente em cada carteira
    retornoativoAprivadop = ativosprivados[2] - 1 #Retornos em forma de percentual
    retornoativoBprivadop = ativosprivados[5] - 1 #Retornos em forma de percentual
    retornoativoApublicop = ativospublicos[2] - 1 #Retornos em forma de percentual
    retornoativoBpublicop = ativospublicos[5] - 1 #Retornos em forma de percentual
    #Puxando variáveis para fazer os calculos de retorno

    retornoativoAprivadors = round(alocacaoprivadaA * retornoativoAprivadop * rendadisponivel,2) #Multiplicação da renda,alocação e retorno do ativo para saber o retorno em moeda do ativo A
    retornoativoBprivadors = round(alocacaoprivadaB * retornoativoBprivadop * rendadisponivel,2) #Multiplicação da renda,alocação e retorno do ativo para saber o retorno em moeda do ativo B
    retornototalcarteiraprivadap = round((alocacaoprivadaA * retornoativoAprivadop) + (alocacaoprivadaB * retornoativoBprivadop), 4) #Retorno total da carteira privada em percentual, multiplicando alocação e retorno de um ativo mais a multiplicação do retorno e alocação do outro ativo
    retornototalprivadors = retornoativoAprivadors + retornoativoBprivadors #Retorno total em moeda, somando os retornos em moeda de cada ativo

    retornoativoApublicors = round(alocacaopublicaA * retornoativoApublicop * rendadisponivel,2) #Multiplicação da renda,alocação e retorno do ativo para saber o retorno em moeda do ativo A
    retornoativoBpublicors = round(alocacaopublicaB * retornoativoBpublicop * rendadisponivel,2) #Multiplicação da renda,alocação e retorno do ativo para saber o retorno em moeda do ativo B
    retornototalcarteirapublicop = round((alocacaopublicaA * retornoativoApublicop) + (alocacaopublicaB * retornoativoBpublicop), 4) #Retorno total da carteira pública em percentual, multiplicando alocação e retorno de um ativo mais a multiplicação do retorno e alocação do outro ativo
    retornototalpublicors = retornoativoApublicors + retornoativoBpublicors #Retorno total em moeda, somando os retornos em moeda de cada ativo

    retornoinvestimentosp = (retornototalcarteiraprivadap * 0.5) + (retornototalcarteirapublicop * 0.5) #Retorno percentual das duas carteiras
    retornoinvestimentosrs = retornototalprivadors + retornototalpublicors #Retorno em moeda das duas carteiras

    return rendadisponivel, retornoativoAprivadop, retornoativoBprivadop, retornoativoApublicop, retornoativoBpublicop, retornoativoAprivadors, retornoativoBprivadors, retornototalcarteiraprivadap, retornototalprivadors, retornoativoApublicors, retornoativoBpublicors, retornototalcarteirapublicop, retornototalpublicors, retornoinvestimentosp, retornoinvestimentosrs
    #Retornar variáveis

def printretornosecomparacoes():
    retornoslista = retornos()
    a = str(retornoslista[0])
    b = str(retornoslista[7]*100)#Multiplicar por 100 para aparecer em %
    c = str(retornoslista[8])
    d = str(retornoslista[11]*100)#Multiplicar por 100 para aparecer em %
    e = str(retornoslista[12])
    f = str(retornoslista[13])
    g = str(retornoslista[14])
    #Tive que colocar tudo em str porque por algum motivo desconhecido estava dando erro no tipo da variável, quando eu coloquei em str deu certo então sucesso ;)
    #Cada variável está salvando uma informação que será printada a seguir
    #A explicação do que está salvo em cada variável está nas strings que as variáveis estão juntas
    print("Renda disponível:",a,"em cada carteira")
    
    print("Retorno Percentual da Carteira Privada:",b,"%")
    
    print("Retorno em Moeda da Carteira Privada :R$",c)
    
    print("Retorno Percentual da Carteira Pública:",d,"%")
    
    print("Retorno em Moeda da Carteira Pública :R$",e)
    
    print("Retorno Percentual do Investimento nas Duas Carteiras:",f)
    
    print("Retorno em Moeda do Investimento nas Duas Carteiras: R$",g)
    print()
    ibov = indices.ibov()[2] - 1
    ifix = indices.ifix()[2] - 1
    cdi = indices.cdi()[2] - 1
    selic = indices.selic()[2] - 1
    ipca = indices.ipca()[2] - 1
    igpm = indices.igpm()[2] - 1
    #Puxar dados dos índices para serem comparados. Todos estão com - 1 porque os dados estão, por exemplo, 1.23 e para fazer a comparação eu preciso que esteja 0.23
    pcarteiratotal = retornoslista[13]
    #Puxar o retorno total do investimento para comparar com os índices de mercado
    if ibov > pcarteiratotal:
        print("Índice Ibovespa","(",ibov,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o Índice Ibovespa (",ibov,")")
    
    if ifix > pcarteiratotal:
        print("Índice IFIX","(",ifix,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o Índice IFIX (",ifix,")")

    if cdi > pcarteiratotal:
        print("CDI","(",cdi,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o CDI (",cdi,")")

    if selic > pcarteiratotal:
        print("Taxa Selic","(",selic,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o Taxa Selic (",selic,")")
    
    if ipca > pcarteiratotal:
        print("IPCA","(",ipca,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o IPCA (",ipca,")")

    if igpm > pcarteiratotal:
        print("IGPM","(",igpm,") maior que a carteira")
    else:
        print("Carteira montada(",pcarteiratotal,") com retorno maior que o IGPM (",igpm,")")
    #Condicionais testando se o retorno está maior que o índice, se estiver var printar que é maior, se não estiver vai printar que é menor que o índice

    x = 1
    y = f*x
    y1 = ibov*x
    y2 = ifix*x
    y3 = cdi*x
    y4 = selic*x
    y5 = ipca*x
    y6 = igpm*x
    #Definindo variáveis para serem utilizadas pelo gráfico

    categories = ['Carteira', 'Índice Ibovespa', 'Ifix', 'CDI', 'Taxa Selic', 'IPCA', 'IGPM']
    values = [str(y), str(y1), str(y2), str(y3), str(y4), str(y5), str(y6)]
    #Foi necessário transformar os valores em string porque o gráfico não estava aceitando o float.
    # Criando o gráfico
    plt.figure(figsize=(10, 6))#Definindo tamanho da figura
    plt.bar(categories, [float(value) for value in values], color='blue')  # Convertendo de volta para float antes de plotar através de um loop
    plt.xlabel('Variáveis')
    plt.ylabel('Valores')
    plt.title('Gráfico com as variáveis')
    #Nome de títulos e eixos
    plt.show() #Mostrar o gráfico



    

