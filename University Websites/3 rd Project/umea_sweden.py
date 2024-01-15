from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    
    data_list = []
    for i in range(1,68):
        page.goto(f'https://www.umu.se/en/search/?q=y&f=Personal&page={i}')
        page.wait_for_load_state("domcontentloaded") 
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')  
    
        divs = soup.find_all('div',class_='person')
        
        for div in divs:
            try:
                name = div.find('div', class_='title').find('a').text.strip()
                first_name =name.split()[0]
            except AttributeError:
                name, first_name = None, None

            try:
                position = div.find('div', class_='title').find('span').get_text(strip=True).replace(',','')
            except AttributeError:
                position = None

            try:
                faculty = div.find('div', class_='organisationer').get_text(strip=True)
            except AttributeError:
                faculty = None

            try:
                phone = div.find('div', class_='telefon').find('a', class_='tfn').get_text(strip=True)
            except AttributeError:
                phone = None

            try:
                email = div.find('div', class_='epost').find('a').get_text(strip=True)
            except AttributeError:
                email = None
            university = 'UMEA'
            print(name)
            print(first_name)
            print(email)
            print(university)
            print(position)
            print(faculty)
            print(phone)
            print("=================================")
            data_list.append([first_name, email, name, position, university, faculty, phone])
df = pd.DataFrame(data_list, columns=['First Name','Email', 'Name', 'Position', 'University', 'Faculty', 'Phone'])
print(df)


df.to_excel('UMEA-y.xlsx', index=False)
    

            
