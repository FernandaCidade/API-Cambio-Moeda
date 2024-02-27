
import requests

# Realizar conexão
# Pegar o valor a ser convertido
# Resposta do servidor e exibir 



# Realizando conexão com url
def conexao():
    url = "http://127.0.0.1:8000/moeda"
    response = requests.get(url)
    data = response.json()

    return data['rates']


# Realizando a conversão da moeda

def conversao_moeda(moeda_origem,moeda_convertida, taxa, moedas):
    # realizar a verificação da taxa a ser aplicada
         
         match moedas:
            case "USD":
                taxa = 4
                moeda_convertida = moeda_origem * taxa
                return moeda_convertida
            case "ETH":
                taxa = 15
                moeda_convertida = moeda_origem * taxa
                return moeda_convertida
            case "BTC":
                taxa = 19
                moeda_convertida = moeda_origem * taxa
                return moeda_convertida
            case "BRL":
                taxa = 19
                moeda_convertida = moeda_origem * taxa
                return moeda_convertida
            case "EUR":
                taxa = 20
                moeda_convertida = moeda_origem * taxa
                return moeda_convertida
             
            case default:
                return None
             
cambio = conexao()
moedas = input("Qual valor da conversão: ").upper()

moeda_convertida = conversao_moeda(moeda_origem,moeda_convertida, taxa, moedas)

if moeda_convertida is not None:
    print(f'\n{moeda_convertida:.2f}')