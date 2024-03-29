import sys
import tkinter
from tkinter import messagebox

import os
import datetime
import json
import pandas as pd

from time import sleep
from googleapiclient.discovery import build

import random, string
import csv
import urllib.parse
import requests
import time
#from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import gspread
from fake_useragent import UserAgent
from google.oauth2.service_account import Credentials

def s_random(j):
    j=j+random.random()
    time.sleep(j)
    
class set_driver:
    def __init__(self,a):
        print('実行されてる')
        i = 0
        while True:
            i += 1
            if i > 5:
                try:
                    self.driver.quit()
                except:
                    pass
            option = Options()
            user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',\
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',\
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',\
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3112.113 Safari/537.36'\
                ] 
            option.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
            option.add_argument('--blink-settings=imagesEnabled=false')
            if a:
                option.add_argument('--headless')
            try:
                self.driver = webdriver.Chrome(options=option)
                s_random(1)
                self.driver.implicitly_wait(10)
                self.driver.set_page_load_timeout(30)
                print('driver 起動')
                break
            except:
                print('driver 起動失敗')
                try:
                    self.driver.quit()
                except:
                    pass
    def driver_quit(self):
        try:
            self.driver.quit()
            return True
        except:
            return False
    
    def driver_url(self,url):
        self.driver.get(url)
        s_random(2)
        
#https://www.google.com/search?q=VRB%E5%8D%94%E5%90%8C%E7%B5%84%E5%90%88+%E4%BB%A3%E8%A1%A8%E8%80%85

class request_beautiful_soup:
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {'user-agent':self.ua.chrome}
    def get_url_google(self,txt_list,url):
        txt_query = ""
        for i in range(len(txt_list)):
            #txt_query_list = txt_query_list + [urllib.parse.quote(txt_list[i])]
            txt_query += urllib.parse.quote(txt_list[i])
            if i != len(txt_list) - 1:
                txt_query += "+"
        next_url = url + txt_query
        res = requests.get(next_url,headers=self.headers)
        #print("google_URL",next_url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup
    
    def yahoo_soup(self,txt_list):
        txt_query = ""
        for i in range(len(txt_list)):
            txt_query += urllib.parse.quote(txt_list[i])
            if i != len(txt_list) - 1:
                txt_query += "+"
        next_url = "https://search.yahoo.co.jp/search?p=" + txt_query
        res = requests.get(next_url,headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup
    
    def get_url(self,url):
        res = requests.get(url,headers=self.headers)
        #print("now URL",url)
        return BeautifulSoup(res.text, "html.parser")
    
    def get_url_mojibake(self,url):
        res = requests.get(url,headers=self.headers)
        return BeautifulSoup(res.content, "html.parser")
    def return_response(self,url):
        return requests.get(url,headers=self.headers)

def txt_to_url(txt):
    return urllib.parse.quote(txt)
        
if __name__ == "__main__":
    driver = set_driver()
    driver.driver.get("https://camp.trainocate.co.jp/magazine/python-class/")
    s_random(5)
    print("kohei")
    driver.driver_quit()