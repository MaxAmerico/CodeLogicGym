Objective: Calcule how much the hour of the employee is worth;
Level: extremely easy

I make it just with 4 lines code, actually I wanted to make something too hard, like this:


#############################
#Functions

def leap_year(year, month, hour, wage):
    if (year % 4 == 0 and year % 100 !=0 and month == 2) or (year % 400 == 0 and month == 2):
     return (hour*29) / wage
    elif (year % 4 != 0 and month == 2) or (year % 400 != 0 and month == 2):
     return (hour*30) / wage
     print(f'{name}, your hour is worth {}')

name = input('What is your name?:')
year = int(input('What year are you?:'))
month = int(input('What month are you?(in numbers):'))
hour = float(input('How many hours do you work per day?'))
wage = float(input('What is your wage?'))
leap_year(year, month, hour, wage)

#############################

I gave up afterwards because I spent all my mental energy...

So, I made of a easier way;


