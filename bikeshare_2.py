import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './chicago.csv',
              'new york city': './new_york_city.csv',
              'washington': './washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    print('Welcome to the bikeshare program!!!')
    # Get user input for city
    while True:
        city = input(f"First to start the program please select a city you want to explore! ({', '.join(cities)}):\n").lower()
        if city in cities:
            break
        else:
            print("Invalid city. Please try again.")

    # Get user input for month
    while True:
        month = input(f"Please choose a month ({', '.join(months)}):\n").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please try again.")

    # Get user input for day
    while True:
        day = input(f"Please choose a day of the week ({', '.join(days)}):\n").lower()
        if day in days:
            break
        else:
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # List of month names 
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'all']

    # display the most common month
    common_month_index = df['month'].mode()[0]
    common_month = month_names[common_month_index - 1]
    print(f'Most common month: {common_month}')

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most common day: {common_day}')

    # display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'Most common start hour: {common_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station: {start_station}')

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station: {end_station}')

    # display most frequent combination of start station and end station trip
    frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'Most frequent trip: from {frequent_trip[0]} to {frequent_trip[1]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f'Total travel time: {total_duration} seconds')


    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_duration:.2f} seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:')
    print(user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender:')
        print(gender_counts)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nBirth Year:')
        print(f'Earliest: {earliest_birth}, Most recent: {recent_birth}, Most common: {common_birth}')


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
