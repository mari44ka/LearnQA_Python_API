import requests
response = requests.get("https://playground.learnqa.ru/api/long_redirect")
response_history = response.history
print(response_history)
print(response.history[0].url)
print(response.history[1].url)
print(response.history[2].url)
