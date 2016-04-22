from selenium import webdriver
import os
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import threading
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import traceback
import csv
import itertools
import fileinput
import random

url_funding = ['https://angel.co/3v-sourceone-ventures','https://angel.co/advanced-risk-management-solutions','https://angel.co/analog','https://angel.co/azione-capital','https://angel.co/baf-spectrum','https://angel.co/bambou-tree-ventures','https://angel.co/bc-capital-group','https://angel.co/blueue','https://angel.co/booster-pack','https://angel.co/bwb','https://angel.co/cardover','https://angel.co/cawaii-koohii-cosplay-cafeteria','https://angel.co/chicago-roadside','https://angel.co/cryonics-asia','https://angel.co/curve','https://angel.co/dilivrit','https://angel.co/dsg-growth','https://angel.co/engage','https://angel.co/flopay','https://angel.co/freelance-loner','https://angel.co/fsc','https://angel.co/global-asia-partners','https://angel.co/golearn','https://angel.co/ihram','https://angel.co/influr','https://angel.co/maritime-technologies','https://angel.co/my-small-world','https://angel.co/national-university-of-singapore','https://angel.co/neue','https://angel.co/next-frontier','https://angel.co/novy-ideas-pte','https://angel.co/papyri','https://angel.co/pixl-pte','https://angel.co/portagram','https://angel.co/qliqqliq','https://angel.co/rattr','https://angel.co/recordtv','https://angel.co/rvcr','https://angel.co/saahi-info-labs','https://angel.co/selling-profitable-beauty-salon','https://angel.co/singapore-angel-network','https://angel.co/skydio','https://angel.co/smartfuture','https://angel.co/srecko','https://angel.co/stealth-mode','https://angel.co/stirling-asset-management','https://angel.co/the-software-practice','https://angel.co/thrive-water','https://angel.co/tinker','https://angel.co/travelhoof','https://angel.co/usb-alchemist']
driver = webdriver.Firefox()

for k in range (0, 52):
    driver.get(url_funding[k])
    #time.sleep(1)
    '''
    try:
        print driver.find_element_by_css_selector("div.name_holder").text
    except:
        print "NO NAME"
    '''
    print url_funding[k]
    try:
        print driver.find_element_by_css_selector("a.company_url").get_attribute("href")
    except:
        print "NO URL"
    try:
        driver.find_element_by_css_selector("div.product_desc.editable_region div.show div.content").text
        print '^'
        print driver.find_element_by_css_selector("div.product_desc.editable_region div.show div.content").text
        print '^'
    except:
        print "FATAL ERROR"
        pass

    print "###"
    '''
    try:
        print driver.find_element_by_css_selector("a.twitter_url.icon_link.fontello-twitter").get_attribute("href")
    except:
        print "NO Twitter"
    try:
        print driver.find_element_by_css_selector("a.facebook_url.icon_link.fontello-facebook").get_attribute("href")
    except:
        print "NO Facebook"
    try:
        print driver.find_element_by_css_selector("a.linkedin_url.icon_link.fontello-linkedin").get_attribute("href")
    except:
        print "NO Linkedin"
    try:
        print driver.find_element_by_css_selector("h2.high_concept").text
    except:
        print "NO CONCEPT"
    try:
        print driver.find_element_by_css_selector("div.tags").text
    except:
        print "NO INDUSTRY"
    for i in range (1, 5):
        try:
            print driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.text > div.name").text
            try:
                driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.text > div.bio").text
                print '"'
                print driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.text > div.bio").text
                print '"'
            except:
                print "No title for " #+str(i)
                pass
        except:
            print "No person for " #+str(i)
            print "No title for " #+str(i)
            pass
        
    for i in range (1, 5):
        try:
            try:
                print "SEEDINFO " +str(i)
                driver.find_element_by_css_selector("div.dsss17.startups-show-sections.fss49.startup_rounds._a._jm > ul > li:nth-child(1) > div > div").text
                print '"'
                print driver.find_element_by_css_selector("div.dsss17.startups-show-sections.fss49.startup_rounds._a._jm > ul > li:nth-child(1) > div > div").text
                print '"'
            except:
                print "No Seed"
            try:
                #print driver.find_element_by_css_selector("li:nth-child(1) > div > div > div.header > div.date_display").text
                print driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.details.inner_section > div.header > div.date_display").text
            except:
                print "NO Date"
            try:
                print driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.details.inner_section > div.raised").text
            except:
                print "No Money"
            
            for j in range (1, 5):
                try:
                    print driver.find_element_by_css_selector("li:nth-child(" +str(i) + ") > div > div > div.participant_list.inner_section > div:nth-child(" +str(j) + ") > div.text > div.name > a").text
                except:
                    print "NO Investor " #+ str(j)
        except:
            print str(url_funding[k])
    print "@@@"
    '''
