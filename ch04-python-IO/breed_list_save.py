import requests
import sys
from urllib.parse import urlparse


save_names = []
if len(sys.argv)  >= 2:
    save_names = sys.argv[1].lower().split(",")
else:
    save_names = ["shiba", "cattledog", "australian"]


def http_response(api_url, method = "GET"):
    if method == "GET":
        return http_get_response_to_json(api_url)
    else:
        pass

def http_get_response_to_json(api_url):
    resp = http_get_response(api_url)
    return  resp.json() if resp is not None else None

def http_get_response(api_url):
    resp = requests.get(api_url)
    return  resp if (resp.status_code in [200]) else None

def download(api_url, file_path, file_name):
    resp = http_get_response(api_url)
    if resp is None:
        return None
    with open(f"{file_path}/{file_name}", "wb") as f:
        f.write(resp.content)

base_url = "https://dog.ceo/api"
breed_list_url = f"{base_url}/breeds/list/all" # 강아지품종의 모든 목록을 갖고 오는 주소
breed_images = {}

breed_resp_json = http_response(breed_list_url)

breed_names = [] if (resp := http_response(breed_list_url)) is None \
    else resp.get("message", {}).keys()

breed_image_urls = [\
    (breed_name, f"{base_url}/breed/{breed_name}/images") \
    for breed_name in breed_names \
            ]
for breed_name, breed_image_url in breed_image_urls:
    breed_img_resp_json = http_response(breed_image_url)
    if breed_img_resp_json is None:
        print("error")
        break
    else:
        breed_image_list = breed_img_resp_json.get("message",[])
        #print(breed_image_list)
        breed_images[breed_name] = breed_image_list


# for breed_name, image_urls in breed_images.items():
#     print(f"{breed_name = }, {len(image_urls) = }")

for save_name in save_names:
    for image_url in breed_image.get(save_name, []):
        file_name = urlparse(image_url).path.split("/")[-1]
        download(image_url,".", f"{save_name}-{file_name}")