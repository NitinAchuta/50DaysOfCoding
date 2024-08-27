import requests
import lxml
from bs4 import BeautifulSoup
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=header)
html = BeautifulSoup(response.text, "lxml")

heading = html.find("div", class_="a-section a-spacing-none aok-align-center aok-relative")
price = float(heading.text.split()[0][1:])
print(price)

if price < 20:
    print("Buy")
else:
    print("Don't buy!")
