# 3-1. Names: Store the names of a few of your friends in a list called names .
# Print each person’s name by accessing each element in the list, one at a time .
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
)message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
names = ['Colton', 'Josh', 'Emilie', 'Luke']
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print (names[4])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
# print a message to them . The text of each message should be the same, but each message should be personalized
#  with the person’s name .
names = ['Colton', 'Josh', 'Emilie', 'Luke']
msg = "Hello, " + names[0].tilte() +"!"
print(msg)
msg = "Hello, " + names[1].tilte() +"!"
print(msg)
msg = "Hello, " + names[2].title() +"!"
print(msg)
msg = "Hello, " + names[3].tiles() +"!"
print(msg)

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples . Use your list to print a series of statements about these items,
#  such as “I would like to own a Honda motorcycle .”
cars = ['charger', 'challenger', 'jeep', 'BMW']
msg = "I would like to own a, " + cars(0).title()
print(msg)
msg = "I would like to own a, " + cars(1).title()
print(msg)
msg = "I would like to own a, " + cars(2).title()
print(msg)
msg = "I would like to own a, " + cars(3).title()
print(msg)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
guests = ['Bill', 'George', 'Jeff', 'Albert']
name = guests[0]. title()
print(name + ", come to dinner.")
name = guests[1]. title()
print(name + ", come to dinner.")
name = guests[2]. title()
print(name + ", come to dinner.")
name = guests[3]. title()
print(name + ", come to dinner.")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations .
# You’ll have to think of someone else to invite .
# •	Start with your program from Exercise 3-4 .
# Add a print statement at the end of your program stating the name of the guest who can’t make it .
# •	Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are
# inviting .
# •	Print a second set of invitation messages, one for each person who is still in your list .
guests = ['Bill', 'George', 'Jeff', 'Albert']
name = guests[1]. title()
print("\nsorry, " + name + "can't make it to dinner.")
del(guests[1])
guests.insert(1, 'Brian')
name = guests[0]. title()
print(name + ", come to dinner.")
name = guests[1].title()
print (name + ", come to dinner. ")
name = guests[2]. title()
print(name +", come to dinner. ")
name = guests[3]. title()
print(name + ", come to dinner. ")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available .
# Think of three more guests to invite to dinner .
# •	Start with your program from Exercise 3-4 or Exercise 3-5 .
# Add a print statement to the end of your program informing people that you found a bigger dinner table .
# •	Use insert() to add one new guest to the beginning of your list .
# •	Use insert() to add one new guest to the middle of your list .
# •	Use append() to add one new guest to the end of your list .
# •	Print a new set of invitation messages, one for each person in your list .
guests = ['Bill', 'Brian', 'Jeff', 'Albert']
name = guests[1]. title()
print("\nWe found a bigger table!")
guests.insert(0, 'Jenna')
guests.insert(2, 'Emilie')
guests.append('Saige')
name = guests[0]. title()
print(name + ", come to dinner.")
name = guests[1].title()
print (name + ", come to dinner. ")
name = guests[2]. title()
print(name +", come to dinner. ")
name = guests[3]. title()
print(name + ", come to dinner. ")
name = guests[4]. title()
print(name + ", come to dinner")
name = guests[5]. title()
print(name + ", come to dinner.")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests .
#  •	Start with your program from Exercise 3-6 .
# Add a new line that prints a message saying that you can invite only two people for dinner .
# •	Use pop() to remove guests from your list one at a time until only two names remain in your list .
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry
#  you can’t invite them to dinner .
# •	Print a message to each of the two people still on your list, letting them know they’re still invited .
# •	Use del to remove the last two names from your list, so you have an empty list .
# Print your list to make sure you actually have an empty list at the end of your program .
guests = ['Jenna', 'Bill', 'Emilie', 'Brian', 'Jeff', 'Albert', 'Saige']
name = guests[0]. title()
print(name + ", come to dinner.")
name = guests[1].title()
print (name + ", come to dinner. ")
name = guests[2]. title()
print(name +", come to dinner. ")
name = guests[3]. title()
print(name + ", come to dinner. ")
name = guests[4]. title()
print(name + ", come to dinner")
name = guests[5]. title()
print(name + ", come to dinner.")
print("\nsorry, only two can come to dinner." )
name = guests.pop()
print("Sorry, " + name.title() + "there's no room at the table. ")
name = guests.pop()
print("sorry, " + name.titel() + "there's no room at the table. ")
name = guests.pop()
print("sorry, " + name.titel() + "there's no room at the table. ")
name = guests.pop()
print("sorry, " + name.title() + " there's no room at the table. ")
name = guests[0].title()
print(name + ", please come to dinner. ")
name = guests[5].title()
print(name + ", please come to dinner. ")
del(guests[0])
del(guests[0])
print(guests)

