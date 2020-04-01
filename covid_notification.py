from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

#function to generate notification
def notify(title, message):
	notification.notify(
	title = title,
	message = message,
	app_icon = "img/icon.ico",#only .ico file will work
	timeout = 10
	)


#get data from webpage
def getData(url):
	r = requests.get(url)
	return r.text



if __name__ == "__main__":

	while True:

		htmlData = getData('https://www.mohfw.gov.in/')

		#represent html as nested data structure
		soup = BeautifulSoup(htmlData, 'html.parser')

		data = ""
		#finding text inside all tr elements and appending into single string
		for tr in soup.find_all('tbody')[0].find_all('tr'):
			data += tr.get_text()
	
		data = data[1:]

		#separate state wise and making a list
		dataList = data.split("\n\n")

		#list of states for which you want to get notifications
		states = ['Andhra Pradesh','Maharashtra','Gujarat']

		for info in dataList[0:26]:
			#separating data of a state(sr no, state, cases, cured, deaths)
			stateInfo = info.split("\n")

			#generate notiication for only those states which are mentioned in list
			if stateInfo[1] in states:
				#set title and message
				notification_title = 'Updates of COVID-19'
				notification_message = f"State : {stateInfo[1]}\nCases(Including foreign Nationals) : {stateInfo[2]}\nCured : {stateInfo[3]}\nDeaths : {stateInfo[4]}" 
				#call notify function
				notify(notification_title, notification_message)
				time.sleep(3)

		#to get notifications in every half an hour
		time.sleep(1800)
