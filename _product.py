from unicodedata import category
from bs4 import BeautifulSoup
from numpy import product, r_
import requests

# SQL SNIPPETS
"""
CREATE TABLE PRODUCT(
PRODUCT_ID INT PRIMARY KEY,
PRODUCT_NAME VARCHAR(30),
PRICE VARCHAR(10),
CATEGORY ENUM('CLOTHES', 'SHOES') DEFAULT NULL,
BRAND VARCHAR(30) DEFAULT NULL
);
"""

"""
CREATE TABLE PRODUCT_(
PRODUCT_ID INT PRIMARY KEY,
PRODUCT_NAME VARCHAR(30),
PRICE VARCHAR(10),
CATEGORY ENUM('CLOTHES', 'SHOES') DEFAULT NULL,
BRAND VARCHAR(30) DEFAULT NULL,
IMAGE_URL VARCHAR(256),
GENDER ENUM('MENS', 'WOMENS') DEFAULT NULL,
);
"""

"""
CREATE TABLE PRODUCT_(
PRODUCT_ID INT PRIMARY KEY,
PRODUCT_NAME VARCHAR(30),
PRICE VARCHAR(10),
CATEGORY ENUM('CLOTHES', 'SHOES') DEFAULT NULL,
BRAND VARCHAR(30) DEFAULT NULL,
IMAGE_URL VARCHAR(256),
GENDER ENUM('MENS', 'WOMENS') DEFAULT NULL,
SIZES VARCHAR(256)
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

# php -S localhost:8080


# prints data in INSERT SQL form
def print_data(products, name):
    # print(f"/// PRINTING {name} DATA... ///")
    id = []
    for i in products[0:5]:
        print("INSERT INTO PRODUCT_")
        # print(
        #     f'VALUES ({i[0]}, "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", {i[5]}, "{i[6]}", "{i[7]}");'
        # )
        print_data_category(i[0], i[3], i[7])
        # print(
        #     f'VALUES ({i[0]}, "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", {i[5]}, "{i[6]}");'
        # )
        # print(
        #     f'VALUES ({i[0]}, "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", {i[5]}, "{i[6]}");'
        # )
        id.append(i[0])
    # print(f"/// ... PRINTING {name} COMPLETE \n")
    return id[len(id) - 1] + 1


def print_data_category(id, category_, sizes):
    print("INSERT INTO CLOTHES")
    for size in sizes:
        print(f'VALUES ({id}, "{category_}", "{size}")')


# scrapers url
def get_data(url, array, id, name, category_, brand, gender):
    try:
        r_url = requests.get(url, 'lxml').text
        soup = BeautifulSoup(r_url, 'lxml')
        match = soup.find(
            'ul', class_='row row-2cols--xs row-3cols--sm row-4cols--lg gutter'
        )
    except Exception as e:
        print(e)

    for x in soup.find_all('li', 'product-container col')[0:5]:
        product_name = x.find('span', 'ProductName-primary').text
        price = x.find('span', 'ProductPrice').text
        price = price[len(price) - 1 - 5:]
        image = get_image(x, brand)
        image = f'"{image}"'
        # array.append([id, product_name, price,
        #              category_, brand, image, gender])
        sizes = get_size(x, brand)
        array.append([id, product_name, price,
                     category_, brand, image, gender, sizes])
        # array.append([id, product_name, price,
        #               category_, brand])
        id += 1

    id = print_data(array, name)
    return id


def get_size(s, brand):
    s = s.find(
        "a", "ProductCard-link ProductCard-content"
    )["href"]

    if brand == "ADIDAS":
        s = s[len(s) - 11:].split(".")
        s_w_html = s[0] + "." + s[1]
        image_url = "https://www.footlocker.com/product/~/" + s_w_html
    elif brand == "NIKE":
        s = s[len(s) - 13:].split(".")
        s_w_html = s[0] + "." + s[1]
        image_url = "https://www.footlocker.com/product/~/" + s_w_html
    else:
        print("invalid")
        return None

    try:
        img = requests.get(image_url, 'lxml').text
        s = BeautifulSoup(img, 'lxml')
    except Exception as e:
        print(e)

    sizes = []
    s = s.find_all("button", "Button SizeSelector-button")
    for i in s:
        str_val = i["aria-label"]
        sizes.append(str_val.split(' ')[1])

    return sizes


def get_image(s, brand):
    s = s.find(
        "a", "ProductCard-link ProductCard-content"
    )["href"]

    if brand == "ADIDAS":
        s = s[len(s) - 11:].split(".")
        s_w_html = s[0] + "." + s[1]
        image_url = "https://www.footlocker.com/product/~/" + s_w_html
    elif brand == "NIKE":
        s = s[len(s) - 13:].split(".")
        s_w_html = s[0] + "." + s[1]
        image_url = "https://www.footlocker.com/product/~/" + s_w_html
    else:
        print("invalid")
        return None

    try:
        img = requests.get(image_url, 'lxml').text
        s = BeautifulSoup(img, 'lxml')
    except Exception as e:
        print(e)

    s = s.find("div", "ProductGallery")
    # print(s)

    try:
        s = s.find("img")["src"]
        w = 200
        h = 300
        old_size = "wid=50&hei=50&fmt=png-alpha"
        new_size = f"wid={w}&hei={h}&fmt=png-alpha"
        i = s.find(old_size)
        s = s[:i] + new_size
        return s
    except Exception as e:
        not_found = "/Users/umarkhan/Desktop/desktop/SCHOOL/Spring 2022/EECS647 - INTRO TO DB SYS/project/frontend/styles/media/image_not_found.png"
        return "NULL"


gender = "MENS"
id = 0

adidas_url_shoes = "https://www.footlocker.com/category/mens/shoes/adidas.html"
adidas_mens_shoes_product = []
adidas_mens_shoes_name = "MENS ADIDAS SHOES"
category_ = "SHOES"
brand = "ADIDAS"
id = get_data(
    adidas_url_shoes,
    adidas_mens_shoes_product,
    id, adidas_mens_shoes_name,
    category_,
    brand,
    gender
)

nike_url_shoes = "https://www.footlocker.com/category/mens/shoes/nike.html"
nike_mens_shoes_product = []
nike_mens_shoes_name = "MENS NIKE SHOES"
category_ = "SHOES"
brand = "NIKE"
id = get_data(
    nike_url_shoes,
    nike_mens_shoes_product,
    id,
    nike_mens_shoes_name,
    category_,
    brand,
    gender
)

adidas_url_tshirts = "https://www.footlocker.com/search?query=mens%20adidas%20t%20shirt"
adidas_mens_tshirt_product = []
adidas_mens_tshirt_name = "MENS ADIDAS TSHIRT"
category_ = "CLOTHES"
brand = "ADIDAS"
id = get_data(
    adidas_url_tshirts,
    adidas_mens_tshirt_product,
    id,
    adidas_mens_tshirt_name,
    category_,
    brand,
    gender
)

nike_url_tshirts = "https://www.footlocker.com/category/mens/clothing/nike/t-shirts.html?currentPage=2&SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-&gclid=Cj0KCQjw0umSBhDrARIsAH7FCodDvtMDJM7GSIzvx1iEzbTBh72bbH-1rrbVSoRuAOY6aPXxbVsJJPYaAk7CEALw_wcB&gclsrc=aw.ds"
nike_mens_tshirt_product = []
nike_mens_tshirt_name = "MENS NIKE TSHIRT"
category_ = "CLOTHES"
brand = "NIKE"
id = get_data(
    nike_url_tshirts,
    nike_mens_tshirt_product,
    id,
    nike_mens_tshirt_name,
    category_,
    brand,
    gender
)

gender = "WOMENS"
adidas_url_shoes = "https://www.footlocker.com/search?query=womens%20adidas%20shoes"
adidas_womens_shoes_product = []
adidas_womens_shoes_name = "WOMENS ADIDAS SHOES"
category_ = "SHOES"
brand = "ADIDAS"
id = get_data(
    adidas_url_shoes,
    adidas_womens_shoes_product,
    id, adidas_womens_shoes_name,
    category_,
    brand,
    gender
)

nike_url_shoes = "https://www.footlocker.com/category/mens/shoes/nike.html"
nike_womens_shoes_product = []
nike_womens_shoes_name = "WOMENS NIKE SHOES"
category_ = "SHOES"
brand = "NIKE"
id = get_data(
    nike_url_shoes,
    nike_womens_shoes_product,
    id,
    nike_womens_shoes_name,
    category_,
    brand,
    gender
)

adidas_url_tshirts = "https://www.footlocker.com/search?query=mens%20adidas%20t%20shirt"
adidas_womens_tshirt_product = []
adidas_womens_tshirt_name = "WOMENS ADIDAS TSHIRT"
category_ = "CLOTHES"
brand = "ADIDAS"
id = get_data(
    adidas_url_tshirts,
    adidas_womens_tshirt_product,
    id,
    adidas_womens_tshirt_name,
    category_,
    brand,
    gender
)

nike_url_tshirts = "https://www.footlocker.com/category/mens/clothing/nike/t-shirts.html?currentPage=2&SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-&gclid=Cj0KCQjw0umSBhDrARIsAH7FCodDvtMDJM7GSIzvx1iEzbTBh72bbH-1rrbVSoRuAOY6aPXxbVsJJPYaAk7CEALw_wcB&gclsrc=aw.ds"
nike_womens_tshirt_product = []
nike_womens_tshirt_name = "WOMENS NIKE TSHIRT"
category_ = "CLOTHES"
brand = "NIKE"
id = get_data(
    nike_url_tshirts,
    nike_womens_tshirt_product,
    id,
    nike_womens_tshirt_name,
    category_,
    brand,
    gender
)


#######################################
# from unicodedata import category
# from bs4 import BeautifulSoup
# from numpy import product, r_
# import requests

# # SQL SNIPPETS
# """
# CREATE TABLE PRODUCT(
# PRODUCT_ID INT PRIMARY KEY,
# PRODUCT_NAME VARCHAR(30),
# PRICE VARCHAR(10),
# CATEGORY ENUM('CLOTHES', 'SHOES') DEFAULT NULL,
# BRAND VARCHAR(30) DEFAULT NULL
# );
# """

