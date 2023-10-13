import requests

list_url = "https://dog.ceo/api/breeds/list/all"
res = requests.get(list_url)


if res.status_code in [200, 201]:
    temp = res.json()
    dog_list = temp.get('message', {}).keys()
    print(dog_list)
    for category in dog_list:
        resp_images = requests.get(f"https://dog.ceo/api/breed/{category}/images")
        if resp_images.status_code == 200:
            l = resp_images.json()["message"]
        print(l)
else:
    print(res.status_code)
    print("실패")