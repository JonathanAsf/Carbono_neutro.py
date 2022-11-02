#Apresentação

print('\nDescubra quanto de CO² sua empresa emite anualmente \n')
print('Caso haja diminuição de emissão de CO² entre os anos, você terá créditos disponíveis \n')

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

#Cálculo de emissão mensal baseado na distância média percorrida | ano passado |

freteantigo = int(input('Qual era a média mensal de fretes da sua empresa no ano passado?\n'))
mediakmantigo = int(input('Qual era a distância(km) média dos seus clientes?\n'))

#Gasto de combustível mensal do ano passado
distgasoantigo = int((freteantigo*mediakmantigo)* 0.82 * 0.75 * 3.7) 
distdiselantigo = int((freteantigo*mediakmantigo)* 0.82 * 3.7) 
distalcoantigo = int((freteantigo*mediakmantigo)*2.716) 

if combustivel == 1:
  print(f'Sua empresa emite:{distgasoantigo:.2f} KG de CO² por mês no ano passado')
elif combustivel == 2:
  print(f'Sua empresa emite:{distdiselantigo:.2f} KG de CO² por mês ano passado')
elif combustivel == 3:
  print(f'Sua empresa emite:{distalcoantigo:.2f} KG de CO² por mês ano passado')
else:
  print('Erro de conexão tente mais tarde ...!')

#Cálculo de emissão de carbono anual | ano passado |

#Gasto de combustível anual do ano passado
kmantigo = int(input('Qual era a média de km rodados por dia no ano passado?\n'))
gasolinaantigo = int(((kmantigo*5)*53)* 0.82 * 0.75 * 3.7) #Fórmula para CO² em Kg emitido usando gasolina no ultimo ano
dieselantigo = int(((kmantigo*5)*53)* 0.82 * 3.7) #Fórmula para CO² em Kg emitido usando diesel no ultimo ano
alcoolantigo = int(((kmantigo*5)*53)*2.716) #Fórmula para Co² em Kg emitido usando etanol no ultimo ano

if combustivel == 1:
   print(f'Sua empresa emitiu por ano {gasolinaantigo:.2f} KG de carbono')
elif combustivel == 2:
   print(f'Sua empresa emitiu por ano {alcoolantigo:.2f} KG de carbono')
elif combustivel == 3:
    print(f'Sua empresa emitiu por ano {dieselantigo:.2f} KG de carbono')

#álculo de emissão mensal baseado na distância média percorrida | ano atual |

freteatual = int(input('Quantos fretes sua empresa faz ao mês (atualmente) ?\n'))
mediakmatual = int(input('Qual é a média da distância(km) do seus clientes?\n'))

#Gasto de combustível mensal do ano passado
distgasoatual = int((freteatual*mediakmatual)* 0.82 * 0.75 * 3.7)
distdiselatual = int((freteatual*mediakmatual)* 0.82 * 3.7)
distalcoatual = int((freteatual*mediakmatual)*2.716)

if combustivel == 1:
  print(f'Sua empresa emite:{distgasoatual:.2f} KG de CO² por mês')
elif combustivel == 2:
  print(f'Sua empresa emite:{distdiselatual:.2f} KG de CO² por mês')
elif combustivel == 3:
  print(f'Sua empresa emite:{distalcoatual:.2f} KG de CO² por mês')
else:
  print('Erro de conexão tente mais tarde ...!')

#Cálculo de emissão de carbono anual | ano atual |

#Gasto de combustível anual do ano atual
kmatual = int(input('Quantos KM sua empresa roda em média por dia atualmente?\n'))
gasolinaatual = int(((kmatual*5)*53)* 0.82 * 0.75 * 3.7) #Fórmula para CO² em Kg emitido usando gasolina no atual ano
dieselatual = int(((kmatual*5)*53)* 0.82 * 3.7) #Fórmula para CO² em Kg emitido usando diesel no atual ano
alcoolatual = int(((kmatual*5)*53)*2.716) #Fórmula para Co² em Kg emitido usando etanol no atual ano

if combustivel == 1:
   print(f'Sua empresa emitiu por ano {gasolinaatual:.2f} KG de carbono')
elif combustivel == 2:
   print(f'Sua empresa emitiu por ano {alcoolatual:.2f} KG de carbono')
elif combustivel == 3:
    print(f'Sua empresa emitiu por ano {dieselatual:.2f} KG de carbono')

#Avaliação do crédito

if combustivel == 1:
   if gasolinaatual > gasolinaantigo:
    print('Você não possuí crédito')
    print('Não houve diminuição de gás carbono em relação ao ano passado')

elif combustivel == 2:
   print(f'Sua empresa emitiu por ano {alcoolatual:.2f} KG de carbono')
   if dieselatual > dieselantigo:
    print('Você não possuí crédito')
    print('Não houve diminuição de gás carbono em relação ao ano passado')
elif combustivel == 3: 
   if alcoolatual > alcoolantigo:
     print('Você não possuí crédito')
     print('Não houve diminuição de gás carbono em relação ao ano passado')


emgasol =  (gasolinaantigo - gasolinaatual)/1000
emdie = (dieselantigo - dieselatual)/1000
emalco = (alcoolantigo - alcoolatual)/1000

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
