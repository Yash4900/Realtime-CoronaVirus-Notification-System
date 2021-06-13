# Realtime-CoronaVirus-Notification-System

Get updates of COVID-19 in India at regular intervals while working on your desktop :desktop_computer:. You will get notification of every state in an interval of 5 seconds. This will repeat again after 30 minutes.	

**pip install the following packages:** 

bs4 - to parse HTML data

plyer - create notifications

requests - fetch data from website

**Run python file and you will start getting notifications**

```
python covid_notification.py
```

The data is fetched from https://www.deccanherald.com/national/coronavirus-india-tracker-state-wise-covid-19-cases-deaths-on-may-22-988638.html

If the structure of HTML of this website changes then slight modifications need to be done in the code to fetch required information.

## Demo

<img src="https://github.com/Yash4900/Realtime-CoronaVirus-Notification-System/blob/master/demo.gif" />
