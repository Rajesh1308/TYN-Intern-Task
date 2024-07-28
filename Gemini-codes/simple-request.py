api_key = "AIzaSyDAPdxupuluPC08adxzayOmM86AyrCUbWY"

import google.generativeai as genai
#import PIL.Image
import os

genai.configure(api_key=api_key)
#img = PIL.Image.open('path/to/image.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config={"response_mime_type": "application/json"})
response = model.generate_content(["Give me a short details about tcs company in 50 words separately, the company specialization in 3 or 4 words, country (headquaters), website, and linkedin url"])

file = open("aiResponse.txt", "w")
file.write(response.text)
file.close()

print(response.text)