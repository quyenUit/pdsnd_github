import time
import pandas as pd
import numpy as np
# handling and manipulating dates
import calendar as cal 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please select a city you would like to explore (Chicago, New York City, Washington):\n").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid city name. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please specify a month (January, February, March, April, May, June) or 'all':\n").strip().lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        print("Invalid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select a day of the week you want to know about (eg Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or 'all':\n").strip().lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        print("Invalid day. Please try again.")

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday

    if month != 'all':
        month_names = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = month_names.index(month) + 1
        df = df[df['Month'] == month_num]

    if day != 'all':
        day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_num = day_names.index(day)
        df = df[df['Day of Week'] == day_num]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel.\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print(f"Most common month: {cal.month_name[most_common_month]}")


    # TO DO: display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print(f"Most common day: {cal.day_name[most_common_day]}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print(f"Most common start hour: {most_common_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip.\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {start_station}")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + " to " + df['End Station']
    most_frequent_trip = df['Station Combination'].mode()[0]
    print(f"Most frequent trip: {most_frequent_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration.\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600
    print(f"Total travel time: {total_duration:.2f} hours")

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean() / 60
    print(f"Average trip duration: {mean_duration:.2f} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats.\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print("\nGender Breakdown:")
        print(gender_counts)

        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print("\nBirth Year Stats:")
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {latest_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print("No gender or birth year data for Washington.")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Allows users to view raw data 10 rows at a time."""
    i = 0
    while True:
        view_data = input("Would you like to see 5 rows of raw data? Enter yes or no: ").lower()
        if view_data == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        else:
            break
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration.\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600
    print(f"Total travel time: {total_duration:.2f} hours")

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean() / 60
    print(f"Average trip duration: {mean_duration:.2f} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
