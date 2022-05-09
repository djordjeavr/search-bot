from search_bot import SearchBot
from time import sleep
import random

websites = []
number = int(input("Number of elements in array:"))
for i in range(0,number):
    search_value = input()
    websites.append(search_value)
number2 = int(input("How many times you want to visit the site:"))
counter = 0



with SearchBot() as bot:
    while counter != number2:
        for value in websites:
            bot.land_first_page()
            sleep(3 + random.random())
            bot.inserting_values(value)
            sleep(3 + random.random())
            bot.open_website()
            sleep(3 + random.random())
            bot.accept_cookie()
            sleep(20 + random.random())
        counter += 1