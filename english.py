import telebot
import time
from threading import Thread
import random
import schedule

token = #your token
bot = telebot.TeleBot(token)

myid = #your telegram id

def schedule_time():
	while True:
		schedule.run_pending()
		time.sleep(1)

def file():
	textfile = open('english.txt', 'r')
	random_list = textfile.readlines()
	bot.send_message(myid, random.choice(random_list))
if __name__ == "__main__":

    schedule.every().day.at('09:00').do(file)
    schedule.every().day.at('09:30').do(file)
    schedule.every().day.at('10:00').do(file)
    schedule.every().day.at('10:30').do(file)
    schedule.every().day.at('11:00').do(file)
    schedule.every().day.at('11:30').do(file)
    schedule.every().day.at('12:00').do(file)
    schedule.every().day.at('12:30').do(file)
    schedule.every().day.at('13:00').do(file)
    schedule.every().day.at('13:30').do(file)
    schedule.every().day.at('14:00').do(file)
    schedule.every().day.at('14:30').do(file)
    schedule.every().day.at('15:00').do(file)
    schedule.every().day.at('15:30').do(file)
    schedule.every().day.at('16:00').do(file)
    schedule.every().day.at('16:30').do(file)
    schedule.every().day.at('17:00').do(file)
    schedule.every().day.at('17:30').do(file)
    schedule.every().day.at('18:00').do(file)
    schedule.every().day.at('18:30').do(file)
    schedule.every().day.at('19:00').do(file)
    schedule.every().day.at('19:30').do(file)
    schedule.every().day.at('20:00').do(file)
    Thread(target=schedule_time).start()
