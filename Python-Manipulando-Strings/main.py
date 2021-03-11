from ExtratorArgumentosUrl import ExtratorArgumentosUrl
url =" https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)
# Aqui ta tudo bem, teste agora o caso em que “moedaorigem=moedadestino".
url ="https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)