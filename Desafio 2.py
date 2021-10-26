variavel_couro = float(input('Qual é o preço dos Couros?'))
variavel_Solado= float(input('Qual é o preço dos Solados?'))
variavel_Cordoes_Ilhoses = float(input('Qual é o preço dos Cordões e dos Ilhoses?'))
variavel_Insumos = float(input('Qual é o preço dos Insumos?'))
variavel_Maoobra = float(input('Qual é o preço da Mão de Obra?'))
variavel_Marketing = float(input('Qual é o preço do Marketing?'))
variavel_vendas = float(input('Qual é o preço dos custos das Vendas?' ))

#CUSTO DA MERCADORIA VENDIDA CMV
CMV = (variavel_couro*0.30) + (variavel_Solado*0.20) + (variavel_Cordoes_Ilhoses*0.05) + (variavel_Insumos*0.05) + (variavel_Maoobra*0.20) + (variavel_Marketing*0.10) + (variavel_vendas*0.10)
print("O preço de custo unitário deste modelo de sapato é R$: ",round(CMV,2))

#CUSTO FINAL COM O LUCRO INCLUSO
Lucro = CMV * 1.30

#PERDAS DE CAPITAL
Perdas = Lucro * 1.15

#IMPOSTOS FEDERAIS
IPI_PIS_COFINS = Perdas * 1.15

#MARGEM DE VENDAS
Vendas = IPI_PIS_COFINS * 1.25

#IMPOSTOS FEDERAIS E ESTADUAIS
ICMS_INSS = Vendas * 1.30

#PREÇO FINAL + IMPOSTOS + MARGEM DE LUCRO
Precofim = ICMS_INSS
print("O valor do Preço Final + Impostos + Margem de lucro repassado ao consumidor final deste modelo de sapato é R$: ",round(Precofim, 2 ))




