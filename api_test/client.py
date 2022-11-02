import requests
import json
url = 'http://localhost:5000/personas'
data = requests.get(url)
if data.status_code == 200:
   data = data.json()
else:
   print("error")
   exit(1)

for person in data:
   print(f'''La persona {person["nombres"]} {person["apellido_paterno"]} {person["apellido_materno"]}
tiene id: {person["id"]} y correo: {person["email"]}''')


