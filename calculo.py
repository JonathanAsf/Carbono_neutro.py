#Apresentação

print('\n Descubra quanto de CO² sua empresa emite anualmente \n')

#Cálculo de emissão

print('Escolha o combustível que sua empresa utiliza:')
print('Gasolina: Digite 1')
print('Diesel: Digite 2')
print('Alcool: Digite 3')
combustivel = int(input())

#Caso outro valor seja inserido, esse condicional fechará o programa

if combustivel != 1 and combustivel != 2 and combustivel !=3:
  print('Opção indisponível, tente novamente.')
  quit()

#Fórmula para o cálculo e apresentação do resultado

km = int(input('Quantos KM sua empresa roda por dia?\n'))
gasolina = int(((km*5)*53)* 0.82 * 0.75 * 3.7) #Fórmula para CO² em Kg emitido uusando gasolina
diesel = int(((km*5)*53)* 0.82 * 3.7) #Fórmula para CO² em Kg emitido usando diesel
alcool = int(((km*5)*53)*2.716) #Fórmula para Co² em Kg emitido usando etanol

if combustivel == 1:
   print(f'Sua empresa emitiu por ano {gasolina:.2f} KG de carbono')
elif combustivel == 2:
   print(f'Sua empresa emitiu por ano {alcool:.2f} KG de carbono')
elif combustivel == 3:
    print(f'Sua empresa emitiu por ano {diesel:.2f} KG de carbono')

#Cálculo baseado distancia percorrida

frete = int(input('Quantos fretes sua empresa faz ao mês?\n'))
mediakm = int(input('Qual é a média da distância(km) do seus clientes?\n'))
distgaso = int((frete*mediakm)* 0.82 * 0.75 * 3.7)
distdisel = int((frete*mediakm)* 0.82 * 3.7)
distalco = int((frete*mediakm)*2.716)

if combustivel == 1:
  print(f'Sua empresa emite:{distgaso:.2f} KG de CO² por mês')
elif distgaso == 2:
  print(f'Sua empresa emite:{distdisel:.2f} KG de CO² por mês')
elif combustivel == 3:
  print(f'Sua empresa emite:{distalco:.2f} KG de CO² por mês')
else:
  print('Erro de conexão tente mais tarde ...!')

#Cálculo de uso de combustível total
gasolinafinal = int(distgaso) #Fórmula para gasolina gasta ao ano
dieselfinal = int(diesel + distdisel) #Fórmula para diesel gasto ao ano
alcoolfinal = int(alcool + distalco) #Fórmula para alcool gasto ao ano
 
if combustivel == 1:
   print(f'Sua empresa emite: {gasolinafinal} KG de CO² por ano\n')
elif combustivel == 2:
   print(f'Sua empresa emite: {dieselfinal} KG de CO² por ano\n')
elif combustivel == 3:
   print(f'Sua empresa emite: {alcoolfinal} KG de CO² por ano\n')
else:
   print('Erro de conexão tente novamente mais tarde...!')


#Avaliação do crédito
#Necessário reformular essa parte do código
if combustivel == 1:
  emgasol = int(gasolinafinal/1000) #Emissão de carbono utilizando gasolina
  print(f'')
elif combustivel == 2:
  emdie = int(dieselfinal/1000) #Emissão de carbono utilizando diesel
  print(f'')
elif combustivel == 3:
  emalco = int(alcoolfinal/1000) #Emissão de carbono utilizando alcool
  print(f'')
else:
  print('Erro de conexão tente mais tarde...')

#Constatação da equivalência 
#Caso não haja equivalência, será feito um cálculo visando alcança-la

if combustivel ==1:
    print('Para compensar a taxa de emissão de CO², será necessário plantar ',emgasol,'árvores\n')
elif combustivel ==2:
    print('Para compensar a taxa de emissão de CO², será necessário plantar ',emdie*7,'árvores\n')
elif combustivel ==3:
    print('Para compensar a taxa de emissão de CO², será necessário plantar ',emalco*7,'árvores\n')

elif combustivel ==1:
    print('A compensação está equivalente. Não será necessário plantar mais árvores.\n')
elif combustivel ==2:
    print('A compensação está equivalente. Não será necessário plantar mais árvores.\n')
elif combustivel ==3:
    print('A compensação está equivalente. Não será necessário plantar mais árvores.\n')
else:
  print('Erro de conexão tente novamente mais tarde...!')

#Conversão para moedas

#Gasolina
if  combustivel == 1:
    credito = float(emgasol * 55.30)
    print('Convertendo para dolar você terá: U$',credito)

    credito = float(emgasol * 57)
    print('Convertendo para euro você terá:',credito)

elif combustivel == 1:
    credito = float(emgasol* 365)
    print('Convertendo para real você terá:',credito)

#Diesel
elif combustivel == 2:
    credito = float(emdie * 55.30)
    print('Convertendo para dolar você terá: U$',credito)

    credito = float(emdie * 57)
    print('Convertendo para euro você terá: U$',credito)

    credito = float(emdie* 365)
    print('Convertendo para real você terá: U$',credito)

#Álcool
elif combustivel == 3:
    credito = float(emalco*55.30)
    print('Convertendo para dolar você terá: U$', credito)

    credito = float(emalco * 57)
    print('Convertendo para euro você terá: ', credito)

    credito = float(emalco * 365)
    print('Convertendo para real você terá:',credito)
