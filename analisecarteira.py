import numpy as np
import pandas as pd
import statistics
import ativos as at
from indices import cdi




def escolha_dos_ativos_privados():
    AGRU11 = at.AGRU11_Conc_do_Aerop_Inter_de_Guarulhos_SA_Emis_01Ser01()[3] 
    VALE38 = at.VALE38_Vale_Emis_08_Ser_03()[3]
    CDBINTER = at.CDB_LIQUIDEZ_DIÁRIA_BANCO_INTER_102_DO_CDI()[3]
    MATD11 = at.MATD11_Mater_Dei_Emis_01_Ser_uni()[3]
    AEGP19 = at.AEGP19_Aegea_Saneamento_e_Part_S_A_Emis_09_Ser_uni()[3]
    lista = [AGRU11, VALE38, CDBINTER, MATD11, AEGP19]
    # Vai pegar todos os coeficientes de variação das funções de cada ativo
    menor = min(lista) #Pegar o menor valor de CV
    listacresceste = sorted(lista)
    segundomenor = listacresceste[1]
    # Para pegar o segundo menor valor, coloquei a lista em ordem crescente e peguei o segundo número da lista
    resultados_priv = menor, segundomenor #Resultados salvos em uma variável
    dicionario = {AGRU11: "AGRU11",
             VALE38: "VALE38",
             CDBINTER: "CDBINTER",
             MATD11: "MATD11",
             AEGP19: "AEGP19"
             }
    # Salvar em um dicionário os valores que significam uma string, que será utilizada para printar na função de montagem de carteiras
    primeiro_ativo_priv = dicionario[menor]
    segundo_ativo_priv = dicionario[segundomenor]
    # Vai pegar os nomes de cada ativo escolhido
    dicionario2 = {AGRU11: at.AGRU11_Conc_do_Aerop_Inter_de_Guarulhos_SA_Emis_01Ser01(),
             VALE38: at.VALE38_Vale_Emis_08_Ser_03(),
             CDBINTER: at.CDB_LIQUIDEZ_DIÁRIA_BANCO_INTER_102_DO_CDI(),
             MATD11: at.MATD11_Mater_Dei_Emis_01_Ser_uni(),
             AEGP19: at.AEGP19_Aegea_Saneamento_e_Part_S_A_Emis_09_Ser_uni()
             }
    #Esse dicionário foi para pegar todos os dados dos ativos escolhidos como media e desvio padrão para realizar outros cálculos, como o sharpe
    mediaA = dicionario2[menor][0]
    despadA = dicionario2[menor][1]
    rentanualA = dicionario2[menor][2]
    mediaB = dicionario2[segundomenor][0]
    despadB = dicionario2[segundomenor][1]
    rentanualB = dicionario2[segundomenor][2]
    colunaA = dicionario2[menor][4]
    colunaB = dicionario2[segundomenor][4]
    #Aqui foi para pegar cada dado que eu ia usar dos ativos escolhidos
    return mediaA, despadA, rentanualA, mediaB, despadB, rentanualB, primeiro_ativo_priv, segundo_ativo_priv, resultados_priv, colunaA, colunaB
    #Retornando as variáveis para serem utilizados em outras funções


