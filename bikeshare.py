#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months={'0':'all','1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December' }

Days={'0':'all','1':'monday','2':'tuesday','3':'wednesday','4':'thursday','5':'friday','6':'saturday','7':'sunday'}

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze and explore .

    Returns:
        (str) city - name of the city to analyze and explore
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    city,month,day=None,None,None
    
    while (True):
        city=input ("enter your city : " )
        if city in CITY_DATA :
            break 
        else :
            print("worng input city")
    while (True):
        month=input ("enter the number of month between '1..12' or 0=all : " )
        if month in Months :
            break   
        else :
            print("worng input month")
    while (True):
        day=input ("enter the number of day between1..7 '1=monday'or 0=all : " )
        if day in Days :
            break   
        else :
            print("worng input day")         
    return city,month,day


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable .

    Args:
        (str) city - name of the city to analyze and explore
        (str) month - name of the month to filter by, or "all" to apply no month filter 
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day if applicable 
    """
    df=pd.read_csv(CITY_DATA [city])
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'] ,errors='coerce',format='%Y-%m-%d %H:%M:%S')
    # TO DO: display the most common month
    print ('the most common month is :{} '.format(df['Start Time'].dt.month.value_counts().index[0]))
   
    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    print ('the most commonstart hour is :{} '.format(df['Start Time'].dt.hour.value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('the most commonly used start station is :{} '.format(df['Start Station'].value_counts().index[0]))

    # TO DO: display most commonly used end station
    print ('the most commonly used end station is :{} '.format(df['End Station'].value_counts().index[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print ('the most most frequent combination of start station and end station trip is :{} '.format( pd.crosstab(df['Start Station'],df['End Station']).stack().index[np.argmax(pd.crosstab(df['Start Station'],df['End Station']).values)]))

   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('the total travel time is  :{} Seconde'.format(df['Trip Duration'].sum()))
    # TO DO: display mean travel time
    print ('the mean travel time is  :{} Seconde'.format(df['Trip Duration'].mean()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('we have :{} type of user'.format(df['User Type'].unique().size))
    print ('we have :{} user'.format(df['User Type'].count()))
    # TO DO: Display counts of gender
    print ('we have :{} type of Gender'.format(df['Gender'].unique().size))
    print ('we have :{} Gender'.format(df['Gender'].count()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print ('the earlist year of birth is :{} '.format(df['Birth Year'].min()))
    print ('the most recent year of birth is :{} '.format(df['Birth Year'].max()))
    print ('the most common year of birth is :{} '.format(df['Birth Year'].value_counts().index[0]))

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


# In[ ]:




