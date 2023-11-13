import pandas as pd
import statistics
import numpy as np
#ESSE ARQUIVO VAI PEGAR AS INFORMAÇÕES DO EXCEL DE TODOS OS ATIVOS
#Irei comentar apenas uma porque os comandos são repetidos, muda apenas o nome do arquivo em que se pega os dados e o nome da função

def cdi():
    abrir_arquivo = 'basededados1.xlsx' #Vai abrir o arquivo excel
    cdi = pd.read_excel(abrir_arquivo) #Com uma função do pandas vai ler o arquivo aberto
    coluna1 = cdi['Rent DI CDI'].astype(float) #Pegar os dados e transformar em float e coloca-los em uma lista
    media_DI_CDI = statistics.mean(coluna1) # Média diária do índice
    despad_DI_CDI = statistics.stdev(coluna1) # Desvio padrão do índice
    coluna2 = cdi['Rent DI CDI + 1'].astype(float) #Vai pegar os dados diários, so que adicionados + 1 para fazer um cálculo, teve que fazer isso porque para calcular o índice anual a função do python não conseguia multiplicar muitos valores próximos de 0
    anual_CDI = np.prod(coluna2) #Cálcular o acumulado anual do índice
    return media_DI_CDI, despad_DI_CDI, anual_CDI
    #Retornar variáveis
#cdi(), está como comentário porque tive que conferir se todos os dados estavam batendo, depois que conferi coloquei como comentário

def selic():
    abrir_arquivo = 'basededados1.xlsx'
    selic = pd.read_excel(abrir_arquivo)
    coluna1 = selic['Rent Selic DI'].astype(float)
    media_DI_selic = statistics.mean(coluna1)
    despad_DI_selic = statistics.stdev(coluna1)
    coluna2 = selic['Rent Selic DI + 1'].astype(float)
    anual_selic = np.prod(coluna2)
    
    return media_DI_selic, despad_DI_selic, anual_selic
#selic()
    
def ifix():
    abrir_arquivo = 'basededados2.xlsx'
    ifix = pd.read_excel(abrir_arquivo)
    coluna1 = ifix['IFIX - Rent DI'].astype(float)
    media_DI_ifix = statistics.mean(coluna1)
    despad_DI_ifix = statistics.stdev(coluna1)
    coluna2 = ifix['IFIX - Rent DI + 1'].astype(float)
    anual_ifix = np.prod(coluna2)
    
    return media_DI_ifix, despad_DI_ifix, anual_ifix
#ifix()

def ibov():
    abrir_arquivo = 'basededados2.xlsx'
    ibov = pd.read_excel(abrir_arquivo)
    coluna1 = ibov['Rent DI IBOV'].astype(float)
    media_DI_ibov = statistics.mean(coluna1)
    despad_DI_ibov = statistics.stdev(coluna1)
    coluna2 = ibov['Rent DI IBOV + 1'].astype(float)
    anual_ibov = np.prod(coluna2)
    
    return media_DI_ibov, despad_DI_ibov, anual_ibov
#ibov()

def ipca():
    abrir_arquivo = 'basededados3.xlsx'
    ipca = pd.read_excel(abrir_arquivo)
    coluna1 = ipca['RENT IPCA MENSAL'].astype(float)
    media_m_ipca = statistics.mean(coluna1)
    despad_m_ipca = statistics.stdev(coluna1)
    coluna2 = ipca['RENT IPCA MENSAL + 1']
    anual_ipca = np.prod(coluna2)
    
    return media_m_ipca, despad_m_ipca, anual_ipca
#ipca()

def igpm():
    abrir_arquivo = 'basededados3.xlsx'
    igpm = pd.read_excel(abrir_arquivo)
    coluna1 = igpm['RENT IGPM MENSAL'].astype(float)
    media_m_igpm = statistics.mean(coluna1)
    despad_m_igpm = statistics.stdev(coluna1)
    coluna2 = igpm['RENT IGPM MENSAL + 1']
    anual_igpm = np.prod(coluna2)
    
    return media_m_igpm, despad_m_igpm, anual_igpm
#igpm()

