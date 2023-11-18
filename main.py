import pandas as pd
import requests
from bs4 import BeautifulSoup
import functions_get_data



URL = "https://www.amazon.in/s?hidden-keywords=B09V1F446C+%7C+B09V1DYYV6+%7C+B09Z1ZG7Y3+%7C+B09Z216R5Q+%7C+B09V1G8BQ6+%7C+B09V19T1XR+%7C+B09V1GJT8M+%7C+B09V1CMJ8G+%7C+B0BS9GT77Q+%7C+B0BS9GCYRN+%7C+B0BS9GGMW5+%7C+B0BSH4MRWR+%7C+B0BSH521SV+%7C+B0BSH5Q4QQ+%7C+B0BSH5GLB3+%7C+B0BSH3JFP2+%7C+B0BSNM47LZ+%7C+B0BSNNC21T+%7C+B0BSNMWS9B+%7C+B0BSNNVK2W+%7C+B0BSNMM83B+%7C+B0BSNPDKJ3+%7C+B0BT3D4QSG+%7C+B0BT4N1P4K+%7C+B0BT2ZS1TB&pf_rd_i=1375424031&pf_rd_m=AT95IG9ONZD7S&pf_rd_p=cc885334-028d-4368-a478-00b4c158c340&pf_rd_r=6CE84QC54MGW0501X8W6&pf_rd_s=merchandised-search-18&pf_rd_t=101&ref=s9_acss_bw_cg_PDPrint_2b1_w"
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

# pull the webpage to variable called webpage
webpage = requests.get(URL,headers=HEADERS)

# convert the webpage into HTML format
soup = BeautifulSoup(webpage.content, "html.parser")


# separate links and store links
links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
product_list = []

#iterate through the links list and convert href to actual http link
for x in links:
    product_list.append("https://amazon.in" + x.get("href"))

#create a dictionary to store all scrapping values

columns = {"Product_name":[],"price":[],"rating":[],"user_reviews":[]}

# iterate through links and get values of each webpage then store the values into dictionary.
for y in product_list:
    new_webpage = requests.get(y, headers=HEADERS)
    new_soup = BeautifulSoup(new_webpage.content, "html.parser")

    columns["Product_name"].append(functions_get_data.get_product_name(new_soup))
    columns["price"].append(functions_get_data.get_price(new_soup))
    columns["rating"].append(functions_get_data.get_rating(new_soup))
    columns["user_reviews"].append(functions_get_data.get_reviews(new_soup))

# create a data frame and store the dictionary values
#convert the data frame into csv file.

amazon_df = pd.DataFrame.from_dict(columns)
amazon_df.to_csv("amazon_web_scraping_final.csv",header=True,index=False)
