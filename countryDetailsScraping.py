import requests
from bs4 import BeautifulSoup

def scraping():
    url = "https://www.scrapethissite.com/pages/simple/"
    
    # Standard practice: Add a User-Agent so you look like a real visitor
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Use requests.get() instead of just requests()
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        html = response.content
        scraped = BeautifulSoup(html, 'html.parser')

        with open('country_details.txt', 'w', encoding='utf-8') as f:
            # Write a header row for your CSV-style text file
            f.write("Country,Capital,Population,Area\n")
            
            for row in scraped.find_all('div', class_='col-md-4 country'):
                country = row.find(class_='country-name').text.strip()
                capital = row.find(class_='country-capital').text.strip()
                population = row.find(class_='country-population').text.strip()
                area = row.find(class_='country-area').text.strip()
            
                line = f"{country},{capital},{population},{area}"
                print(line)
                f.write(line + '\n')
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    scraping()





































'''import requests
from bs4 import BeautifulSoup

def scraping():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests(url)
    html = response.content
    scraped = BeautifulSoup(html, 'html.parser')

    # Open the file once before the loop starts
    with open('country_details.txt', 'w', encoding='utf-8') as f:
        for row in scraped.find_all('div', class_='col-md-4 country'):
            # .strip() removes leading/trailing whitespace and newlines
            country = row.find(class_='country-name').text.strip()
            capital = row.find(class_='country-capital').text.strip()
            population = row.find(class_='country-population').text.strip()
            area = row.find(class_='country-area').text.strip()
        
            # Using an f-string for cleaner formatting
            line = f"{country},{capital},{population},{area}"
        
            print(line)
            f.write(line + '\n')



if __name__ == "__main__":
    scraping()
'''