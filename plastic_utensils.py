from math import prod
from string import whitespace
from unicodedata import category
from bs4 import BeautifulSoup
from numpy import product, r_
import requests

"""

CREATE TABLE PRODUCT(
PRODUCT_ID INT PRIMARY KEY UNIQUE,
PRODUCT_NAME VARCHAR(256),
PRICE VARCHAR(30),
IMAGE_URL VARCHAR(256),
COLOR ENUM('BLACK', 'WHITE', 'OTHER') DEFAULT NULL,
WEIGHT ENUM('LIGHT', 'MEDIUM', 'HEAVY', 'OTHER') DEFAULT NULL,
TYPE ENUM('SPOON', 'FORK', 'KNIFE', 'SPORK', 'OTHER') DEFAULT NULL
);

"""

"""

CREATE TABLE CART_DETAIL(
CART_DETAIL_ID INT PRIMARY KEY UNIQUE,
CART_ID INT,
FOREIGN KEY (CART_ID) REFERENCES CART(CART_ID),
PRODUCT_ID INT,
FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT(PRODUCT_ID),
QUANTITY INT,
TOTAL_PRICE VARCHAR(30)
);

"""

"""

CREATE TABLE CART(
CART_ID INT PRIMARY KEY UNIQUE,
USERNAME VARCHAR(30),
FOREIGN KEY (USERNAME) REFERENCES USER(USERNAME)
);

"""


"""

CREATE TABLE USER
(
USERNAME VARCHAR(30) PRIMARY KEY UNIQUE,
PASSWORD VARCHAR(30),
FIRST_NAME VARCHAR(30),
LAST_NAME VARCHAR(30)
);

'''
INSERT INTO USER (USER_ID, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME)
VALUES (0, "UMI", "TEST1", "UMAR", "KHAN");
'''

"""


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}


def print_data(products):
    for p in products:
        print("INSERT INTO PRODUCT")
        print(
            f'VALUES ({p[0]}, \'{p[1]}\', \'{p[2]}\', \'{p[3]}\', \'{p[4]}\', \'{p[5]}\', \'{p[6]}\');'
        )


def get_data(url, products, name, type, id):
    try:
        r_url = requests.get(url, 'lxml').text
        s = BeautifulSoup(r_url, 'lxml')
    except Exception as e:
        print(e)
        return -1

    s = s.find_all('li', 'product')

    for i in s:
        name = get_name(i)
        price = get_price(i)
        image_url = get_image(i)
        color = get_color(i)
        weight = get_weight(i)
        type = get_type(i)
        if "FACE SHIELDS" not in name:
            products.append(
                [id, name, price, image_url, color, weight, type])
        id += 1

    print_data(products)


def get_name(i):
    name = i.find('h4', 'card-title')
    name = name.find('a').text
    return name


def get_price(i):
    price = i.find('span', 'price price--withoutTax price--main').text
    return price


def get_image(i):
    image = i.find('img')['src']
    return image


def get_color(i):
    name = i.find('h4', 'card-title')
    name = name.find('a').text.lower()

    if "black" in name:
        return "BLACK"
    elif "white" in name:
        return "WHITE"
    else:
        return "OTHER"


def get_weight(i):
    name = i.find('h4', 'card-title')
    name = name.find('a').text.lower()

    if "heavy" in name:
        return "HEAVY"
    elif "medium" in name:
        return "MEDIUM"
    elif "light" in name:
        return "LIGHT"
    else:
        return "OTHER"


def get_type(i):
    name = i.find('h4', 'card-title')
    name = name.find('a').text.lower()

    if "fork" in name:
        return "FORK"
    elif "spoon" in name:
        return "SPOON"
    elif "knife" in name:
        return "KNIFE"
    elif "spork" in name:
        return "SPORK"
    else:
        return "OTHER"

    # can be spoon, fork, knife, spork
id = 0
url = "https://www.wowplastics.com/cutlery/?gclid=Cj0KCQjw3v6SBhCsARIsACyrRAkNPulayZRPux-cbfFpDEiNvWVpf1a2NUszJaIN7xPcdk7tj_cHqm8aAhEJEALw_wcB"
products = []
name = "MENS ADIDAS SHOES"
type = "SHOES"
id = get_data(
    url, products, name, type, id
)
