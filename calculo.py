#parte 1

combustivel = int(input('Se sua empresa usa gasolina digite 1, se for diesel digite 2\n'))
km = int(input('Quantos KM sua empresa rodo no dia? \n'))
resto = int((km*5)*53)* 0.82 * 0.75 * 3.7 
resto1 = int((km*5)*53)* 0.82 * 3.7
if combustivel == 1:
   print('Sua empresa emitiu:\n',resto,'kg de carbono')
elif combustivel == 2:
   print('Sua empresa emitiu: ',resto1,'kg de carbono')
else:
   print('Erro de conexão tente mais tarde ...!')

#parte2

#parte3
frete = int(input('Quantos fretes sua empresa faz ao mês? '))
distanciaMedia = int(input('Qual é a media da distancia do seus clientes? '))
resto3 = int(frete*distanciaMedia)* 0.82 * 0.75 * 3.7 
resto4 = (frete*distanciaMedia)* 0.82 * 3.7
if combustivel == 1:
  print('Sua empresa emitiu',resto3,'KG de carbono ')
elif combustivel == 2:
  print('Sua empresa emitiu',resto4,'KG de carbono ')
else:
  print('Erro de conexão tente mais tarde ...!'')

#parte4

diminuicao = float(input('Digite quantos KG sua empresa diminuiu nesse ano:\n '))
distanciaMedia = int(diminuicao / 1000)
if diminuicao >= 1000:
  print('Você recebeu:',distanciaMedia,'creditos ')
elif diminuicao < 1000:
    print('Você não recebeu nenhum credito ')
else:
    print('Erro de conexão tente mais tarde... ')
print('digite para qual moeda vc quer converter? ')

#parte5
resto5 = int(resto3+resto)
resto6 = int(resto2+resto1)
if combustivel == 1:
   print('Por ano sua empresa gasta',resto5,'KG de CO2 ')
elif combustivel == 2:
  print('Por ano sua empresa gasta',resto6,'KG de CO2 ')

#parte 5.1
if distanciaMedia > 0:
   print('Compensando vc tera que plantar',distanciaMedia*7,'arvores')
elif distanciaMedia == 0:
  print('Compensando foi abaixo de 1 o precissa plantar nenhuma arvores')
else:
  print('Erro de conexão tente novamente mais tarde...!')

#parte 6
moeda = int(input('para dolar digite 1,para euro digite 2,para real digite 3?'))
if moeda == 1:
  n7 = float(distanciaMedia * 55.30)
  print('Convertendo para dolar você tera:\n','US$',n7) 
elif moeda == 2:
  n7 = float(distanciaMedia * 57)
  print('Convertendo para euro você tera:\n','Є',n7)
elif moeda == 3:
  n7 = float(distanciaMedia * 365)
  print('Convertendo para real você tera:\n','R$',n7)
else:
  print('Erro de conexão tente mais tarde...\n')
