import mechanize
import urllib
import cookielib
from bs4 import BeautifulSoup
import html2text
import re
import sys
import StringIO
import getpass
from easygui import passwordbox
import collections
import urllib2
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
#try:

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)


br.set_handle_gzip(False)


br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Chrome')]


browser = webdriver.Chrome()
#browser = webdriver.PhantomJS(executable_path='C:\Users\Zack\Desktop\deskTweet\phantomjs.exe')

# The site we will navigate into, handling it's session
br.open('https://twitter.com/')

# Inspect name of the form
'''
for f in br.forms():
print f
'''
# Select the second (index one) form - the first form is a search query box
br.select_form(nr=1) 

#browser.get('https://twitter.com/')



browser.delete_all_cookies()

# User credentials
#####HANDLE LOGIN CHECKING#####
username = raw_input("Phone, email or username: ")
print "Password: "
password = passwordbox("Password: ")

#password = getpass.getpass() #-> echos pass with IDLE
#password = raw_input("Password: ") -> echos pass


br.form['session[username_or_email]'] = username
br.form['session[password]'] = password


# Login
br.submit()

#Prints html of main page after login
br.open('https://twitter.com/')
browser.get('https://twitter.com')

if str(username) not in br.response().read():
    print "\n***Login failed***\n"

else:
    	
    user = browser.find_element_by_id('signin-email')
    passw = browser.find_element_by_id('signin-password')
    user.send_keys(str(username).lower())
    passw.send_keys(password)
    browser.save_screenshot("login.png")
	
    LOGIN_BUTTON_XPATH = '//*[@id="front-container"]/div[2]/div[2]/form/table/tbody/tr/td[2]/button'
    button = browser.find_element_by_xpath(LOGIN_BUTTON_XPATH)
    button.click()
    time.sleep(1)
    browser.save_screenshot("home.png")
    print "\nWelcome @" + str(username) +"\n"

    COMPOSE_FIELD_XPATH = '//*[@id="tweet-box-mini-home-profile"]'
    field = browser.find_element_by_xpath(COMPOSE_FIELD_XPATH)
    field.click()
    browser.save_screenshot("compose.png")

    defaultText = browser.find_element_by_xpath("//*[@id='tweet-box-mini-home-profile']/div/br").text
    print "In tweetbox -> ("+str(defaultText)+")"
    
    #browser.find_element_by_xpath("//*[@id='tweet-box-mini-home-profile']/div").send_keys(message)
    browser.save_screenshot("default.png")



    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='tweet-box-mini-home-profile']").send_keys("ping3")
    changedText = browser.find_element_by_xpath("//*[@id='tweet-box-mini-home-profile']/div").text
    browser.save_screenshot("myTweet.png")
    print "In tweetbox -> ("+str(changedText)+")"
    time.sleep(2)
    TWEET_SEND_XPATH = '//*[@id="page-container"]/div[2]/div[1]/div/div[3]/form/div[2]/div[2]/button'
    send = browser.find_element_by_xpath(TWEET_SEND_XPATH)
    send.click()
    time.sleep(2)
    browser.save_screenshot("sent.png")
    print "Tweet successfully posted!"

    '''
    TWEET_XPATH = '//*[@id="tweet-box-mini-home-profile"]/div'
    TWEET_TEXT = browser.find_element_by_xpath(TWEET_XPATH)


    browser.findElement(By.xpath('//*[@id="tweet-box-mini-home-profile"][div[text()="hello world"]]'));
    #TWEET_TEXT.send_keys('dnkjasnd')
    browser.save_screenshot("tweet.png")



    start = browser.find_element_by_xpath("//*[@id='tweet-box-mini-home-profile']/div").getText()
    print start
    '''
    
    '''
    time.sleep(3)
        
    time.sleep(2)
    #box = browser.find_element_by_id('tweet-box-mini-home-profile')
    '''




    '''
    root = etree.fromstring('<div aria-labelledby="tweet-box-mini-home-profile-label" id="tweet-box-mini-home-profile" class="tweet-box rich-editor  notie" contenteditable="true" spellcheck="true" role="textbox" aria-multiline="true" dir="ltr" aria-autocomplete="list" aria-expanded="false" aria-owns="typeahead-dropdown-11"><div>(.+?)</div></div>')
    root.xpath("//*[@id='tweet-box-mini-home-profile']/div/text()")[0] = "This is my tweet"
    '''


    '''
    regex = '<div aria-labelledby="tweet-box-mini-home-profile-label" id="tweet-box-mini-home-profile" class="tweet-box rich-editor  notie" contenteditable="true" spellcheck="true" role="textbox" aria-multiline="true" dir="ltr" aria-autocomplete="list" aria-expanded="false" aria-owns="typeahead-dropdown-11"><div>(.+?)</div></div>'
    pattern = re.compile(regex)
    htmltext = br.open('https://twitter.com/').read()
    tweetText = re.findall(pattern,htmltext)
        
    print tweetText
    '''
  
#tweet = raw_input("What would you like to Tweet? ")
	
#tweetText = tree.xpath("//*[@id='tweet-box-mini-home-profile']/div/text()")
#print tweetText



#print(html.xpath("//*[@id='tweet-box-mini-home-profile']/div/text()"))




'''
regex = '<div aria-labelledby="tweet-box-mini-home-profile-label" id="tweet-box-mini-home-profile" class="tweet-box rich-editor  notie" contenteditable="true" spellcheck="true" role="textbox" aria-multiline="true" dir="ltr" aria-autocomplete="list" aria-expanded="false" aria-owns="typeahead-dropdown-11"><div>(.+?)</div></div>'
pattern = re.compile(regex)
htmltext = br.open('https://twitter.com/').read()
tweetText = re.findall(pattern,htmltext)
print tweetText
'''


'''
soup_xpath = "//*[@id='tweet-box-mini-home-profile']/div/text()"
tweetText = soup.xpath(soup_xpath)
print "this is the tweet: \n" + tweetText +"\n"
'''

#except:
#print "~~~Exception Thrown! Most likely incorrect login credentials.~~~"
