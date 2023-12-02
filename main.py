import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# this one gets all King's books and their publishing date

# driver.get("https://stephenking.com/works/novel/index.html")
#
# books = driver.find_elements(By.CLASS_NAME, value="works-title")
# dates = driver.find_elements(By.CLASS_NAME, value="works-date")
# stephen_kings_books = []
#
# for book, date in zip(books, dates):
#     kings_books = {
#         "title": book.text,
#         "date": date.text
#     }
#     stephen_kings_books.append(kings_books)
#
# print(stephen_kings_books)
#
# driver.close()

#this one gets 100 most played games on steam and their numbers
driver.get("https://steamdb.info/charts/")

table = driver.find_element(By.CLASS_NAME, 'table-products')
rows = table.find_elements(By.TAG_NAME, 'tr')
top_games= []

for row in rows:
    try:
        game = {
            "Name": row.find_elements(By.TAG_NAME, 'td')[2].text,
            "Current Players": row.find_elements(By.TAG_NAME, 'td')[3].text,
            "24 Hour Peak": row.find_elements(By.TAG_NAME, 'td')[4].text,
            "All Time Peak": row.find_elements(By.TAG_NAME, 'td')[5].text
        }
        top_games.append(game)
    except IndexError:

        print("No third cell in this row")


print(top_games)
driver.close()
