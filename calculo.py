n4 = int(input('se sua empresa usa gasolina digite 1, se for diesel digite 2'))
n6 = int(input('quantos KM sua empresa roda no dia?'))
resto = int((n6*5)*53)* 0.82 * 0.75 * 3.7
resto1 = int((n6*5)*53)* 0.82 * 3.7
if n4 == 1:
   print('você emitiu',resto,'kg de carbono')
elif n4 == 2:
   print('você emitiu',resto,'kg de carbono')
else:
   print('erro de conexão tente masi tarde ...!')
  
dimi = float(input('digite quantos KG sua empresa diminuiu nesse ano :'))
n2 = int(dimi / 1000)
if dimi >= 1000:
  print('você recebeu:',n2,'creditos')
elif dimi < 1000:
    print('você não recebeu nenhum credito')
else:
    print('erro de conexão tente mais tarde...')
print('digite para qual moeda vc quer converter?')
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




  
