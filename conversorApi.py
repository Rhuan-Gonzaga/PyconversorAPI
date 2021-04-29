import requests
import json

request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
rq = json.loads(request.text)
value = rq['USDBRL']['high']


real = float(input("How much money do you have in your wallet?R$ "))
dollar = float(value)

print("With R${:.2f} you can buy US${:.2f}".format(real, real*dollar))

