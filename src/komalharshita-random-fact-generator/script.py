import requests
import json

def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    data = json.loads(response.text)  
    fact = data['text']        
    return fact

print("---Welcome to my random fact generator---\n")

print("Enter a number: ")
n = int(input())

if n > 7:
    print("Maximum number of facts per execution is 7")
elif n <= 0:
    print("Minimum number of facts per execution is 1")
else:
    for i in range(n):
        print(get_fact())
        print()