def sharpe_privado():
    retorno_ativo1 = escolha_dos_ativos_privados()[0]  # Função que puxa o retorno médio do ativo A
    retorno_ativo2 = escolha_dos_ativos_privados()[3] # Função que puxa o retorno médio do ativo B
    taxa_livre_risco = cdi()[0]  #Taxa livre de risco pode ser algum índice "livre de risco" como CDI ou TAXA SELIC
    alocacoes = np.arange(0, 1.02, 0.02) #Definindo a variável alocações(um intervalo) entre 0 a 1 de 0.02 em 0.02 como foi instruído pelo exemplo de fronteira eficiente que foi passado para a gente
    desvio_padrao_ativo1 = escolha_dos_ativos_privados()[1] # Função que puxa o desviopadrão do ativo A
    desvio_padrao_ativo2 = escolha_dos_ativos_privados()[4] # Função que puxa o desviopadrão do ativo A
    coluna1 = escolha_dos_ativos_privados()[9] 
    coluna2 = escolha_dos_ativos_privados()[10]
    #Aqui vai pegar todos os dados de rentabilidade média diária de cada
    varianciaA = desvio_padrao_ativo1**2 #Calculando a variancia de cada ativo que é elevar o desvio padrão ao quadrado
    varianciaB = desvio_padrao_ativo2**2 #Calculando a variancia de cada ativo que é elevar o desvio padrão ao quadrado
    melhor_alocacao = 0 #Criando uma variável que será a melhor alocação, após o loop irá salvar a melhor alocação
    melhor_sharpe = -float('inf') # Criando um variável com valor negativo infinito para que no loop de cálculo do sharpe qualquer valor será maior, assim salvando na variável
    for alocacao in alocacoes: #Criando um loop para calcular para cada alocação um sharpe
        retorno_carteira = alocacao * retorno_ativo1 + (1 - alocacao) * retorno_ativo2
        covariancia = desvio_padrao_ativo1 * desvio_padrao_ativo2 * np.corrcoef(coluna1[:len(coluna2)], coluna2)[0, 1]
        variancia = alocacao**2 * varianciaA + (1 - alocacao)**2 * varianciaB + 2 * alocacao * (1-alocacao) * covariancia
        desvio_padrao_carteira = variancia**0.5
        #Essas fórmulas foram passadas para a gente nas monitorias, são fórmulas que calculam desvio padrão e média da carteira com dois ativos e duas ponderações(alocações)
        sharpe = (retorno_carteira - taxa_livre_risco) / desvio_padrao_carteira
        #Fórmula de sharpe
        if sharpe > melhor_sharpe:
            melhor_sharpe = sharpe
            melhor_alocacao = alocacao
        #Dentro do loop, para cada sharpe calculado se for maior que o sharpe anterior vai ser salvos nas variáveis a melhor alocação com o maior sharpe
    alocacaoprivado = melhor_alocacao
    sharpeprivado = melhor_sharpe
    return sharpeprivado, alocacaoprivado
    #Retornando as variáveis para serem utilizados em outras funções

def escolha_dos_ativos_publicos():
    #Essa função é a mesma da escolha de ativos privados, apenas muda o nome das variáveis e os ativos puxados
    NTN_F = at.NTN_F_Tesouro_Prefixado_com_Juros_Semestrais_2027_BRSTNCNTF1P8()[3]
    LTF_2026 = at.LTF_Tesouro_SELIC_2026_BRSTNCLF1RE0()[3]
    LTF_2027 = at.LTF_Tesouro_Selic_2027_BRSTNCLF1RH3()[3]
    NTN_B = at.NTN_B_Tesouro_IPCA_mais_com_Juros_RSTNCNTB4U6()[3]
    NTN_C = at.NTN_C_Tesouro_IGPM_2031_BRSTNCNTC0K4()[3]
    lista = [NTN_F, LTF_2026, LTF_2027, NTN_B, NTN_C]
    menor = min(lista)
    listacresceste = sorted(lista)
    segundomenor = listacresceste[1]
    resultados = menor, segundomenor
    dicionario = {NTN_F: "Tesouro Prefixado com Juros Semestrais 2027",
             LTF_2026: "Tesouro Selic 2026",
             LTF_2027: "Tesouro Selic 2027",
             NTN_B: "Tesouro IPCA+ com juros",
             NTN_C: "Tesouro IGPM 2031"
             }
    primeiro_ativo = dicionario[menor]
    segundo_ativo = dicionario[segundomenor]
    dicionario2 = {NTN_F: at.NTN_F_Tesouro_Prefixado_com_Juros_Semestrais_2027_BRSTNCNTF1P8(),
             LTF_2026: at.LTF_Tesouro_SELIC_2026_BRSTNCLF1RE0(),
             LTF_2027: at.LTF_Tesouro_Selic_2027_BRSTNCLF1RH3(),
             NTN_B: at.NTN_B_Tesouro_IPCA_mais_com_Juros_RSTNCNTB4U6(),
             NTN_C: at.NTN_C_Tesouro_IGPM_2031_BRSTNCNTC0K4()
             }
    mediaA = dicionario2[menor][0]
    despadA = dicionario2[menor][1]
    rentanualA = dicionario2[menor][2]
    mediaB = dicionario2[segundomenor][0]
    despadB = dicionario2[segundomenor][1]
    rentanualB = dicionario2[segundomenor][2]
    colunaA = dicionario2[menor][4]
    colunaB = dicionario2[segundomenor][4]
    return mediaA, despadA, rentanualA, mediaB, despadB, rentanualB, primeiro_ativo, segundo_ativo, resultados, colunaA, colunaB


