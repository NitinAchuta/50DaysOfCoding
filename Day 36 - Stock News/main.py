import requests
from datetime import date, timedelta
from newsapi import NewsApiClient
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

EMAIL = 'EMAIL HERE'
EMAIL_PASSKEY =  'EMAIL API PASSWORD HERE'

def enough_change(open_data, close_data):
    if 1 - (open_data / close_data) * 100 >= 5:
        return True
    elif 1 - (close_data / open_data) * 100 >= 5:
        return True

def send_mail():
    global STOCK, EMAIL, EMAIL_PASSKEY
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_key = "304fdd3282e9478ea40f1b4202cdf102"
    NewsApiClient.newsapi = NewsApiClient(api_key= news_key)
    news_parameters = {
        "apiKey": news_key,
        "q": "Tesla"
    }

    news_response = requests.get(url = "https://newsapi.org/v2/top-headlines", params=news_parameters)
    news = news_response.json()
    articles = news["articles"]
    content_list = []
    for i in range(3):
        content = f"TSLA: UP 5% \nHeadlines: {articles[i][f'title']}\nBrief: {articles[i][f'content']}"
        content_list.append(content)



    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    for content in content_list:
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = EMAIL, password = EMAIL_PASSKEY)
            connection.sendmail(from_addr=EMAIL, to_addrs="TO ADDRESS HERE", msg=f"Subject: {STOCK} Info For Today\n\n{content}") 

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_key = "ALPHAVANTAGE KEY"
second_alpha_key = "SECOND ALPHA VANTAGE KEY"
parameters = {
    "apikey": second_alpha_key,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY"
}
ticker_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
ticker_response.raise_for_status()
ticker_data = ticker_response.json()["Time Series (Daily)"]
# ticker_data = {'Meta Data':{'1. Information':'Daily Prices (open, high, low, close) and Volumes','2. Symbol':'TSLA','3. Last Refreshed':'2024-06-10','4. Output Size':'Compact','5. Time Zone':'US/Eastern'},'Time Series (Daily)':{'2024-06-10':{'1. open':'176.0600','2. high':'178.5700','3. low':'173.1700','4. close':'173.7900','5. volume':'50869682'},'2024-06-07':{'1. open':'176.1300','2. high':'179.3500','3. low':'175.5800','4. close':'177.4800','5. volume':'56244932'},'2024-06-06':{'1. open':'174.6000','2. high':'179.7300','3. low':'172.7300','4. close':'177.9400','5. volume':'69887024'},'2024-06-05':{'1. open':'175.3500','2. high':'176.1500','3. low':'172.1300','4. close':'175.0000','5. volume':'57953756'},'2024-06-04':{'1. open':'174.7750','2. high':'177.7550','3. low':'174.0000','4. close':'174.7700','5. volume':'60056340'},'2024-06-03':{'1. open':'17 8.1300','2. high':'182.6389','3. low':'174.4900','4. close':'176.2900','5. volume':'68568920'},'2024-05-31':{'1. open':'178.5000','2. high':'180.3200','3. low':'173.8200','4. close':'178.0800','5. volume':'67314602'},'2024-05-30':{'1. open':'178.5750','2. high':'182.6700','3. low':'175.3800','4. close':'178.7900','5. volume':'77784755'},'2024-05-29':{'1. open':'174.1900','2. high':'178.1500','3. low':'173.9300','4. close':'176.1900','5. volume':'54782649'},'2024-05-28':{'1. open':'176.4000','2. high':'178.2500','3. low':'173.1600','4. close':'176.7500','5. volume':'59736620'},'2024-05-24':{'1. open':'174.8350','2. high':'180.0800','3. low':'173.7300','4. close':'179.2400','5. volume':'65584478'},'2024-05-23':{'1. open':'181.8000','2. high':'181.9000','3. low':'173.2600','4. close':'173.7400','5. volume':'71975496'},'2024-05-22':{'1. open':'182.8500','2. high':'183.8000','3. low':'178.1200','4. close':'180.1100','5. volume':'88313477'},'2024-05-21':{'1. open':'175.5100','2. high':'186.8750','3. low':'174.7100','4. close':'186.6000','5. volume':'115266512'},'2024-05-20':{'1. open':'177.5600','2. high':'177.7540','3. low':'173.5200','4. close':'174.9500','5. volume':'61727425'},'2024-05-17':{'1. open':'173.5500','2. high':'179.6300','3. low':'172.7500','4. close':'177.4600','5. volume':'77445845'},'2024-05-16':{'1. open':'174.1000','2. high':'175.7900','3. low':'171.4300','4. close':'174.8400','5. volume':'59812220'},'2024-05-15':{'1. open':'179.9000','2. high':'180.0000','3. low':'173.1100','4. close':'173.9900','5. volume':'79662993'},'2024-05-14':{'1. open':'174.4959','2. high':'179.4900','3. low':'174.0700','4. close':'177.5500','5. volume':'86407422'},'2024- 05-13':{'1. open':'170.0000','2. high':'175.4000','3. low':'169.0000','4. close':'171.8900','5. volume':'67018903'},'2024-05-10':{'1. open':'173.0500','2. high':'173.0599','3. low':'167.7500','4. close':'168.4700','5. volume':'72627178'},'2024-05-09':{'1. open':'175.0100','2. high':'175.6200','3. low':'171.3700','4. close':'171.9700','5. volume':'65950292'},'2024-05-08':{'1. open':'171.5900','2. high':'176.0600','3. low':'170.1500','4. close':'174.7200','5. volume':'79969488'},'2024-05-07':{'1. open':'182.4000','2. high':'183.2600','3. low':'177.4000','4. close':'177.8100','5. volume':'75045854'},'2024-05-06':{'1. open':'183.8000','2. high':'187.5600','3. low':'182.2000','4. close':'184.7600','5. volume':'84390253'},'2024-05-03':{'1. open':'182.1000','2. high':'184.7800','3. low':'178.4200','4. close':'181.1900','5. volume':'75491539'},'2024-05-02':{'1. open':'182.8600','2. high':'184.6000','3. low':'176.0200','4. close':'180.0100','5. volume':'89148041'},'2024-05-01':{'1. open':'182.0000','2. high':'185.8600','3. low':'179.0100','4. close':'179.9900','5. volume':'92829719'},'2024-04-30':{'1. open':'186.9800','2. high':'190.9500','3. low':'182.8401','4. close':'183.2800','5. volume':'127031787'},'2024-04-29':{'1. open':'188.4200','2. high':'198.8700','3. low':'184.5400','4. close':'194.0500','5. volume':'243869678'},'2024-04-26':{'1. open':'168.8500','2. high':'172.1200','3. low':'166.3700','4. close':'168.2900','5. volume':'109815725'},'2024-04-25':{'1. open':'158.9600','2. high':'170.8800','3. low':'158.3600','4. close':'170.1800','5. volume':'126427521'},'2024-04-24':{'1. open':'162.8400','2. high':'167.9700','3. low':'157.5100','4. close':'162.1300','5. volume':'181178020'},'2024-04-23':{'1. open':'143.3300','2. high':'147.2600','3. low':'141.1100','4. close':'144.6800','5. volume':'124545104'},'2024-04-22':{'1. open':'140.5600','2. high':'144.4400','3. low':'138.8025','4. close':'142.0500','5. volume':'107097564'},'2024-04-19':{'1. open':'148.9700','2. high':'150.9400','3. low':'146.2200','4. close':'147.0500','5. volume':'87074500'},'2024-04-18':{'1. open':'151.2500','2. high':'152.2000','3. low':'148.7000','4. close':'149.9300','5. volume':'96098830'},'2024-04-17':{'1. open':'157.6400','2. high':'158.3300','3. low':'153.7800','4. close':'155.4500','5. volume':'82439718'},'2 024-04-16':{'1. open':'156.7420','2. high':'158.1900','3. low':'153.7500','4. close':'157.1100','5. volume':'96999956'},'2024-04-15':{'1. open':'170.2400','2. high':'170.6900','3. low':'161.3800','4. close':'161.4800','5. volume':'100245310'},'2024-04-12':{'1. open':'172.3400','2. high':'173.8099','3. low':'170.3644','4. close':'171.0500','5. volume':'64722669'},'2024-04-11':{'1. open':'172.5500','2. high':'175.8800','3. low':'168.5100','4. close':'174.6000','5. volume':'94515987'},'2024-04-10':{'1. open':'173.0400','2. high':'174.9300','3. low':'170.0100','4. close':'171.7600','5. volume':'84532407'},'2024-04-09':{'1. open':'172.9100','2. high':'179.2200','3. low':'171.9200','4. close':'176.8800','5. volume':'102327658'},'2024-04-08':{'1. open':'169.3400','2. high':'174.5000','3. low':'167.7900','4. close':'172.9800','5. volume':'1 04039371'},'2024-04-05':{'1. open':'169.0800','2. high':'170.8600','3. low':'160.5100','4. close':'164.9000','5. volume':'136439809'},'2024-04-04':{'1. open':'170.0700','2. high':'177.1900','3. low':'168.0100','4. close':'171.1100','5. volume':'122061224'},'2024-04-03':{'1. open':'164.0200','2. high':'168.8200','3. low':'163.2800','4. close':'168.3800','5. volume':'82223543'},'2024-04-02':{'1. open':'164.7500','2. high':'167.6900','3. low':'163.4300','4. close':'166.6300','5. volume':'115344925'},'2024-04-01':{'1. open':'176.1700','2. high':'176.7500','3. low':'170.2100','4. close':'175.2200','5. volume':'80751684'},'2024-03-28':{'1. open':'177.4500','2. high':'179.5700','3. low':'175.3000','4. close':'175.7900','5. volume':'77654838'},'2024-03-27':{'1. open':'181.4100','2. high':'181.9100','3. low':'176.0000','4. close':'179.8300','5. volume':'81804043'},'2024-03-26':{'1. open':'178.5800','2. high':'184.2500','3. low':'177.3800','4. close':'177.6700','5. volume':'113186227'},'2024-03-25':{'1. open':'168.7600','2. high':'175.2400','3. low':'168.7300','4. close':'172.6300','5. volume':'74228615'},'2024-03-22':{'1. open':'166.6900','2. high':'171.2000','3. low':'166.3000','4. close':'170.8300','5. volume':'75580637'},'2024-03-21':{'1. open':'176.3900','2. high':'178.1800','3. low':'171.8000','4. close':'172.8200','5. volume':'73178014'},'2024-03-20':{'1. open':'173.0000','2. high':'176.2500','3. low':'170.8200','4. close':'175.6600','5. volume':'83846726'},'2024-03-19':{'1. open':'172.3600','2. high':'172.8200','3. low':'167.4200','4. close':'171.3200','5. volume':'77271428'},'2024-03-18':{'1. open':'170.0200','2. high':'174.7200','3. low':'165.9000','4. close':'173.8000','5. volume':'108214358'},'2024-03-15':{'1. open':'163.1600','2. high':'165.1845','3. low':'160.7600','4. close':'163.5700','5. volume':'97146832'},'2024-03-14':{'1. open':'167.7700','2. high':'171.1700 ','3. low':'160.5100','4. close':'162.5000','5. volume':'125494925'},'2024-03-13':{'1. open':'173.0500','2. high':'176.0500','3. low':'169.1500','4. close':'169.4800','5. volume':'104717978'},'2024-03-12':{'1. open':'177.7700','2. high':'179.4300','3. low':'172.4101','4. close':'177.5400','5. volume':'87009098'},'2024-03-11':{'1. open':'175.4500','2. high':'182.8700','3. low':'174.8000','4. close':'177.7700','5. volume':'85013157'},'2024-03-08':{'1. open':'181.5000','2. high':'182.7300','3. low':'174.7000','4. close':'175.3400','5. volume':'85544644'},'2024-03-07':{'1. open':'174.3500','2. high':'180.0400','3. low':'173.7000','4. close':'178.6500','5. volume':'102129004'},'2024-03-06':{'1. open':'179.9900','2. high':'181.5760','3. low':'173.7000','4. close':'176.5400','5. volume':'107920944'},'2024-03-05':{'1. open':'183.0500','2. high':'184.5900','3. low':'177.5700','4. close':'180.7400','5. volume':'119660758'},'2024-03-04':{'1. open':'198.7300','2. high':'199.7500','3. low':'186.7200','4. close':'188.1400','5. volume':'134334869'},'2024-03-01':{'1. open':'200.5200','2. high':'204.5200','3. low':'198.5000','4. close':'202.6400','5. volume':'82243119'},'2024-02-29':{'1. open':'204.1800','2. high':'205.2800','3. low':'198.4463','4. close':'201.8800','5. volume':'85906974'},'2024-02-28':{'1. open':'200.4200','2. high':'205.3000','3. low':'198.4400','4. close':'202.0400','5. volume':'99806173'},'2024-02-27':{'1. open':'204.0400','2. high':'205.6000','3. low':'198.2600','4. close':'199.7300','5. volume':'108645412'},'2024-02-26':{'1. open':'192.2900','2. high':'201.7800','3. low':'192.0000','4. close':'199.4000','5. volume':'111747116'},'2024-02-23':{'1. open':'195.3100','2. high':'197.5700','3. low':'191.5000','4. close':'191.9700','5. volume':'78841917'},'2024-02-22':{'1. open':'194.0000','2. high':'198.3200','3. low':'191.3600','4. close':'197.4100','5. volume':'92739461'},'2024-02-21':{'1. open':'193.3600','2. high':'199.4400','3. low':'191.9500','4. close':'194.7700','5. volume':'103844008'},'2024-02-20':{'1. open':'196.1300','2. high':'198.6000','3. low':'189.1300','4. close':'193.7600','5. volume':'104545762'},'2024-02-16':{'1. open':'202.0600','2. high':'203.1700','3. low':'197.4000','4. close':'199.9500','5. volume':'111346705'},'2024-02-15':{'1. open':'189.1600','2. high':'200.8800','3. low':'188.8595','4. close':'200.4500','5. volume':'120831762'},'2024-02-14':{'1. open':'185.3000','2. high':'188.8900','3. low':'183.3500','4. close':'188.7100','5. volume':'81202987'},'2024-02-13':{'1. open':'183.9900','2. high':'187.2600','3. low':'182.1087','4. close':'184.0200','5. volume':'86759478'},'2024-02-12':{'1. open':'192.1100','2. high':'194.7300','3. low':'187.2800','4. close':'188.1300','5. volume':'95498597'},'2024-02-09':{'1. open':'190.1800','2. high':'194.1200','3. low':'189.4800','4. close':'193.5700','5. volume':'84476347'},'2024-02-08':{'1. open':'189.0000','2. high':'191.6171','3. low':'185.5800','4. close':'189.5600','5. volume':'83034043'},'2024-02-07':{'1. open':'188.1800','2. high':'189.7900','3. low':'182.6800','4. close':'187.5800','5. volume':'111535217'},'2024-02-06':{'1. open':'177.2100','2. high':'186.4900','3. low':'177.1100','4. close':'185.1000','5. volume':'122675954'},'2024-02-05':{'1. open':'184.2600','2. high':'184.6800','3. low':'175.0100','4. close':'181.0600','5. volume':'134294447'},'2024-02-02':{'1. open':'185.0400','2. high':'188.6900','3. low':'182.0000','4. close':'187.9100','5. volume':'110612672'},'2024-02-01':{'1. open':'188.5000','2. high':'189.8800','3. low':'184.2800','4. close':'188.8600','5. volume':'91843275'},'2024-01-31':{'1. open':'186.9950','2. high':'193.9700','3. low':'185.8459','4. close':'187.2900','5. volume':'103221430'},'2024-01-30':{'1. open':'195.3300','2. high':'196.3593 ','3. low':'190.6100','4. close':'191.5900','5. volume':'109982327'},'2024-01-29':{'1. open':'185.6300','2. high':'191.4800','3. low':'183.6700','4. close':'190.9300','5. volume':'125013148'},'2024-01-26':{'1. open':'185.5000','2. high':'186.7800','3. low':'182.1000','4. close':'183.2500','5. volume':'107343231'},'2024-01-25':{'1. open':'189.7000','2. high':'193.0000','3. low':'180.0600','4. close':'182.6300','5. volume':'198076787'},'2024-01-24':{'1. open':'211.8800','2. high':'212.7300','3. low':'206.7700','4. close':'207.8300','5. volume':'112930989'},'2024-01-23':{'1. open':'211.3000','2. high':'215.6500','3. low':'207.7516','4. close':'209.1400','5. volume':'106605946'},'2024-01-22':{'1. open':'212.2600','2. high':'217.8000','3. low':'206.2700','4. close':'208.8000','5. volume':'117952527'},'2024-01-19':{'1. open':'209.9900','2. high':'213.1900','3. low':'207.5600','4. close':'212.1900','5. volume':'102260343'},'2024-01-18':{'1. open':'216.8800','2. high':'217.4500','3. low':'208.7400','4. close':'211.8800','5. volume':'108595431'}}}

today = date.today()
yesterday = today - timedelta(days = 1)
two_days_ago = yesterday - timedelta(days = 1)
open_data = float(ticker_data[str(yesterday)]["1. open"])
close_data = float(ticker_data["2024-06-07"]["4. close"])

send_mail()