# """
# INSERT INTO PRODUCT
# VALUES (<VALUES>, ...)
# """

# """
# DROP TABLE PRODUCT
# """

# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
# }

# # php -S localhost:8080


# # prints data in INSERT SQL form
# def print_data(products, name):
#     print(f"/// PRINTING {name} DATA... ///")
#     id = []
#     for i in products[0:5]:
#         print("INSERT INTO PRODUCT")
#         print(
#             f'VALUES ({i[0]}, "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", {i[5]});'
#         )
#         # print(
#         #     f'VALUES ({i[0]}, "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", {i[5]}, "{i[6]}");'
#         # )
#         id.append(i[0])
#     print(f"/// ... PRINTING {name} COMPLETE \n")
#     return id[len(id) - 1] + 1


# # scrapers url
# def get_data(url, array, id, name, category_, brand):
#     try:
#         r_url = requests.get(url, 'lxml').text
#         soup = BeautifulSoup(r_url, 'lxml')
#         match = soup.find(
#             'ul', class_='row row-2cols--xs row-3cols--sm row-4cols--lg gutter'
#         )
#     except Exception as e:
#         print(e)

#     for x in soup.find_all('li', 'product-container col')[0:5]:
#         product_name = x.find('span', 'ProductName-primary').text
#         price = x.find('span', 'ProductPrice').text
#         price = price[len(price) - 1 - 5:]
#         image = get_image(x, brand)
#         image = f'"{image}"'
#         array.append([id, product_name, price,
#                      category_, brand, image])
#         # array.append([id, product_name, price,
#         #               category_, brand])
#         id += 1

