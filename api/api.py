from flask import Flask, jsonify

  # Biblioteca de conversão de moedas
from forex_python.converter import CurrencyCodes, CurrencyRates
c = CurrencyRates()
cd = CurrencyCodes()

app = Flask(__name__)
  # Titulo do programa

@app.route('/cambio', methods=['POST'])

# Função para escolher o codigo da moeda
def valor(valor):
  while True:
      print ("CONVERSOR DE MOEDA")
      print (" Insira o valor desejado para cambiar\n- Insira a moeda inicial \n- Insira a moeda para cambio")
      valor = int(input('Insira o valor a ser convertido: '))
      return jsonify(valor)

# 2 Moeda inicial
def moeda_inicio():
              print('Selecione a moeda de inicio')
              cod_moeda_inicio = None 
              codigo = int(input("selecione uma das opções:  "))
              match codigo:
                  case 1:
                      cod_moeda_inicio = 'BRL'
                      print("cod de escolha:", cod_moeda_inicio)
                      return cod_moeda_inicio
                  case 2:
                      cod_moeda_inicio = 'USD'
                      print("cod de escolha:", cod_moeda_inicio)
                      return cod_moeda_inicio
                  case 3:
                      cod_moeda_inicio = 'EUR'
                      print("cod de escolha:", cod_moeda_inicio)
                      return cod_moeda_inicio
                  case 4:
                      cod_moeda_inicio = 'BTC'
                      print("cod de escolha:", cod_moeda_inicio)
                      return cod_moeda_inicio
                  case 5:
                      cod_moeda_inicio = 'ETH'
                      print("cod de escolha:", cod_moeda_inicio)
                      return cod_moeda_inicio
                  case _:
                      raise ValueError("Código inválido! Favor inserir dentre as opções fornecidas.")
          

# 3 Moeda de cambio
def moeda_cambio():
  print('Selecione a moeda para cambio')
  cod_moeda_cambio = None 
  codigo = int(input("selecione uma das opções:  "))
  match codigo:
      case 1:
          cod_moeda_cambio = 'BRL'
          print("cod de escolha:", cod_moeda_cambio)
          return cod_moeda_cambio
      case 2:
          cod_moeda_cambio = 'USD'
          print("cod de escolha:", cod_moeda_cambio)
          return cod_moeda_cambio
      case 3:
         cod_moeda_cambio = 'EUR'
         print("cod de escolha:", cod_moeda_cambio)
         return cod_moeda_cambio
      case 4:
          cod_moeda_cambio = 'BTC'
          print("cod de escolha:", cod_moeda_cambio)
          return cod_moeda_cambio
      case 5:
          cod_moeda_cambio = 'ETH'
          print("cod de escolha:", cod_moeda_cambio)
          return cod_moeda_cambio
      case _:
          raise ValueError("Código inválido! Favor inserir dentre as opções fornecidas.")
    

    # Informações do cambio 


def cambio(cod_moeda_inicial, moeda_inicial, resultado, cod_moeda_cambio, moeda_cambio):

  resultado = c.convert(cod_moeda_inicial, cod_moeda_cambio, moeda_inicial)
  simbolo_moeda = cd.get_symbol(cod_moeda_inicial)
  simbolo_moeda_cambio = cd.get_symbol(cod_moeda_cambio)
  resultado = round(resultado, 2)

  return jsonify(cod_moeda_inicial + str(moeda_inicial) + cod_moeda_cambio + str(resultado))

# rodar a API
app.run(host='0.0.0.0')