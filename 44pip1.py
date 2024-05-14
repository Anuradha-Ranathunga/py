import requests

response = requests.get('https://corona.lmao.ninja/v2/continents?yesterday=true&sort=')
print(response)
content = response.json()

print(type(content))

#json is a dictionary. json=> javascript object notation