#     id = print_data(array, name)
#     return id


# def get_image(s, brand):
#     s = s.find(
#         "a", "ProductCard-link ProductCard-content"
#     )["href"]

#     if brand == "ADIDAS":
#         s = s[len(s) - 11:].split(".")
#         s_w_html = s[0] + "." + s[1]
#         image_url = "https://www.footlocker.com/product/~/" + s_w_html
#     elif brand == "NIKE":
#         s = s[len(s) - 13:].split(".")
#         s_w_html = s[0] + "." + s[1]
#         image_url = "https://www.footlocker.com/product/~/" + s_w_html
#     else:
#         print("invalid")
#         return None

#     try:
#         img = requests.get(image_url, 'lxml').text
#         s = BeautifulSoup(img, 'lxml')
#     except Exception as e:
#         print(e)

#     s = s.find("div", "ProductGallery")
#     # print(s)

#     try:
#         s = s.find("img")["src"]
#         w = 200
#         h = 300
#         old_size = "wid=50&hei=50&fmt=png-alpha"
#         new_size = f"wid={w}&hei={h}&fmt=png-alpha"
#         i = s.find(old_size)
#         s = s[:i] + new_size
#         return s
#     except Exception as e:
#         not_found = "/Users/umarkhan/Desktop/desktop/SCHOOL/Spring 2022/EECS647 - INTRO TO DB SYS/project/frontend/styles/media/image_not_found.png"
#         return "NULL"


