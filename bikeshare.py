import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

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
    city = input("Please input City name (Chicago, New york city or Washington): ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("City is not a valid name, please input another City name: ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please input Month or all to use without filter (all, january, february, ... , june): ").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day of week or all to use without filter (all, monday, tuesday, ... sunday): ").lower()

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start_hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['Month'] == month]
   
    if day != 'all':
        df = df[df['Weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start_hour'] = df['Start Time'].dt.hour
    Month=int(df['Month'].mode().values[0])
    # TO DO: display the most common month
    print("The most common month is: {}".format(MONTHS[Month-1]))
    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(str(df['Weekday'].mode().values[0])))
    # TO DO: display the most common start hour
    print("The most common start hour: {}".format(int(df['Start_hour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Combination_Stations'] = df['Start Station'] + " " + df['End Station'] 
    
    # TO DO: display most commonly used start station
    print("The most commonly used start station is: {} ".format(df['Start Station'].mode().values[0]))
    # TO DO: display most commonly used end station
    print("The most commononly used end station is: {} ".format(df['End Station'].mode().values[0]))
    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is: {} ".format(df['Combination_Stations'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Duration'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    print("The total travel time is: {} ".format(df['Duration'].sum()))
    # TO DO: display mean travel time
    print("The mean travel time is: {} ".format(df['Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:{}".format(df['User Type'].value_counts()))
    
    # TO DO: Display counts of gender
    #city = input("Please input city name: ").lower()
    if city == 'washington':
        print("Counts of gender in Washington is currently not available")
    else: 
        Gender = df['Gender'].value_counts()
        print(Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is: {}".format(int(df['Birth Year'].min())))
        print("The most recent year of birth is: {}".format(int(df['Birth Year'].max())))
        print("The most common birth year is: {}".format(int(df['Birth Year'].mode().values[0])))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    lines = 0
    raw_data = input("Would you like to see 5 lines raw data? yes or no: ").lower()

    while True:
        if raw_data != 'no':
            print(df.iloc[lines:lines + 5])
            lines = lines + 5
            raw_data = input("Would you like to continue? yes or no: ").lower()
        else:
            break    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