#3-8 Seeing the World: Think of at least five places in the world you’d like to visit .
# •	Store the locations in a list . Make sure the list is not in alphabetical order .
# •	Print your list in its original order . Don’t worry about printing the list neatly,
# just print it as a raw Python list .
#  •	Use sorted() to print your list in alphabetical order without modifying the actual list .
# •	Show that your list is still in its original order by printing it .
# •	Use sorted() to print your list in reverse alphabetical order without changing the order of the original list .
#  •	Show that your list is still in its original order by printing it again .
# •	Use reverse() to change the order of your list . Print the list to show that its order has changed .
# •	Use reverse() to change the order of your list again . Print the list to show it’s back to its original order .
#  •	Use sort() to change your list so it’s stored in alphabetical order .
# Print the list to show that its order has been changed . •
# Use sort() to change your list so it’s stored in reverse alphabetical order .
# Print the list to show that its order has changed .
locations = ['Fenway Park', 'Yankee Stadium', 'Florida', 'California']
print("original order:")
print(locations)
print("\nAlphabetical:")
print(sorted(locations))
print("\noriginal order:")
print(locations)
print("\nReverse Alphabetical:")
print(sorted(locations, reverse=true))
print("\noriginal order:")
print("\nreversed:")
locations.reverse()
print(locations)
print("\noriginal order:")
print(locations)
print("\nalphabetical")
locations. sort(
print(locations)
print("\nreverse alphabetical")
locations. sort(reverse=true)
print(locations)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
# use len() to print a message indicating the number of people you are inviting to dinner .
guests = ['Jenna', 'Saige']
len(guests)

#4-1. Pizzas: Think of at least three kinds of your favorite pizza .
# Store these pizza names in a list, and then use a for loop to print the name of each pizza .
# •	Modify your for loop to print a sentence using the name of the pizza instead of printing
# just the name of the pizza . For each pizza you should have one line of output containing a simple statement
#  like I like pepperoni pizza .
#  •	Add a line at the end of your program,
# outside the for loop, that states how much you like pizza .
# The output should consist of three or more lines about the kinds of pizza you like and then
# an additional sentence, such as I really love pizza!
favorite_pizza = ['Pepporoni', 'sausage', 'cheese']
for pizza in favorite pizza
    print(favorite_pizza)
print("\n")
for pizza in favorite_pizza:
    print("I really love " + pizza+ "pizza!")
print("\nI really love pizza!")

#4-2. Animals: Think of at least three different animals that have a common characteristic .
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal .
# •	Modify your program to print a statement about each animal, such as A dog would make a great pet.
# •	Add a line at the end of your program stating what these animals have in common .
# You could print a sentence such as Any of these animals would make a great pet!
animals = ['dog', 'fish', 'tiger']
for animals in animals:
    print(animal.title() + ", make a great pet!")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .
numbers = list(range(1,21))
for numbers in numbers:
    print(numbers)

#4-4. One Million: Make a list of the numbers from one to one million,
# and then use a for loop to print the numbers .
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .)
numbers = list(range(1, 1,000,001))
for numbers in numbers:
    print(numbers)

