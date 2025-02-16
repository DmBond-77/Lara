from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

def get_all_categories():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    categories = {}
    
    try:
        driver.get("https://books.toscrape.com/index.html")
        category_elements = driver.find_elements(By.CSS_SELECTOR, ".side_categories ul li a")
        for category in category_elements[1:]:  # Пропускаем первую категорию "Books"
            category_name = category.text.strip()
            category_url = category.get_attribute("href")
            categories[category_name] = category_url
    finally:
        driver.quit()
    
    return categories

def get_books_from_category(category_url, category_name):
    books = []
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(category_url)
        while True:
            book_cards = driver.find_elements(By.CSS_SELECTOR, ".product_pod")
            for card in book_cards:
                title_element = card.find_element(By.CSS_SELECTOR, "h3 a")
                title = title_element.get_attribute("title") or title_element.text
                price = card.find_element(By.CSS_SELECTOR, ".price_color").text.replace("£", "")
                image_url = card.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
                book_url = title_element.get_attribute("href")
                
                rating_element = card.find_element(By.CSS_SELECTOR, ".star-rating")
                rating_text = rating_element.get_attribute("class")
                rating = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}.get(rating_text.split()[-1], 0)
                
                if rating > 0:  # Исключаем 'Not rated'
                    books.append([title, price, rating, image_url, book_url, category_name])
            
            next_page = driver.find_elements(By.CSS_SELECTOR, ".next a")
            if next_page:
                next_url = next_page[0].get_attribute("href")
                driver.get(next_url)
                time.sleep(2)  # Ждем загрузки страницы
            else:
                break
    finally:
        driver.quit()
    
    return books

def save_to_csv(data, filename="books.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating", "Image URL", "Book URL", "Category"])
        writer.writerows(data)

if __name__ == "__main__":
    categories = get_all_categories()
    all_books = []
    for category_name, category_url in categories.items():
        all_books.extend(get_books_from_category(category_url, category_name))
    save_to_csv(all_books)
    print(f"Saved {len(all_books)} books to books.csv")
