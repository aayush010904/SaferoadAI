import requests
from Image2Url import image_to_data_url

# API endpoint
API_URL = "https://realtimechatapp-18ss.onrender.com/api/messages/send/USER_ID"

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2N2U0NGY2YmNlMjhjNTk5NTU4OTUwN2IiLCJpYXQiOjE3NDMwMTU3ODcsImV4cCI6MTc0MzYyMDU4N30.PNeekg_Ki3Y1bKgtdPL_G6ZVJq5MxkrzQJyBGuGw7Ac"
# Authentication headers
HEADERS = {
    "Content-Type": "application/json"
}

COOKIES = {
    "jwt": TOKEN
}

RECIEVER_ID = "67d427151a03794271c0e3d2"

def send_message(text, image_path=None):
    url = API_URL.replace("USER_ID", RECIEVER_ID)

    if image_path:
        image_url = image_to_data_url(image_path)

    payload = {
        "text": text,
        "image": image_url
    }

    response = requests.post(url, json=payload, headers=HEADERS, cookies=COOKIES)

    print("\n🔍 Debugging API Response:")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)  # Print raw response before parsing

    try:
        response_json = response.json()  # Try parsing JSON
        print("✅ Parsed JSON Response:", response_json)
    except requests.exceptions.JSONDecodeError:
        print("❌ Error: Response is not valid JSON!")

# # Example call
# send_message("Hello, this is an accident and the victim is: ", "./avatar.png")
