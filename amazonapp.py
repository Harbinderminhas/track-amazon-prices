import time

import requests
from bs4 import BeautifulSoup
import smtplib



# URL is from amazon product that i chose
URL='https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_4?crid=1XRLJC9DPE8SM&keywords=sony+a7r&qid=1568299797&s=gateway&sprefix=sony+a7%2Caps%2C298&sr=8-4'




# from my user agent i got this header file-type this in google
headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title= soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    print("dd"+str(price))
    qq=str(price).split("\xa0")
    print(qq)
    qq2=str(qq[1]).replace(",","")
    converted_price=float(qq2)

    if(converted_price< 1.8000):
         send_mail()


    print(converted_price)

    print(title.strip())

    if(converted_price > 1.8000):
        send_mail()


def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('harbinderminhas92@gmail.com','harryminhas')

    subject='Price fell down!'
    body='check the amazon link https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_4?crid=1XRLJC9DPE8SM&keywords=sony+a7r&qid=1568299797&s=gateway&sprefix=sony+a7%2Caps%2C298&sr=8-4'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'harbinderminhas92@gmail.com',
        'harbinderminhas92@gmail.com',str(msg)
    )
    print('Hey Email Has BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60)





check_price()





