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

		htmlData = getData('https://www.deccanherald.com/national/coronavirus-india-karnataka-maharashtra-delhi-tamil-nadu-kerala-update-state-wise-total-number-of-confirmed-cases-vaccine-deaths-on-june-8-995035.html')

		#represent html as nested data structure
		soup = BeautifulSoup(htmlData, 'html.parser')

		data = []
		#finding text inside all tr elements and appending into single string
		for tr in soup.find_all('tbody')[0].find_all('tr'):
			temp = []
			# Finding data in columns
			for td in tr.find_all('td'):
				temp.append(td.get_text())
			data.append(temp)
		
		# Removing head of table
		data = data[1:]


		for state_info in data:
			
			#set title and message
			notification_title = 'Update of COVID-19'
			notification_message = f"State : {state_info[0]}\nCases : {state_info[1]}\nDeaths : {state_info[2]}" 
			#call notify function
			notify(notification_title, notification_message)
			time.sleep(5)

		#to get notifications in every half an hour
		time.sleep(1800)
