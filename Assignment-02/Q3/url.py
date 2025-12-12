import requests

url="https://fakestoreapi.com/products"
response=requests.get(url)
print("status code:",response.status_code)
data=response.json()
print("resp data:",data) 