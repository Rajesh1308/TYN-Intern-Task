import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/company/red-hat/"

payload = {}
headers = {
  'Cookie': 'bcookie="v=2&8b4b2349-daa4-4fcd-8d33-584886a8f213"; lang=v=2&lang=en-us; lidc="b=TGST07:s=T:r=T:a=T:p=T:g=2898:u=1:x=1:i=1721905811:t=1721992211:v=2:sig=AQH0JtWxb69wmed_b3xUpuIXGJ8ixCX8"; JSESSIONID=ajax:6196000457702636803; bscookie="v=1&2024072511101168460af6-f2fe-44f8-8c81-83565938ef51AQHXkbpL7_2FHdv0-PGoDOZ4-yt056Dc"',
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.text:
    soup = BeautifulSoup(response.content, 'html.parser')

    #p_tag = soup.find('p', class_='break-words whitespace-pre-wrap text-color-text')
    p_tag = soup.find('p', attrs={"class": "break-words whitespace-pre-wrap text-color-text"})

    
    print(p_tag.text)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