#4-5. Summing a Million: Make a list of the numbers from one to one million,
#  and then use min() and max() to make sure your list actually starts at one and ends at one million .
# Also, use the sum() function to see how quickly Python can add a million numbers .
numbers = list(range(1, 1,000,001))
print(min(numbers))
print(max(numbers))
print(max(numbers))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers
# from 1 to 20 . Use a for loop to print each number .
odd_numbers = list(range(1, 21))
print(odd_numbers)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30 .
# Use a for loop to print the numbers in your list .
threes = list(range(3, 31, 3))
for numbers in numbers:
    print(number)

#4-8. Cubes: A number raised to the third power is called a cube .
# For example, the cube of 2 is written as 2**3 in Python .
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube .
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes
    print(cube)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
cubes = [nuumber**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

#4-10. Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:
# •	Print the message, The first three items in the list are: .
# Then use a slice to print the first three items from that program’s list .
# •	Print the message, Three items from the middle of the list are: .
# Use a slice to print three items from the middle of the list .
# •	Print the message, The last three items in the list are: .
# Use a slice to print the last three items in the list .
animals = ['dog', 'fish', 'tiger']
animals.append('pig')
print("the first three items in the list are:")
print("three items from the middle of the list are:")
print("the last three items in the list are:")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) .
# Make a copy of the list of pizzas, and call it friend_pizzas .
# Then, do the following: •	Add a new pizza to the original list .
# •	Add a different pizza to the list friend_pizzas . •	Prove that you have two separate lists .
# Print the message, My favorite pizzas are:, and then use a for loop to print the first list .
# Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list .
# Make sure each new pizza is stored in the appropriate list .
favorite_pizza = ['Pepporoni', 'sausage', 'cheese']
friend_pizzas = favorite_pizza[:]
favorite_pizzas.append('bacon')
friend_pizzas.append('vegatable')

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing
# to save space . Choose a version of foods.py, and write two for loops to print each list of foods .
my favorite foods:
{'steak', 'hamburger', 'potatoes'}
my friends favorite foods:
["fish", 'tacos', 'brocoli']

#4-13. Buffet: A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple .
# •	Use a for loop to print each food the restaurant offers .
# •	Try to modify one of the items, and make sure that Python rejects the change .
# •	The restaurant changes its menu, replacing two of the items with different foods .
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on
# the revised menu.
menu_options = ('chicken nuggets', 'chicken wings', 'mac and cheese', 'vegetables', 'ice cream')
print("these are your menu options, ")
for item in menu_options:
    print("these are your menu options, " + item)
menu_options = ('chicken nuggets', 'chicken wings', 'mac and cheese', 'vegetables', 'ice cream', 'cake')
print("\nthe menu has been changed")
print("you have these new menu options, ")
for items in menu_options:
    print("these are your menu options, " + item)

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and
# your prediction for the results of each test . Your code should look something like this:
•Look closely at your results, and make sure you understand why each line evaluates to True or False
. •	Create at least 10 tests . Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
cars = ['range rover', 'audi', 'porsche', 'lamborghini', 'ferrari', 'bmw', 'cadillac', 'jeep', 'chevy', 'toyota']
car = 'audi'
car == 'audi'
car = 'audi'
cars == 'chevy'
cars = 'range rover'
cars == 'toyota'
cars = 'toyota'
cars == 'lamborghini'
cars = 'lamborghini'
cars == 'porsche'
cars = 'ferrari'
cars == 'jeep'
cars = 'jeep'
cars == 'jeep'
cars = 'lamborghini'
cars == 'lamborghini'
cars = 'cadillac'
cars == 'cadillac'
cars = 'porsche'
cars == 'porsche'

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red' .
# •Write an if statement to test whether the alien’s color is green.
# If it is, print a message that the player just earned 5 points.
# •Write one version of this program that passes the if test and another that fails.
# (The version that fails will have no output.)
alien_color = 'red'
if alien_color == 'green':
    print("you just received 5 points")
alien_color = 'green'
if alien_color == 'green':
    print("you received 5 points")

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.•If the alien’s color is green, print a statement that the player just
# earned 5 points for shooting the alien.
# •If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# •Write one version of this program that runs the if block and another that runs the else block.
alien_color = 'red'
if alien_color == 'red':
    print("you received 5 points")
else:
    print("you received 10 points")
alien_color = 'yellow'
if alien_color == 'green'
    print("you received 5 points")
else:
    print("you received 10 points")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •If the alien is green, print a message that the player earned 5 points.
# •If the alien is yellow, print a message that the player earned 10 points.
# •If the alien is red, print a message that the player earned 15 points.
# •Write three versions of this program, making sure each message is printed for the appropriate color alien.
alien_color = 'red'
if alien_color == 'yellow'
    print("you received 5 points")
elife alien_color == 'green'
    print("you received 10 points")
else:
    print("you received 15 points")

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
# Set a value for the variable age, and then:
# •If the person is less than 2 years old, print a message that the person is a baby.
# •If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# •If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# •If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# •If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# •If the person is age 65 or older, print a message that the person is an elder.
age = 21
if age < 2:
    print("you are a baby")
elif age < 4:
    print("then you're a toddler")
elif age < 13:
    print("then you're a kid")
elif age < 20:
    print("then you're a teenager")
elif age < 65:
    print("then you're an adult")
else:
    print("then you're an elder")

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if
# statements that check for certain fruits in your list.
# •Make a list of your three favorite fruits and call it favorite_fruits.
# •Write five if statements . Each should check whether a certain kind of fruit is in your list.
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!
favorite_fruits = ['strawberries', 'apples', 'oranges']
if 'strawberries' in favorite_fruits:
    print("I like strawberries")
if 'apples' in favorite_fruits:
    print("I like apples")
if 'oranges' in favorite_fruits:
    print("I like oranges")
if 'pineapple' in favorite_fruits:
    print("I like pineapple")
if 'grapefruit' in favorite_fruits:
    print("I like grapefruit")

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user: •If the username is 'admin',
# print a special greeting, such as Hello admin, would you like to see a status report?
# •Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
usernames = ['Bryson', 'Mike', 'Jenna', 'Colton', 'Saige']
for username in usernames:
    if username == 'admin'
        print("hello admin, would you like to see a status report?")
    else:
        print("Hello" + username + ", nice to see you again!"

#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
    # •If the list is empty, print the message We need to find some users!
    # •Remove all of the usernames from your list, and make sure the correct message is printed.
username[]
if usernames:
    for usernames in username:
        if username == 'admin'
            print("Hello admin, would you like a status report?")
        else:
            print("Hello" + username + ", nice to see you again!")
else:
    print("we need to find some users!")

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that
#everyone has a unique username.
#•Make a list of five or more usernames called current_users.
#•Make another list of five usernames called new_users . Make sure one or two of the new usernames are
#also in the current_users list.•Loop through the new_users list to see if each new username has
#already been used. If it has, print a message that the person will need to enter a new username.
#If a username has not been used, print a message saying that the username is available.
#•Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
current_users = ['John', 'Brian', 'Jeff', 'Mike', 'Ron']
new_users = ['Emilie', 'Jenna', 'Saige', 'Elle']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user_lower() in current_users_lower:
        print("sorry" + new_user + ", that name is already being used")
    else:
        print("good, " + "you can still use this name!")

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
#Most ordinal numbers end in th, except 1, 2, and 3. •Store the numbers 1 through 9 in a list.
#•Loop through the list . •	Use an if-elif-else chain inside the loop to print the proper ordinal ending
#for each number . Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
#and each result should be on a separate line .
number = (range(1,10))
for numbers in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
