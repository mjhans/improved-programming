import requests

base_url = "https://dog.ceo/api"
breed_list_url = f"{base_url}/breeds/list/all" # 강아지품종의 모든 목록을 갖고 오는 주소
breed_images = {}

breed_list_response = requests.get(breed_list_url)
#print(breed_list_response)

if breed_list_response.status_code not in (400, 401, 404, 500):
    breed_list = breed_list_response.json().get("message", {}).keys()
    for breed_name in breed_list:
        breed_image_url = f"{base_url}/breed/{breed_name}/images"
        breed_image_response = requests.get(breed_image_url)
        
        if breed_image_response.status_code not in (400, 401, 404, 500):
            breed_image_list = breed_image_response.json().get("message", [])
            breed_images[breed_name] = breed_image_list
        else:
            print(f"request error : {breed_image_response.status_code}")


    # for breed in breed_list:
    #     print(f"breed_name: {breed}")
else:
    print(f"request error : {breed_list_response.status_code}")

for breed_name, image_urls in breed_images.items():
    print(f"{breed_name = }, {len(image_urls) = }")