from bs4 import BeautifulSoup
from numpy import r_
import requests

# SQL SNIPPETS
"""
CREATE TABLE USER
(
USERNAME VARCHAR(30) PRIMARY KEY UNIQUE,
PASSWORD VARCHAR(30),
FIRST_NAME VARCHAR(30),
LAST_NAME VARCHAR(30)
);
"""

'''
INSERT INTO USER (USER_ID, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME)
VALUES (0, "UMI", "TEST1", "UMAR", "KHAN");
'''

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
