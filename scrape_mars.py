from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'C:\webdrivers\chromedriver.exe'}
    browser5 = Browser('chrome', **executable_path, headless=False)
    browser5.visit(url5)

    executable_path = {'executable_path': 'C:\webdrivers\chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)
    browser2.visit(url2)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url1 = 'https://mars.nasa.gov/news/'
    response1 = requests.get(url1)
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response2 = requests.get(url2)
    url3 = 'https://twitter.com/marswxreport?lang=en'
    response3 = requests.get(url3)
    url4 = 'http://space-facts.com/mars/'
    response4 = requests.get(url4)
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response5 = requests.get(url5)
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    soup3 = BeautifulSoup(response3.text, 'html.parser')
    soup4 = BeautifulSoup(response4.text, 'html.parser')

    # mars news
    results1 = soup1.find('div', {'class':['content_title', 'rollover_description_inner']})

    for result in results1:
        news_title = soup1.find(class_='content_title').text

        news_p = soup1.find('div',  class_="rollover_description_inner").text
    
    # featured image
    for x in range(1):
    # HTML object
        html2 = browser2.html
    # Parse HTML with Beautiful Soup
        soup2 = BeautifulSoup(response2.text, 'html.parser')
    # Retrieve all elements that contain book information
        images = soup2.find_all('div', class_='img')

    # Iterate through each book
        for image in images:
            link = image.find('img')
            img_url = link['src']
    #img_url = str(image.find('data-fancybox-href'))
            featured_image_url = ('https://www.jpl.nasa.gov' + img_url)


    # weather grab
    results3 = soup3.find('p', {'class':['TweetTextSize TweetTextSize--normal js-tweet-text tweet-text']})

    mars_weather = soup3.find('p', {'class':['TweetTextSize TweetTextSize--normal js-tweet-text tweet-text']}).text

    #mars facts

    mars_facts = pd.read_html(url4)
    mf_df = mars_facts[0]
    mf_df.set_index([0], inplace=True)
    html_table = mf_df.to_html()
    html_table.replace('\n', '')

    #mars hemispheres
    final_title = []
    final_image = []

    for x in range(1):
    # HTML object
        html5 = browser5.html
    # Parse HTML with Beautiful Soup
        soup5 = BeautifulSoup(response5.text, 'html.parser')
    # Retrieve all elements that contain information
        articles = soup5.find_all('div', class_='description') 
        images = soup5.find_all('div', class_='item')


    # Iterate through each book
        for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
            title = article.find('h3').text
            final_title.append(title)
        
            for image in images:
                link = image.find('a')
                img_url = link['href']
                final_image.append('https://astrogeology.usgs.gov' + img_url)



    # Store data in a dictionary
    mars_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_weather': mars_weather,
        'mf_df': mf_df,
        'title': final_title,'img_url': final_image
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
