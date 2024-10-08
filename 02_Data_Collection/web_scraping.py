from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib, math, time, os, pandas as pd

options = Options()
# options.add_argument("--headless=new") 
# options.add_argument('--window-size=974,1047')
# options.add_argument('--window-position=953,0')
options.add_experimental_option("detach", True)
