# Welcome to Python Webscrapper

Hello, in this project we're going to see how to construct the basis of your webscrapping project!

## First Steps
We need to install some items first

 1. Download [Python here!](https://www.python.org/downloads/)
 2. Download Webdrive Chrome - [Chromedriver](https://chromedriver.chromium.org/home)
 3. *Optional* - Install [Git Bash](https://git-scm.com/downloads)
 4. *Optional* - Download [Visual Studio Code](https://code.visualstudio.com/)

## Setting up the enviroment

Note: We're using the selenium library

We need to make sure that pip is installed, so run the command on your terminal
`pip --version`
Hopefully you will get something like: 
`pip 21.1.3 from [...]`

`pip install selenium`

it's important that you know the location of **chromedriver.exe**, I personally like to move it to a new file were we're going to work.

following the structure:
/.workspace/
|_____ chromedriver.exe
|_____ *{your_webscripping_file}.py*

    import time
    from selenium import webdriver
    
    driver  = webdriver.Chrome('/path/to/chromedriver') # Optional argument, if not specified will search path.
    
    driver.get('http://www.google.com/');
    
    time.sleep(5) # Let the user actually see something!
    
    search_box  =  driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    
    time.sleep(5) # Let the user actually see something!
    driver.quit()


## Now it's your turn
From this point on, you're ready to go!
We've got all the basis for the Selenium project to flow.
