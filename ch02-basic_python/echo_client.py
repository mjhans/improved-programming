import requests

response = requests.get("https://www.bible.ac.kr/")

d_result = response.json()
#print(type(d_result))
result = f"""{d_result["method"]}
"""

print(result)
print(response.status_code)

if response.status_code != 200:
    raise Exception()