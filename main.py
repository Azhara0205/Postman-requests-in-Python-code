import requests

url_1 = "https://catfact.ninja/fact"
url_2 = "https://catfact.ninja/facts"
url_3 = "https://catfact.ninja/breeds"
url_4 = "https://catfact.ninja/breeds?limit=2&page=2"
url_5 = "https://catfact.ninja/facts?max_length=30"

payload = {}
headers = {
  'Cookie': 'XSRF-TOKEN=eyJpdiI6IlZRUFhrS0YvZXRVeE4rcVN1MExYQ1E9PSIsInZhbHVlIjoiWXpvU2dxWWozM0RucVV3aFViYW96RUFZdlpXajhoTno3OElyQjc4T2EwZ242bUJqb2pDVkVNbkpIZUpuaFpkbkJtLy90TTJDb0FkWGt1clN1cjIvWXhEcFpQY2g1Z3V3UHc2ZXVjWlBrUGpTWk1DY3pVcy84MFhGd2RtN1pISHMiLCJtYWMiOiI5MTBiZTQxODc0ZWI0NDRjMWEwYWFkMTM0NTljODVlNWNlN2MwYjkxYzE1ZmI4ZTliNzM4Yzk4ZWIxMjYyZjlmIiwidGFnIjoiIn0%3D; catfacts_session=eyJpdiI6ImlibXYzeko3NnJYZ3BIQXNBcG44SFE9PSIsInZhbHVlIjoicW5rei85alllMzJRVnQ4TlVwZVdMZ0NoZWxMVzA1N0xSWE9Wc1FiN0VEU1U0SFBVVW5mL1JNdVBORXF5b25UeWE3WEE5MzNWZWpoSjVQZUUxdVZUc3BnSVUzakpBdDUxaExGN1FIVFVpL2M2bkZ4aFFJVTlUQ2tFZldsL1FST08iLCJtYWMiOiI4MzAyNDQyYWYwZDNlZWYyNWU3MDNlNDFkOGI1NmRlMTVkNTk5ZjEwMDRjOWExNjNlNGYzZjQ3MWRmMzRhMWYzIiwidGFnIjoiIn0%3D'
}

response_1 = requests.get(url_1, headers=headers, data=payload)
response_2 = requests.get(url_2, headers=headers, data=payload)
response_3 = requests.get(url_3, headers=headers, data=payload)
response_4 = requests.get(url_4, headers=headers, data=payload)
response_5 = requests.get(url_5, headers=headers, data=payload)

print("First request: ")
print(response_1.text)
print(response_1.status_code)

print("Second request: ")
print(response_2.text)
print(response_2.status_code)

print("Third request: ")
print(response_3.text)
print(response_3.status_code)

print("Fourth request: ")
print(response_4.text)
print(response_4.status_code)

print("Fifth request: ")
print(response_5.text)
print(response_5.status_code)

