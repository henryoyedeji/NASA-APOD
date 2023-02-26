import requests


def get_content():
    url = "https://api.nasa.gov/planetary/apod?api_key=O6Dw0wFVEAskcybu1ZY0zkvl74zTmMtqZlACEWwo"
    request = requests.get(url)
    content = request.json()
    # Get image
    img_url = content['hdurl']
    image = requests.get(img_url)
    # Save image to file
    with open("image.png", mode="wb") as img:
        img.write(image.content)
    return content
