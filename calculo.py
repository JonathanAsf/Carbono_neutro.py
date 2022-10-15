#Apresentação.

print('Descubra se sua empresa possui crédito resultante de baixa emissão de CO²')

#Cálculo de emissão

print('Escolha o combustível que sua empresa utiliza:')
print('Gasolina: Digite 1') 
print('Diesel: Digite 2')
combustivel = int(input()) 

#Caso outro valor seja inserido, esse condicional fechará o programa.

if combustivel != 1 and combustivel != 2:
  print('Opção indisponível, tente novamente.')
  quit()

#Fórmula para o cálculo e apresentação do resultado.

km = int(input('quantos KM sua empresa rodo no dia?'))
gasolina = int((km*5)*53)* 0.82 * 0.75 * 3.7 
diesel = int((km*5)*53)* 0.82 * 3.7
if combustivel == 1:
   print(f'sua empresa emitiu {gasolina:.2f}KG de carbono')
else:
   print(f'sua empresa emitiu {diesel:.2f} KG de carbono')

#Cálculo de gasto apenas utilizando energia elétrica.

contadeluz =  float(input("Quanto ficou a conta de luz da sua empresa"))
respostadaluz = float(contadeluz*0.092) 
porano = int(respostadaluz*(53*5))
print('Sua empresa emite',porano,'CO² anualmente')

#Cálculo baseado distancia percorrida

frete = int(input('Quantos fretes sua empresa faz ao mes'))
mediakm = int(input('Qual é a media da distancia do seus clientes'))
gasolina1 = int(frete*mediakm)* 0.82 * 0.75 * 3.7 
diesel1 = int(frete*mediakm)* 0.82 * 3.7
if combustivel == 1:
  print('sua empresa emitiu',gasolina1,'KG de CO²')
elif combustivel == 2:
  print('sua empresa emitiu',diesel1,'KG de CO²')
else:
  print('erro de conexão tente mais tarde ...!')

#Avaliação do crédito.

diminuição = float(input('digite quantos KG CO² sua empresa emitiu a menos nesse ano :'))
respostadimi = int(diminuição / 1000)
if diminuição >= 1000:
  print('Você recebeu:',respostadimi,'créditos')
elif diminuição < 1000:
    print('Você não recebeu nenhum crédito')
else:
    print('Erro de conexão tente mais tarde...')

      
#parte5
gasolinafinal = int(gasolina1 + gasolina + porano)
dieselfinal = int(diesel + diesel1 + porano)
if combustivel == 1:
   print('Por ano sua empresa gasta',gasolinafinal,'KG de CO²')
elif combustivel == 2:
  print('Por ano sua empresa gasta',dieselfinal,'KG de CO²')
else:
  print('Erro de conexão tente novamente mais tarde...!')

#parte 6
if respostadimi > 0:
   print('Para compensar a taxa de emissão, será necessário plpantar ',respostadimi*7,'árvores')
elif respostadimi == 0:
  print('A compensação está equivalente. Não será necessário plantar mais árvores.')
else:
  print('erro de conexão tente novamente mais tarde...!')

#parte 7
print("Você possui crédito, escolha a moeda que deseja obter a cotação")
conversão = int(input('Digite 1 para dolar, Digite 2 para euro, Digite 3 para real'))
if conversão == 1:
  n7 = float(respostadimi * 55.30)
  print('Convertendo para dolar você tera:',n7) 
elif conversão == 2:
  n7 = float(respostadimi * 57)
  print('Convertendo para euro você tera:',n7)
elif conversão == 3:
  n7 = float(respostadimi * 365)
  print('Convertendo para real você tera:',n7)
else:
  print('erro de conexão tente mais tarde...')
