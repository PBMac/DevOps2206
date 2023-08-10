import requests

try:
    response = requests.get("fkdamflmdsalfmslamflkdmaflkdsmfamlk")
except requests.exceptions.MissingSchema as e:
    print("invalid scheme")