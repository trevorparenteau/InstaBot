
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#gets username and password

username = input("Enter username: ")
password = input("Enter password: ")

tags = []

print("You can enter up to 10 tags. Type quit or press enter when done")

#gets user tags 

def getInputs(userString, numStrings):
    while (userString != "quit") and (numStrings <= 10):
        userString = input(f"Tag {numStrings}: ")
        if not userString:
            break
        tags.append(userString)
        numStrings += 1

uString = input("Tag 1: ")
nStrings = 1

if not uString:
    while (not uString):
        print("Must enter at least 1 tag")
        uString = input("Tag 1: ")
        tags.append(uString)
        nStrings = 2
    getInputs(uString, nStrings)
else: 
    tags.append(uString)
    nStrings = 2
    getInputs(uString, nStrings)

comment = input("Type what you would like to comment on posts: ")

#navigates to Instagram 

PATH = "/Users/trevorparenteau/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

time.sleep(2)

#enters login information and gets to home page 

usernameBox = driver.find_element_by_css_selector("[name='username']")
passwordBox = driver.find_element_by_css_selector("[name='password']")
login = driver.find_element_by_css_selector("button")

usernameBox.send_keys(username)
passwordBox.send_keys(password)
login.click()

time.sleep(3)

saveInfo = driver.find_element_by_css_selector("[class='sqdOP yWX7d    y3zKF     ']")

saveInfo.click()

time.sleep(2)

notifications = driver.find_element_by_css_selector("[class='aOOlW   HoLwm ']")

notifications.click()

# finds posts in tags, follows accounts, likes posts, and comments 

def Vist_Tag(driver, url):
    driver.get(url)
    time.sleep(5)

    # to prevent an account ban, there is a limit of 20 actions per hour 
    # for best results, run program once per hour

    actionsLimitPerHour = 20 / len(tags)

    pictures = driver.find_elements_by_css_selector("div[class='_9AhH0']")

    imageCount = 0

    for picture in pictures:

        if imageCount >= actionsLimitPerHour:
            break

        picture.click()
        time.sleep(3)

        followButton = driver.find_element_by_css_selector("[class='sqdOP yWX7d    y3zKF     '")
        followButton.click()

        time.sleep(random.random() * 3)
        
       
        try:
            likeButton = driver.find_element_by_class_name('fr66n')
            likeButton.click()
        except: 
            print("Error: couldn't like")
        
        finally:

            time.sleep(random.random() * 3)
        
      
            commentBox = driver.find_element_by_class_name('Ypffh')
            commentBox.click()

            time.sleep(random.random() * 3)
        
            commentBox = driver.find_element_by_class_name('Ypffh')
            commentBox.send_keys(comment)

            commentBox.submit()

            time.sleep(4)

            closeButton = driver.find_element_by_css_selector("[aria-label='Close']")
            closeButton.click()

            imageCount += 1

            time.sleep(5)


for tag in tags:
    Vist_Tag(driver, f"https://www.instagram.com/explore/tags/{tag}")