import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

init_browser()

url= https://mars.nasa.gov/news 