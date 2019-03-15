import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

NASA_url= 'https://mars.nasa.gov/news'

browser.visit(NASA_url)

time.sleep(1)
NASA_html = browser.html
NASA_soup = bs(NASA_html, "lxml")

[x.text for x in NASA_soup.select(".content_title")]

Nasa_total = NASA_soup.find_all ('li', class_='slide')
Nasa_news_title = Nasa_total[0].find('div', class_='content_title').text
Nasa_news_preparation = Nasa_total[0].find('div', class_='article_teaser_body').text
print(Nasa_news_title) 
print(Nasa_news_preparation)

JPL_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

browser.visit(JPL_url)

JPL_html = browser.html

JPL_soup=bs(JPL_html,'lxml')

space_image = JPL_soup.find(id="full_image")["data-fancybox-href"]
print(space_image)

featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18907_ip.jpg'

Mars_Weather_url = 'https://twitter.com/marswxreport?lang=en'

browser.visit(Mars_Weather_url)

Mars_Weather_html = browser.html

Mars_Weather_soup = bs(Mars_Weather_html, 'lxml')

print(Mars_Weather_soup)

latest_tweet = Mars_Weather_soup.find("p", {"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"},1)
print(latest_tweet)

mars_weather = latest_tweet

Mars_Facts_url = 'http://space-facts.com/mars/'

tables_Mars_Facts = pd.read_html(Mars_Facts_url)

print(tables_Mars_facts)

Mars_Hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

hemisphere_image_urls = 

browser.quit()