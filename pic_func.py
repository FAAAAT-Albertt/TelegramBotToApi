import requests


TOKEN = ""




def pic():
    url = "https://api.segmind.com/v1/kandinsky2.2-txt2img"
    api_key = "SG_8f017c0a04694ff1"

    value_promt = get_promt()

    # Request payload
    data = {
    "prompt": value_promt[0],
    "negative_prompt": "lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands",
    "samples": 1,
    "num_inference_steps": 25,
    "img_width": 1024,
    "img_height": 1024,
    "prior_steps": 25,
    "seed": 9863172,
    "base64": False
    }
    response = requests.post(url, json=data, headers={'x-api-key': api_key})

    if response.status_code == 200:
        filename = "image.jpg"
        with open(filename, "wb") as file:
            file.write(response.content)

        url_photo = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

        files = {'photo': open("image.jpg", 'rb')}
        data = {'chat_id': value_promt[1]}

        response = requests.post(url_photo, files=files, data=data)
    else:
        text = "Ошибка при получении картинки. Код ошибки: "
        url_photo = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={value_promt[1]}&text={text}{response.status_code}"
        source = requests.get(url_photo)


def get_promt():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
    response = requests.get(url)
    data = response.json()
    pass
    promt = data['result'][0]['message']['text']
    user_id = data['result'][0]['message']['chat']['id']
    return promt, user_id



if __name__ == '__main__':
    pic()