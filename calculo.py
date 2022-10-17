#Apresentação
print('Descubra se sua empresa possui crédito resultante de baixa emissão de CO²')

#Cálculo de emissão

print('Escolha o combustível que sua empresa utiliza:')
print('Gasolina: Digite 1') 
print('Diesel: Digite 2')
combustivel = int(input()) 

#Caso outro valor seja inserido, esse condicional fechará o programa

if combustivel != 1 and combustivel != 2:
  print('Opção indisponível, tente novamente.')
  quit()

#Fórmula para o cálculo e apresentação do resultado

km = int(input('Quantos KM sua empresa roda por dia?\n'))
gasolina = int(((km*5)*53)* 0.82 * 0.75 * 3.7) #Fórmula para CO² em Kg emitido usando gasolina
diesel = int(((km*5)*53)* 0.82 * 3.7) #Fórmula para CO² em Kg emitido usando diesel

if combustivel == 1:
   print(f'Sua empresa emitiu {gasolina:.2f}KG de carbono')
else:
   print(f'Sua empresa emitiu {diesel:.2f} KG de carbono')

#Cálculo de gasto apenas utilizando energia elétrica

contadeluz =  float(input("Qual é o valor médio da conta de luz da sua empresa?\n"))
respostadaluz = float(contadeluz*0.092) 
porano = int(respostadaluz*(53*5))
print(f'Sua empresa emite {porano:.2f}CO² anualmente')

#Cálculo baseado distancia percorrida

frete = int(input('Quantos fretes sua empresa faz ao mês?\n'))
mediakm = int(input('Qual é a média da distância do seus clientes?\n'))
gasolina1 = int((frete*mediakm)* 0.82 * 0.75 * 3.7) 
diesel1 = int((frete*mediakm)* 0.82 * 3.7)

if combustivel == 1:
  print(f'Sua empresa emitiu: {gasolina1:.2f}KG de CO²')
elif combustivel == 2:
  print(f'Sua empresa emitiu: {diesel1:.2f}KG de CO²')
else:
  print('Erro de conexão tente mais tarde ...!')

#Avaliação do crédito

diminuição = float(input('Quantos KG CO² sua empresa emitiu a menos nesse ano? \n'))
respostadimi = int(diminuição / 1000)
if diminuição >= 1000:
  print(f'Você recebeu: {respostadimi:.2f} créditos\n')
elif diminuição < 1000:
    print('Você não possui crédito disponível\n')
else:
    print('Erro de conexão tente mais tarde...')


#Cálculo de uso de combustível total
gasolinafinal = int(gasolina1 + gasolina + porano) #Fórmula para gasolina gasta ao ano
dieselfinal = int(diesel + diesel1 + porano) #Fórmula para diesel gasto ao ano
if combustivel == 1:
   print(f'Por ano sua empresa gasta: {gasolinafinal:.2f}KG de CO²\n')
elif combustivel == 2:
  print(f'Por ano sua empresa gasta?: {dieselfinal:.2f}KG de CO²\n')
else:
  print('Erro de conexão tente novamente mais tarde...!')

#Diminuição de Co²
if respostadimi > 0:
   print(f'Para compensar a taxa de emissão de CO², será necessário plantar {respostadimi*7} árvores\n')
elif respostadimi == 0:
  print('A compensação está equivalente. Não será necessário plantar mais árvores.\n')
else:
  print('Erro de conexão tente novamente mais tarde...!')

#Conversão papa moedas
print("Escolha uma moeda para converter o crédito existente")
print('Dólar: Digite 1') 
print('Euro: Digite 2')
print('Real: Digite 3')

conversão = int(input(''))

if conversão == 1:
  n7 = float(respostadimi * 55.30)
  print(f'Convertendo para dolar você terá: US${n7} disponíveis em crétido') 
elif conversão == 2:
  n7 = float(respostadimi * 57)
  print(f'Convertendo para euro você terá: €{n7} disponíveis em crétido')
elif conversão == 3:
  n7 = float(respostadimi * 365)
  print(f'Convertendo para real você terá: R${n7} disponíveis em crétido')
else:
  print('Erro de conexão tente mais tarde...')
2
