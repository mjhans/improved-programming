import requests



def http_response(api_url, method = "GET"):
    if method == "GET":
        return http_get_response(api_url)
    else:
        pass

def http_get_response(api_url):
    resp = requests.get(api_url)
    return  resp.json() if (resp.status_code in [200]) else None

    # return_value = None
    # if resp.status_code not in(400, 401):
    #     return_value = resp.json()
    # else:
    #     return_value = None
    # return return_value


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


for breed_name, image_urls in breed_images.items():
    print(f"{breed_name = }, {len(image_urls) = }")

# for breed_name in breed_names:
#     breed_image_url = f"{base_url}/breed/{breed_name}/images"
    
#     #print(breed_image_url)
#     breed_img_resp_json = http_response(breed_image_url)
#     if breed_img_resp_json is None:
#         print("error")
#         break
#     else:
#         breed_image_list = breed_img_resp_json.get("message",[])
#         #print(breed_image_list)
#         breed_images[breed_name] = breed_image_list

# for breed_name, image_urls in breed_images.items():
#     print(f"{breed_name = }, {len(image_urls) = }")