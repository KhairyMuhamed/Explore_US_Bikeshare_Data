# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 03:27:34 2021

@author: laphouse
"""

# -*- coding: utf-8 -*-
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','all']
user_filters =['day','month','both','none'] 
city_filters=['chicago','new york','washington']      
days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday','all']

 
 
def get_filters():
    
    

    
    print('Hello! Let\'s explore some US bikeshare data!')    
   
 
    city = input('Would you like to see data for Chicago, New York, or Washington?\n\n')
    
    if((city.lower()) not in city_filters) :
       print('invalid option, restart program\n')
       get_filters() 
    
    elif city.lower() == 'chicago':
        city =  'chicago'
     
    elif city.lower() == 'new york' :
        city = 'new_york_city'  
     
    elif city.lower() == 'washington':
        city =  'washington'


    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n\n")
    start_loc = 0
    
    while (view_data != 'no'):
      df = pd.read_csv(CITY_DATA[city])
      print(df.iloc[start_loc:start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()
      
      
    filters = input ('would you want to filter the data by month, day, both, or not at all if none please type \'none\'\n\n')
    if((filters.lower()) not in user_filters) :
       print('invalid option, restart program\n')
       get_filters() 
    if filters.lower() == 'month' :
       month = input('Which month?  \'all\',\'january\', \'february\', \'march\', \'april\', \'may\', \'june\'\n\n')  
       if((month.lower()) not in months):
           print('invalid option, restart program\n')
           get_filters() 
       day = 'all'
       
    elif filters.lower() == 'day':
          day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday \n\n')
          if((day.lower()) not in days) :
           print('invalid option, restart program\n')
           get_filters() 
          month = 'all'
       
    elif filters.lower() == 'both':
          month = input('Which month? All, January, Febrewary, March, April, May, June\n\n')  
          day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday \n\n')
          if(((month.lower()) not in months) or (day not in days)) :
           print('invalid option, restart program')
           get_filters() 

    elif filters.lower() == 'none':
          month = 'all'
          day = 'all'
    print('-'*40)
  
    
    return city, month, day



def load_data(city, month, day):
    
    df =  pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = months.index(month)+1
        df = df[df['month'] == month]


    if day != 'all' :
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday','all']
        day = days.index(day)+1
        df = df[df['day'] == day]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)
    
    popular_day = df['day'].mode()[0]
    print('Most Popular day:', popular_day)

    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_s_station = df['Start Station'].mode()[0]
    print('Most common start station:'+most_common_s_station)

    most_common_e_station = df['End Station'].mode()[0]
    print('Most common end station:'+most_common_e_station)

  
    print('Most frequent combination of start station, and end station trip :'+most_common_s_station+", "+most_common_e_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time {total_travel_time}")

    trip_duration_mean = df['Trip Duration'].mean()
    print(f"mean travel time:{trip_duration_mean}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)
     
    if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print(gender)
  
    else:
      print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    if 'Birth Year' in df:
      youngest = df['Birth Year'].min()
      print(f"Earliest year of birth: {youngest}")
    
      oldest = df['Birth Year'].max()
      print(f"Oldest year of birth{oldest}")
    
      most_frequent = df['Birth Year'].mode()[0]
      print (f"Most common year of birth: {most_frequent}")
    else:
        print('Birth year stats cannot be calculated because Gender does not appear in the dataframe')
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
     while True:
         
       city, month, day = get_filters()
       df = load_data(city, month, day)
       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       
       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
          break
      
if __name__ == "__main__":
	main()
