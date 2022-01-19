import time
import pandas as pd
import numpy as np
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
        city = input('Please enter the city "chicago, new york city, washington"').lower()
        if city not in CITY_DATA:
            print ('Please try again and make sure your enter a valid city')
        else :
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month from january to june or all ').lower()
        months = ['january','february','march','april','may','june']
        if month != 'all' and month not in months :
            print('Please enter a correct month')
        else :
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please enter a day of week or all ').lower()
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day != 'all' and day not in days :
            print('Please enter a correct day ')
        else :
            break 
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
    df = pd.read_csv(CITY_DATA[city]) # to load th data 
    df['Start Time'] = pd.to_datetime(df['Start Time']) # to convert the time to data
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    # filter by month 
    if month != 'all':
        months =months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df =df[df['month'] == month]
    return df
def view_raw_data(df):
    """"
    Display subsequent rows of data accroding user answer 
    """
    i =0
    answer = input("W'you like to display the first 5 rows of data ? yes/no ").lower()
    pd.set_option('display.max_columns',None)
    while True:
        if answer == 'no':
            break
        #print(i:i+5)
        answer= input("W'you like to display the first 5 rows of data ? yes/no ").lower()
        i+=5
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month',common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day', common_day)
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour ',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start =df['Start Station'].mode()[0]
    print('Most common start station',common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station',common_end)
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station']+ ','+df['End Station']).mode()[0]
    print('Most frequent start and end station',common_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    Total_time = df['Trip Duration'].sum()
    print('Total time of the trip ',Total_time ,'Seconds or ',Total_time /3600,'hour')
    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('average time of the trip ',average_time ,'Seconds or ',average_time /3600,'hour')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('Count of user type \n',df['User Type'].value_counts());
    # TO DO: Display counts of gender
    if 'Gender' in df :
        print('\n Count of Gender \n',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth day' in df:
        earliest_by_year =int(df['Birth day'].min())
        print('\n Earliest year Birth day :\n ',earliest_by_year)
        recent_year =int(df['Birth day'].max())
        print('\n Most recent year Birth day :\n ',recent_year)
        common_year =int(df['Birth day'].mode()[0])
        print('\n Most common year Birth day :\n ',common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()