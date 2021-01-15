# Импорт библиотеки requests
import requests
# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/astros.json")
# Вывод кода
print(response.status_code)
# Вывод ответа, полученного от сервера API
print(response.json())
