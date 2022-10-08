import requests,json

# result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = json.loads(result.text)
# print (result[0]['title'])

# ----------------------- Exchange Api ile Döviz Uygulaması -----------------------

# api_url = "https://api.exchangeratesapi.io/v1/latest?apikey=39B0bZXNV04in8jpaMMVXpB1a4Hc6WaV base="
bozulan_doviz = input("Bozduracağınız Döviz Tipini Giriniz: ")
alinan_doviz = input("Alacağınız Döviz Tipini Giriniz: ")
miktar = int(input(f"Ne Kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))
# result = requests.get(api_url+bozulan_doviz)
# result = json.loads(result.text)

# print(result)

import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to={alinan_doviz}&from={bozulan_doviz}&amount={miktar}"

payload = {}
headers= {
  "apikey": "39B0bZXNV04in8jpaMMVXpB1a4Hc6WaV"
}

response = requests.request("GET", url, headers=headers, data = payload)

result = response.text
print (result)