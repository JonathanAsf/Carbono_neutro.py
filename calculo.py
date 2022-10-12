parte 1

n4 = int(input('se sua empresa usa gasolina digite 1, se for diesel digite 2'))
n6 = int(input('quantos KM sua empresa rodo no dia?'))
resto = int((n6*5)*53)* 0.82 * 0.75 * 3.7 
resto1 = int((n6*5)*53)* 0.82 * 3.7
if n4 == 1:
   print('sua empresa emitiu',resto,'kg de carbono')
elif n4 == 2:
   print('sua empresa emitiu',resto1,'kg de carbono')
else:
   print('erro de conexão tente masi tarde ...!')

parte2











parte3
n3 = int(input('quantos fretes sua empresa faz ao mes'))
n2 = int(input('qual é a media da distancia do seus clientes'))
resto3 = int(n3*n2)* 0.82 * 0.75 * 3.7 
resto4 = nt(n3*n2)* 0.82 * 3.7
if n4 == 1:
  print('sua empresa emitiu',resto3,'KG de carbono')
elif n4 == 2:
  print('sua empresa emitiu',resto4,'KG de carbono')
else:
  print('erro de conexão tente masi tarde ...!')


parte4

dimi = float(input('digite quantos KG sua empresa diminuiu nesse ano :'))
n2 = int(dimi / 1000)
if dimi >= 1000:
  print('você recebeu:',n2,'creditos')
elif dimi < 1000:
    print('você não resebeu nenhum credito')
else:
    print('erro de conexão tente mais tarde...')
print('digite para qual moeda vc quer converter?')



parte5,0

resto5 = int(resto3+resto)
resto6 = int(resto2+resto1)
if n4 == 1:
   print('por ano sua empresa gasta',resto5,'KG de CO2')
elif n4 == 2:
  print('por ano sua empresa gasta',resto6,'KG de CO2')

parte 5.1

if n2 > 0:
   print('conpensando vc tera que plantar',n2*7,'arvore')
elif n2 == 0:
  print('conpensando foi abaixo de 1 o precissa plantar nenhuma arvore')
else:
  print('erro de conexão tente novamente mais tarde...!')








parte 6

n5 = int(input('para dolar digite 1,para euro digite 2,para real digite 3?'))
if n5 == 1:
  n7 = float(n2 * 55.30)
  print('convertendo para dolar você tera:',n7) 
elif n5 == 2:
  n7 = float(n2 * 57)
  print('convertendo para euro você tera:',n7)
elif n5 == 3:
  n7 = float(n2 * 365)
  print('convertendo para real você tera:',n7)
else:
  print('erro de conexão tente mais tarde...')




  
