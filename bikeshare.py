#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

"""
The City Data files must be in the correct folder to ensure retrieval
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

divider = '-'*50

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("\n")
    print(divider)
    print('Hello! Let\'s explore some US bikeshare data!')
    print(divider)

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        city = input("Which city would you like to see data for: Chicago, New York City, or Washington? ").lower()
        if city == "":
            print("Attention: A city name is required.")
        elif city not in CITY_DATA:
            print("There is no data for that city. Choose another? ")
        else:
            print(f"City chosen - \"{city.title()}\".")
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month to filter on (January-June), or leave it blank to select all months. ").lower()
        if month == "":
            print("No input entered, using \"all\"'.")
            month = 'all'
            break
        elif month not in MONTHS:
            print("Error: invalid month filter. Choose another? ")
        else:
            print(f"Month chosen - \"{month.title()}\".")
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day of the week to filter on, or leave it blank to select all days. ").lower()
        if day == "":
            print("No input entered, using \"all\"'.")
            day = 'all'
            break
        elif day not in DAYS:
            print("Error: invalid day filter. Choose another? ")
        else:
            print(f"Day chosen - \"{day.title()}\".")
            break
            
    print(divider)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print(f"Currently Loading data...")

    df = pd.read_csv(f"data/{CITY_DATA[city]}")

    # scrub to avoid encountering missing data - drop rows with date NaNs, if they exist.
    print("Currently Cleaning data...\n")
    df.dropna(subset=['Start Time', 'End Time'], inplace=True)

    # Ensure dates are in the correct format and columns to work with.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    monthIdx = MONTHS.index(month) + 1

    # Check both start and end times, in case a ride goes over midnight.
    df['Start Month'] = df['Start Time'].dt.month
    df['End Month'] = df['End Time'].dt.month

    if month != "all":
        df = df[(df['Start Month'] == monthIdx) | (df['End Month'] == monthIdx)]

    dayIdx = DAYS.index(day) + 1

    df['Start Day'] = df['Start Time'].dt.dayofweek
    df['End Day'] = df['End Time'].dt.dayofweek

    if day != "all":
        df = df[(df['Start Day'] == dayIdx) | (df['End Day'] == dayIdx)]

    df['Start Hour'] = df['Start Time'].dt.hour
    df['End Hour'] = df['End Time'].dt.hour

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print(divider)
    print('Calculating the most frequent times of travel...')
    print(divider)

    start_time = time.time()
    
    # display the most common month
    start_month_mode, end_month_mode = df[['Start Month', 'End Month']].mode().values[0]

    if start_month_mode == end_month_mode:
        print(f"The most common month for a ride was {MONTHS[start_month_mode - 1].title()}.")
    else:
        print(f"The most common month to start a ride was {MONTHS[start_month_mode - 1].title()}.")
        print(f"The most common month to end a ride was {MONTHS[end_month_mode - 1].title()}.")

    # display the most common day of week
    start_day_mode, end_day_mode = df[['Start Day', 'End Day']].mode().values[0]

    if start_day_mode == end_day_mode:
        print(f"The most common day of the week for a ride was {DAYS[start_day_mode - 1].title()}.")
    else:
        print(f"The most common day of the week to start a ride was {DAYS[start_day_mode - 1].title()}.")
        print(f"The most common day of the week to end a ride was {DAYS[end_day_mode - 1].title()}.")

    # display the most common start hour
    start_hour_mode, end_hour_mode = df[['Start Hour', 'End Hour']].mode().values[0]
    if start_hour_mode == end_hour_mode:
        print(f"The most common hour for a ride was {start_hour_mode}.")
    else:
        print(f"The most common hour to start a ride was {start_hour_mode}.")
        print(f"The most common hour to end a ride was {end_hour_mode}.")

    print("\nThis took %s seconds.\n" % (time.time() - start_time))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print(divider)
    print('Calculating the most popular stations and trip...')
    print(divider)

    start_time = time.time()

    start_station_mode, end_station_mode = df[['Start Station', 'End Station']].mode().values[0]
    
    # display most commonly used start station
    print(f"The most common station to start a ride was {start_station_mode}.")

    # display most commonly used end station
    print(f"The most common station to end a ride was {end_station_mode}.")

    # display most frequent combination of start station and end station trip
    most_common_stations = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f"The most common station combination (start to end) was {most_common_stations}.")

    print("\nThis took %s seconds.\n" % (time.time() - start_time))

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\n")
    print(divider)
    print('Calculating the Trip Duration...')
    print(divider)

    start_time = time.time()

    # display total travel time
    df['Duration'] = df['End Time'] - df['Start Time']
    total_travel_time =  df['Duration'].dt.total_seconds().sum()

    # display mean travel time
    avg_travel_time = df['Duration'].mean()

    print(f"The total travel time of all trips was {total_travel_time}")
    print(f"The mean travel time of all trips was {avg_travel_time}")

    print("\nThis took %s seconds.\n" % (time.time() - start_time))

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print(divider)
    print('Calculating the User Stats...')
    print(divider)
    
    start_time = time.time()

    # Display counts of user types
    print("-- The user type values: ")
    # print(counts)
    for label, count in df['User Type'].value_counts().items():
        print(f"{label}: {count}")
        
    # Display counts of gender
    if 'Gender' in df:

        print("\n-- The gender values: ")
        for index, count in df['Gender'].value_counts().items():
            print(f"{index}: {count}")

        print("\n")
    else:
        print('\n')
        print(f"The Gender is not available for this city.")
    
        # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        print("\n-- The birth values: ")
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])

        print(f"The earliest birth year is {earliest}.")
        print(f"The most recent birth year is {most_recent}.")
        print(f"The most common birth year is {common_year}.")
    else:
        print('\n')
        print(f"The Birth Year is not available for this city.")
    
    print("\nThis took %s seconds.\n" % (time.time() - start_time))

def see_raw_data(df):
    """Asks if the user wants to see the raw data in increments of 5"""

    confirm = input('\nWould you like to see the raw data? ')
    row_offset = 0
    row_step = 5

    while True:
        if confirm.lower() not in ['yes', 'y', 'yeah', 'yup']:
            break
        else:
            print(df.iloc[row_offset:row_offset + row_step])
            row_offset += row_step
            confirm = input('\nWould you like to see more of the raw data? ')

def main():
    while True:

        try:

            # query for user input
            city, month, day = get_filters()

            df = load_data(city, month, day)

            # # run some analysis
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            see_raw_data(df)
            
            # restart the process if the user wants to continue
            restart = input('\nWould you like to run this again?\n')

            if restart.lower() not in ['yes', 'y', 'yeah', 'yup']:
                print('Analysis complete.')
                break
        except KeyboardInterrupt:
            print('\n')
            print(divider)
            print("Goodbye!")
            print(divider)
            break
        except Exception as e:
            print(e)
            print('An Error occurred. Try again')
            break

if __name__ == "__main__":
    main()


# In[ ]:




