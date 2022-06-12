from search_bot import SearchBot
from time import sleep
import random
import os

websites = []
number = int(input("Number of elements in array:"))
for i in range(0,number):
    search_value = input()
    websites.append(search_value)
number2 = int(input("How many times you want to visit the site:"))
country = input("Which country do you want?")
counter = 0



with SearchBot() as bot:
    while counter != number2:
        for value in websites:
            os.system("windscribe connect " + country)
            bot.land_first_page()
            sleep(5 + random.random())
            bot.accept_google_cookie()
            sleep(5 + random.random())
            bot.inserting_values(value)
            sleep(5 + random.random())
            bot.open_website()
            sleep(5 + random.random())
            bot.accept_cookie()
            sleep(20 + random.random())
            os.system("windscribe disconnect")
        counter += 1
