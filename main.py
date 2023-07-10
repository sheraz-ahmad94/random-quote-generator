import requests
import json

def generate_quote():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Key": "1f92897968msh477a7d353e8ce6cp1328ebjsnda4a5da58125",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def format_data(data):
    quote = data["content"]
    by = data["originator"]["name"]
    print(f"Quote: {quote}")
    print(f"By: {by}")

print("-" * 25)
print("Random Quote of the Day")
print("-" * 25)
data = generate_quote()
format_data(data)


