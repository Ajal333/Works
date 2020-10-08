import requests
from bs4 import BeautifulSoup
import smtplib

URL = "Url to the product link go here"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    # Find your User Agent by just googling my user agent and copy paste it here
}


def sendMail():
    print("Sending mail....")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("your mail", "password")

    subject = "Price fall, Hurry up!"

    body = f"Check the product ASAP: {URL}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("from mail", "to mail", msg)

    print("MAIL HAS BEEN SENT!")

    server.quit()


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = (
        soup.find(id="priceblock_ourprice")
        .get_text()
        .replace("\xa0", "")
        .replace(",", "")
    )

    convertedPrice = float(price[1:])

    print(title.strip())

    print(convertedPrice)

    if convertedPrice < 1500:
        sendMail()


checkPrice()
