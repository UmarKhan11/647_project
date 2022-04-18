from bs4 import BeautifulSoup
from numpy import r_
import requests

# SQL SNIPPETS
"""
CREATE TABLE CART
(
CART_ID INT PRIMARY KEY UNIQUE,
USERNAME VARCHAR(30),
FOREIGN KEY (USERNAME) REFERENCES USER(USERNAME)
);
"""

"""
INSERT INTO PRODUCT
VALUES (<VALUES>, ...)
"""

"""
DROP TABLE PRODUCT
"""

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}
