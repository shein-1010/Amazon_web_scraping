def get_product_name(soup):
    try:
        product_name = soup.find("span",attrs={"id":"productTitle"})
        product_name_text =product_name.text
        product_name_string = product_name_text.strip()



    except AttributeError:
        title_string = ""

    return product_name_string



def get_price(soup):
    try:
        price =soup.find("span",attrs={"class":"a-offscreen"}).string.strip()


    except AttributeError:
        price=""
    return price


def get_rating(soup):
    try:
        rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
    except AttributeError:
        rating = "n/a"
    return rating



def get_reviews(soup):
    try:
        review = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review = "n/a"
    return review