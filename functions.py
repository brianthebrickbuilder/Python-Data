'''
Name:           functions.py
Author:         Brian Richardson
Version:        1.0
Date:           June 20, 2021
Description:    This is the function file for lab 05
'''

import pandas as pd
import matplotlib.pylab as plt

def menu():
    '''
    Main menu
    '''
    print("\n\n************* Welcome to the Python Data Analysis App *************")

    while True:
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit")

        user_selection = menu_selection(1,3)

        if user_selection == 1:
            population_menu()
        elif user_selection == 2:
            housing_menu()
        elif user_selection == 3:
            return True

def menu_selection(lower_bounds, upper_bounds):
    '''
    User selection for menus
    '''
    pattern = "[%s-%s]"%(lower_bounds, upper_bounds)

    while True:
        user_selection = input()
        if pd.Series([user_selection], dtype = "string",).str.match(pattern).loc[0]:
            return int(user_selection)
        print("Enter a number between 1 and 3 ")

def menu_exit():
    '''
    Application exit procedures
    '''
    print("************* Thank you for using Python Data Analysis App *************")

def population_menu():
    '''
    Menu for processing population data
    '''
    menu_quit = False
    while menu_quit is False:
        print("\n\nYou have entered population data.")
        print("Select the column you want to analyze:")
        print("1. Population April 1")
        print("2. Population July 1")
        print("3. Change population")
        print("4. Exit")

        user_selection = menu_selection(1,4)

        if user_selection == 1:
            open_population_april()
        elif user_selection == 2:
            open_population_july()
        elif user_selection == 3:
            open_population_changes()
        elif user_selection == 4:
            menu_quit = True

def housing_menu():
    '''
    Menu for processing housing data
    '''
    menu_quit = False
    while menu_quit is False:
        print("\n\nYou have entered housing data.")
        print("Select the column you want to analyze:")
        print("1. Age")
        print("2. Bedrooms")
        print("3. Built")
        print("4. Rooms")
        print("5. Utility")
        print("6. Exit")

        user_selection = menu_selection(1,6)

        if user_selection == 1:
            open_housing_age()
        elif user_selection == 2:
            open_housing_bedrooms()
        elif user_selection == 3:
            open_housing_built()
        elif user_selection == 4:
            open_housing_rooms()
        elif user_selection == 5:
            open_housing_utility()
        elif user_selection == 6:
            menu_quit = True

def open_population_april():
    '''
    Opens the PopChange.csv file and loads Pop Apr 1 column
    '''
    try:
        april_data = pd.read_csv('PopChange.csv', usecols=['Pop Apr 1'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(april_data)

def open_population_july():
    '''
    Opens the PopCHange.csv file and loads Pop Jul 1 column
    '''
    try:
        july_data = pd.read_csv('PopChange.csv', usecols=['Pop Jul 1'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(july_data)

def open_population_changes():
    '''
    Opens the PopCHange.csv file and loads Change Pop column
    '''
    try:
        changes_data = pd.read_csv('PopChange.csv', usecols=['Pop Apr 1'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(changes_data)

def open_housing_age():
    '''
    Opens the Housing.csv file and loads AGE data
    '''
    try:
        age_data = pd.read_csv('Housing.csv', usecols=['AGE'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(age_data)

def open_housing_bedrooms():
    '''
    Opens the Housing.csv file and loads BEDRMS data
    '''
    try:
        bed_data = pd.read_csv('Housing.csv', usecols=['BEDRMS'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(bed_data)

def open_housing_built():
    '''
    Opens the Housing.csv file and loads BUILT data
    '''
    try:
        built_data = pd.read_csv('Housing.csv', usecols=['BUILT'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(built_data)

def open_housing_rooms():
    '''
    Opens the Housing.csv file and loads ROOMS data
    '''
    try:
        rooms_data = pd.read_csv('Housing.csv', usecols=['ROOMS'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(rooms_data)

def open_housing_utility():
    '''
    Opens the Housing.csv file and loads AGE data
    '''
    try:
        utility_data = pd.read_csv('Housing.csv', usecols=['UTILITY'])
    except FileNotFoundError:
        print('PopChange.csv not found.')

    display_column_data(utility_data)

def display_column_data(data_set):
    '''
    Takes a pandas data set and returns meta data
    '''
    print("Count = ", data_set.count()[0])
    print("Mean = ", data_set.mean()[0].round(2))
    print("Standard Deviation = ", data_set.std()[0].round(2))
    print("Min = ", data_set.min()[0])
    print("Max = ", data_set.max()[0])

    plt.hist(data_set, rwidth=4, bins="auto")
    plt.show()
    