# id = 0
# adidas_url_shoes = "https://www.footlocker.com/category/mens/shoes/adidas.html"
# adidas_mens_shoes_product = []
# adidas_mens_shoes_name = "MENS ADIDAS SHOES"
# category_ = "SHOES"
# brand = "ADIDAS"
# gender = "MALE"
# id = get_data(
#     adidas_url_shoes,
#     adidas_mens_shoes_product,
#     id, adidas_mens_shoes_name,
#     category_,
#     brand
# )

# nike_url_shoes = "https://www.footlocker.com/category/mens/shoes/nike.html"
# nike_mens_shoes_product = []
# nike_mens_shoes_name = "MENS NIKE SHOES"
# category_ = "SHOES"
# brand = "NIKE"
# id = get_data(
#     nike_url_shoes,
#     nike_mens_shoes_product,
#     id,
#     nike_mens_shoes_name,
#     category_,
#     brand,
# )

# # adidas_url_tshirts = "https://www.footlocker.com/search?query=mens%20adidas%20t%20shirt"
# # adidas_mens_tshirt_product = []
# # adidas_mens_tshirt_name = "MENS ADIDAS TSHIRT"
# # category_ = "CLOTHES"
# # brand = "ADIDAS"
# # id = get_data(
# #     adidas_url_tshirts,
# #     adidas_mens_tshirt_product,
# #     id,
# #     adidas_mens_tshirt_name,
# #     category_,
# #     brand,
# #     gender
# # )

# # nike_url_tshirts = "https://www.footlocker.com/category/mens/clothing/nike/t-shirts.html?currentPage=2&SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-SID=5403&inceptor=1&cm_mmc=paid%20search-_-google-_-g-_-non-brand-_--_--_-p-_--_--_-14813690286-_--_-128687528078-_-dynamic-_-p67393659753-_-552876788063-_--_--_--_-&gclid=Cj0KCQjw0umSBhDrARIsAH7FCodDvtMDJM7GSIzvx1iEzbTBh72bbH-1rrbVSoRuAOY6aPXxbVsJJPYaAk7CEALw_wcB&gclsrc=aw.ds"
# # nike_mens_tshirt_product = []
# # nike_mens_tshirt_name = "MENS NIKE TSHIRT"
# # category_ = "CLOTHES"
# # brand = "NIKE"
# # id = get_data(
# #     nike_url_tshirts,
# #     nike_mens_tshirt_product,
# #     id,
# #     nike_mens_tshirt_name,
# #     category_,
# #     brand,
# #     gender
# # )
