import requests
import base64

print("""\t \t \t Coded By NikolaT3sla #https://twitter.com/Nikola_T3sla """)

TEXT = input("Text to convert it to mp3 : ")
output = input("Name of The mp3 file : ")
url = "https://cxl-services.appspot.com/proxy?url=https://texttospeech.googleapis.com/v1beta1/text:synthesize&token=03AGdBq24eevW6MGj4eG6_fs4n57wCcXO4xau7brfj5wQn9lXvJbK3UaB_dpf1tfb2jkGbEKWYStuZkbddn22u6q0lBn0g_LQltr9ZqNPsX-HW4K9MZa-oR8kCgZzaagK8gwkOr3ISi1Y3z1Q36-TpuNpAvjYgQhldcepm3RXAEv7I6KjR0L9LHoR8jh5vvGyp9Oy5zNLCmZget2Ix60kQZdSaATtOfptH5ecDBxkSjCYiMTGZgOyEjEzGtctvKPjfnk3D3eiqHfA2lTojYwRUIWLfCJ8DT1wRwgEY7ExDOfzJCauREL-mEDMOtHDqr4IAuCAu_t8Rl6jg3crihoAUJ5o30FtHm66ycVSUjD1RD8SKryqUsOwi3Qtc0rSTei5RbmkEkqvtSZUiZenluAnp-sgn8VbcMtxFZgwCHCxWc2Bi36aBuH5whGOt0bxY-zwLhT8pTtxbkuTZ"

payload="{\r\n    \"input\": {\r\n        \"text\": \" " + TEXT + "\"\r\n    },\r\n    \"voice\": {\r\n        \"languageCode\": \"en-US\",\r\n        \"name\": \"en-US-Wavenet-D\"\r\n    },\r\n    \"audioConfig\": {\r\n        \"audioEncoding\": \"LINEAR16\",\r\n        \"pitch\": 0,\r\n        \"speakingRate\": 1\r\n    }\r\n}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
data = response.json()
token = data['audioContent']
mp3_bytes = token.encode('utf-8')
with open (output+'.mp3', 'wb') as file_to_save:
	decoded = base64.decodebytes(mp3_bytes)
	file_to_save.write(decoded)
