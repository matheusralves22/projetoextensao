import pandas as pd
import statistics
import numpy as np
#ESSE ARQUIVO VAI PEGAR AS INFORMAÇÕES DO EXCEL DE TODOS OS ATIVOS
#Irei comentar apenas uma porque os comandos são repetidos, muda apenas o nome do arquivo em que se pega os dados e o nome da função
def NTN_F_Tesouro_Prefixado_com_Juros_Semestrais_2027_BRSTNCNTF1P8():
    abrir_arquivo = 'basededados1.xlsx' #Vai abrir o arquivo excel
    publico = pd.read_excel(abrir_arquivo) #Com uma função do pandas vai ler o arquivo aberto
    coluna1 = publico['Rent DI NTN-F Tesouro Prefixado com Juros Semestrais 2027 - BRSTNCNTF1P8'].astype(float) #Essa função vai pegar os dados de rentabilidade diária do ativo, colocar em uma lsita e transformar em float
    media_DI = statistics.mean(coluna1) #Calcular a média
    despad_DI = statistics.stdev(coluna1) #calcular o desvio padrão
    coluna2 = publico['Rent DI NTN-F Tesouro Prefixado com Juros Semestrais 2027 - BRSTNCNTF1P8 + 1'].astype(float) #Vai pegar os dados de rentabilidade diária, so que adicionados + 1 para fazer um cálculo, teve que fazer isso porque para calcular a rentabilidade anual a função do python não conseguia multiplicar muitos valores próximos de 0
    rentanual = np.prod(coluna2) #Calcular rentabilidade anual
    coeficiente_variacao = despad_DI/media_DI #Calcular o coeficiente de variação de cada ativo
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
    #retornar valores que serão utilizados
#NTN_F_Tesouro_Prefixado_com_Juros_Semestrais_2027_BRSTNCNTF1P8() , está como comentário porque tive que conferir se todos os dados estavam batendo, depois que conferi coloquei como comentário

def LTF_Tesouro_SELIC_2026_BRSTNCLF1RE0():
    abrir_arquivo = 'basededados1.xlsx'
    publico = pd.read_excel(abrir_arquivo)
    coluna1 = publico['Rent DI LTF Tesouro SELIC 2026 - BRSTNCLF1RE0'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = publico['Rent DI LTF Tesouro SELIC 2026 - BRSTNCLF1RE0 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#LTF_Tesouro_SELIC_2026_BRSTNCLF1RE0()

def LTF_Tesouro_Selic_2027_BRSTNCLF1RH3():
    abrir_arquivo = 'basededados1.xlsx'
    publico = pd.read_excel(abrir_arquivo)
    coluna1 = publico['Rent DI LTF Tesouro Selic 2027 - BRSTNCLF1RH3'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = publico['Rent DI LTF Tesouro Selic 2027 - BRSTNCLF1RH3 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#LTF_Tesouro_Selic_2027_BRSTNCLF1RH3()

def NTN_B_Tesouro_IPCA_mais_com_Juros_RSTNCNTB4U6():
    abrir_arquivo = 'basededados1.xlsx'
    publico = pd.read_excel(abrir_arquivo)
    coluna1 = publico['Rent DI NTN-B Tesouro IPCA+ com Juros - RSTNCNTB4U6'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = publico['Rent DI NTN-B Tesouro IPCA+ com Juros - RSTNCNTB4U6 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#NTN_B_Tesouro_IPCA_mais_com_Juros_RSTNCNTB4U6()

def NTN_C_Tesouro_IGPM_2031_BRSTNCNTC0K4():
    abrir_arquivo = 'basededados1.xlsx'
    publico = pd.read_excel(abrir_arquivo)
    coluna1 = publico['Rent DI NTN-C Tesouro IGPM 2031 - BRSTNCNTC0K4'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = publico['Rent DI NTN-C Tesouro IGPM 2031 - BRSTNCNTC0K4 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#NTN_C_Tesouro_IGPM_2031_BRSTNCNTC0K4()

def AGRU11_Conc_do_Aerop_Inter_de_Guarulhos_SA_Emis_01Ser01():
    abrir_arquivo = 'basededados1.xlsx'
    privado = pd.read_excel(abrir_arquivo)
    coluna1 = privado['Rent DI AGRU11 - Conc do Aerop Inter de Guarulhos S/A Emis 01/Ser 01'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = privado['Rent DI AGRU11 - Conc do Aerop Inter de Guarulhos S/A Emis 01/Ser 01 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#AGRU11_Conc_do_Aerop_Inter_de_Guarulhos_SA_Emis_01Ser01()

def VALE38_Vale_Emis_08_Ser_03():
    abrir_arquivo = 'basededados1.xlsx'
    privado = pd.read_excel(abrir_arquivo)
    coluna1 = privado['Rent DI VALE38 - Vale Emis 08/Ser 03'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = privado['Rent DI VALE38 - Vale Emis 08/Ser 03 + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#VALE38_Vale_Emis_08_Ser_03()

def CDB_LIQUIDEZ_DIÁRIA_BANCO_INTER_102_DO_CDI():
    abrir_arquivo = 'basededados1.xlsx'
    privado = pd.read_excel(abrir_arquivo)
    coluna1 = privado['Rent DI CDB LIQUIDEZ DIÁRIA BANCO INTER 102% DO CDI'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = privado['Rent DI CDB LIQUIDEZ DIÁRIA BANCO INTER 102% DO CDI + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#CDB_LIQUIDEZ_DIÁRIA_BANCO_INTER_102_DO_CDI()

def MATD11_Mater_Dei_Emis_01_Ser_uni():
    abrir_arquivo = 'basededados4.xlsx'
    privado = pd.read_excel(abrir_arquivo)
    coluna1 = privado['Rent DI - MATD11 - Mater Dei Emis 01/Ser uni'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = privado['Rent DI - MATD11 - Mater Dei Emis 01/Ser uni + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#MATD11_Mater_Dei_Emis_01_Ser_uni()

def AEGP19_Aegea_Saneamento_e_Part_S_A_Emis_09_Ser_uni():
    abrir_arquivo = 'basededados5.xlsx'
    privado = pd.read_excel(abrir_arquivo)
    coluna1 = privado['AEGP19 - Aegea Saneamento e Part S/A Emis 09/Ser uni'].astype(float)
    media_DI = statistics.mean(coluna1)
    despad_DI = statistics.stdev(coluna1)
    coluna2 = privado['AEGP19 - Aegea Saneamento e Part S/A Emis 09/Ser uni + 1'].astype(float)
    rentanual = np.prod(coluna2)
    coeficiente_variacao = despad_DI/media_DI
    return media_DI, despad_DI, rentanual, coeficiente_variacao, coluna1
#AEGP19_Aegea_Saneamento_e_Part_S_A_Emis_09_Ser_uni()

