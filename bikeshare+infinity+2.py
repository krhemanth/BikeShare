
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().magic('matplotlib inline')


# In[ ]:


import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
	print('Hello! Let\'s explore some US bikeshare data!\n')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
	global city
	city = input("Enter the city name that you want to analyse data Chicago, New york city, Washington?\n\n").lower()
	while True:
		if city not in ["chicago", "new york city", "washington", "exit"]:
			city = input("Please check the spelling and try again. or type exit to leave the programme else Enter the city name that you want to analyse data Chicago, New york city, Washington?\n\n").lower()
		elif city == "exit":
			break
		else:
			return ('you have selected:'+ city.title()+'\n' )
			break
            
def get_month():
	global month
	month = input("Select a month from January, February, March, April, May, June or \'All\' to apply no filter\n").title()
	while True:
		if month not in ["January", "February", "March", "April", "May", "June","All"]:
			month = input("please select a month from above mentioned months in that format\n")
		else:
			return ('you have selected:' + month.title() + '\n')
			break
def get_day():
	global day
	day = input("Select any day eg.Monday or \'All\' to apply no filter\n").title()
	while True:
		if day not in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","All"]:
			day = input("please select a day from above mentioned days in that format\n")
		else:
			return('you have selected:' + day.title() + '\n')
			break

print(get_filters())
print(get_month())
print(get_day())
df = pd.read_csv(CITY_DATA[city])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.strftime('%B')
df['day'] = df['Start Time'].dt.strftime('%A')
df['hour'] = df['Start Time'].dt.hour
if month!='All':
	df = df[df['month'] == month]   
if day!='All':
	df = df[df['day'] == day]
df.dropna()
df.head(10)

def popular_month(city):
 #get month names immediately
	popular_month = df['month'].mode()[0]
	return(popular_month)
print("The most frequent month when people take bike is "+popular_month(city)+"\n")

def popular_day(city):
#get days immediately
	popular_day = df['day'].mode()[0]
	return(popular_day)
print("The busiest day of the month when people take bike is "+popular_day(city)+"\n")

def popular_hour(city):
	popular_hour = df['hour'].mode()[0]
	return(popular_hour)
print("The Rush hour of the day is "+str(popular_hour(city))+":00hrs"+"\n")

def trip_duration2(city, month, day):
	total = np.sum(df['Trip Duration'])
	total3 = (total//3600)
	return (total3)
print("Total hours of all the trips of the day "+str(trip_duration2(city, month, day))+"hrs"+"\n")
def trip_duration1(city, month, day):
	average = np.average(df['Trip Duration'])
	average = (average/60)
	return (average)
print("Average hours of all the trips of the day "+str(trip_duration1(city, month, day))+"min"+"\n")
def popular_stations(city, month, day):
	start_station = df['Start Station'].value_counts().idxmax()
	return (start_station)
print("The popular station where people take bike -> "+popular_stations(city, month, day)+"\n")
def popular_stations2(city, month, day):
	end_station = df['End Station'].value_counts().idxmax()
	return (end_station)
print("The popular station where people drop the bike -> "+popular_stations(city, month, day)+"\n")
def popular_trip(city, month, day):
    #start_station = df['Start Station'].value_counts().index[0] #need station name, not a pd series output
    #end_station = df['End Station'].value_counts().index[0]
	df['trip'] = df['Start Station'].value_counts().idxmax()+ '-' + df['End Station'].value_counts().idxmax()
	trip = df['trip'].value_counts().idxmax()
	return(trip)
print("The busiest round trip of the day -> "+popular_trip(city, month, day)+"\n")
def users(city, month, day):
	user_types = df['User Type'].value_counts()
	return("Types of users travel "+"\n"+str(user_types)+"\n")
print(users(city, month, day))

def gender(city, month, day):
	while True:
		if city in ["washington"]:
			return("No gender column for this city")
			break
		else:
			gender = df['Gender'].value_counts()
			return("Count of different genders "+"\n"+str(gender)+"\n")
print(gender(city, month, day))

def birth_years(city, month, day):
	while True:
		if city in ["washington"]:
			return("No birth_years column for this city")
			break
		else:
			oldest = df['Birth Year'].min()
			youngest = df['Birth Year'].max()
			avg = df['Birth Year'].mean()
			return("Oldest user born in the year : "+ str(int(oldest)) +" Youngest user born in the year : "+ str(int(youngest))+" Average user birth year is : "+str(int(avg)))
print(birth_years(city, month, day))



def display_data():
	global data
	row = 0
	idx = 0
	while True:
		data = input("Do you want to see your city data enter \'yes\' or \'no\'.")
		if data not in ["yes", "no"]:
			print("Invalid input format")
		elif data == "yes":
			data = input("Enter how many sets you want to see in interger format"+"\n")
			row+=int(data)
			print(df[idx:row])
			idx=int(row)   
		elif data == "no":
			print("Bye");
			break
display_data()   
    


