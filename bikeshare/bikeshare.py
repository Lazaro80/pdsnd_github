import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']  
WEEK_DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']  
    
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
    input_city = input('Please type a city to analyze (chicago, new york city, washington): ').lower()
    while(input_city not in CITIES):
        input_city = input('Please type a VALID city from the list to analyze (chicago, new york city, washington): ').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)    
    input_month = input('Please type the month (by name) up to june or type ''all'': ').lower()
    while(input_month not in MONTHS and input_month != 'all'):
        input_month = input('Please type a VALID month by name up to june. ie: ''february'': ').lower()    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    input_day = input('Please type the day of week (by name) or type ''all'': ').lower()
    while(input_day not in WEEK_DAYS and input_day != 'all'):
        input_day = input('Please type a VALID day by name. ie: ''monday'': ').lower()  
        
    print('-'*40)
    return input_city, input_month, input_day


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
    
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
    
    # TO DO: display the most common month
    print('Most common month: {mcm}'.format(mcm=df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of week: {mcd}'.format(mcd=df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common day of week: {mcs}'.format(mcs=df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common Start Station: {mss}'.format(mss=df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most common End Station: {mes}'.format(mes=df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most common Station combination: {msc}'.format(msc=(df['Start Station']+' - '+df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {ttt}'.format(ttt = df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time: {ttt:.2f}'.format(ttt = df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Number of users by their type:')
    print('{ut}\n'.format(ut = df.groupby(['User Type'])['User Type'].count()))
    
    # TO DO: Display counts of gender
    print('Number of users by their gender:')
    try:
        print('{ut}\n'.format(ut = df.groupby(['Gender'])['Gender'].count()))
    except:
        print('It is not possible to show info about gender.\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest year of birth: {by}'.format(by = int(df['Birth Year'].min())))
        print('Most recent year of birth: {by}'.format(by = int(df['Birth Year'].max())))
        print('Most common year of birth: {by}'.format(by = int(df['Birth Year'].mode())))
    except:
        print('It is not possible to show info about birth date.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    start_row = 0
    end_row = 10
    max_rows = df.shape[0]
    go = 'y'
    
    while(start_row < max_rows and go == 'y'):  
        print(start_row)
        print(df[start_row:end_row])
        start_row += 10
        end_row = start_row + 10
        if(end_row > max_rows):
            end_row = max_rows
        go = input('Print next 10 rows? (Hit ''y'' or enter to continue or ''n'' to stop): ') or 'y'

def main():
    while True:
        city, month, day = get_filters()
        #city, month, day = 'chicago','january','Monday'
        df = load_data(city, month, day)        
        time_stats(df)            
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        print_raw_data = input('\nWould you like to print raw data? Enter yes (y) or no (n).\n').lower()
        while(print_raw_data not in ['y','n']):  
            print_raw_data = input('\nWould you like to print raw data? Enter yes (y) or no (n).\n').lower()
        if(print_raw_data == 'y'):
            raw_data(df)    
               
        restart = input('\nWould you like to restart? Enter yes (y) or no (n).\n')
        if restart.lower() != 'y':
            break
       

if __name__ == "__main__":
	main()