def sharpe_publico():
    #Essa função é a mesma da sharpe privado, apenas muda o nome das variáveis e os ativos puxados
    retorno_ativo1 = escolha_dos_ativos_publicos()[0]  # Substitua pelo retorno médio do primeiro ativo
    retorno_ativo2 = escolha_dos_ativos_publicos()[3] # Substitua pelo retorno médio do segundo ativo
    taxa_livre_risco = cdi()[0]  # Substitua pela taxa livre de risco 0.000465503460602376
    alocacoes = np.arange(0, 1.00, 0.02)
    desvio_padrao_ativo1 = escolha_dos_ativos_publicos()[1] # Substitua pelo desvio padrão do primeiro ativo
    desvio_padrao_ativo2 = escolha_dos_ativos_publicos()[4] # Substitua pelo desvio padrão do segundo ativo
    coluna1 = escolha_dos_ativos_privados()[9]
    coluna2 = escolha_dos_ativos_privados()[10]
    varianciaA = desvio_padrao_ativo1**2
    varianciaB = desvio_padrao_ativo2**2
    melhor_alocacao = 0
    melhor_sharpe = -float('inf')
    for alocacao in alocacoes:
        retorno_carteira = alocacao * retorno_ativo1 + (1 - alocacao) * retorno_ativo2
        covariancia = desvio_padrao_ativo1 * desvio_padrao_ativo2 * np.corrcoef(coluna1[:len(coluna2)], coluna2)[0, 1]
        variancia = alocacao**2 * varianciaA + (1 - alocacao)**2 * varianciaB + 2 * alocacao * (1-alocacao) * covariancia
        desvio_padrao_carteira = variancia**0.5
        sharpe = (retorno_carteira - taxa_livre_risco) / desvio_padrao_carteira
        if sharpe > melhor_sharpe:
            melhor_sharpe = sharpe
            melhor_alocacao = alocacao
    alocacaopublica = melhor_alocacao
    sharpepublico = melhor_sharpe
    return sharpepublico, alocacaopublica


def printcarteiras(): #Função para dar o print com boa estética das carteiras
    listapublicos = escolha_dos_ativos_publicos()
    sharpepublico = sharpe_publico()
    #Puxando as funções e criando uma lista com os valores retornados em cada uma
    O = listapublicos[6] #Nome do Ativo A
    P = listapublicos[7] #Nome do Ativo B
    Q = listapublicos[8] #Coeficientes de variação
    R = sharpepublico[0] #Índice de sharpe da carteira
    S = (sharpepublico[1]) * 100 #Alocação de A
    Ss = (sharpepublico[1]) #Tive que fazer essa variável sem o '* 100' para conseguir o complemento da alocação, sem isso não estava dando o resultado correto
    U = round((1 - Ss) * 100, 1) #Alocação de B
    #Variáveis criadas para puxar um elemento da lista. 
    print()
    print(" CARTEIRA PÚBLICA ")
    print("Os resultados do coeficiente de variação maximizados dos ativos A e do B foram, respectivamente, ",Q[0], "e", Q[1] )
    print("Ativo A da carteira Pública : ",O, " com ",S,"%","alocado ")
    print("Ativo B da carteira Pública : ",P, " com ",U,"%","alocado ")
    print("Essa carteira possui um índice de Sharpe de: ", R)
    #Print Carteira Pública
    listaprivados = escolha_dos_ativos_privados()
    sharpeprivado = sharpe_privado()
    #Puxando as funções e criando uma lista com os valores retornados em cada uma
    O1 = listaprivados[6] #Nome do Ativo A
    P1 = listaprivados[7] #Nome do Ativo B
    Q1 = listaprivados[8] #Coeficientes de variação
    R1 = sharpeprivado[0] #Índice de sharpe da carteira
    S1 = (sharpeprivado[1]) * 100 #Alocação de A
    Ss1 = (sharpeprivado[1]) #Tive que fazer essa variável sem o '* 100' para conseguir o complemento da alocação, sem isso não estava dando o resultado correto
    U1 = round((1 - Ss1) * 100, 1) ##Alocação de B
    print()
    print(" CARTEIRA PRIVADA ")
    print("Os resultados do coeficiente de variação maximizados dos ativos A e do B foram, respectivamente, ",Q1[0], "e", Q1[1] )
    print("Ativo A da carteira Privada : ",O1, " com ",S1,"%","alocado ")
    print("Ativo B da carteira Privada : ",P1, " com ",U1,"%","alocado ")
    print("Essa carteira possui um índice de Sharpe de: ", R1)
    #Print Carteira Privada

