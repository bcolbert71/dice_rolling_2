#9-1. Restaurant: Make a class called Restaurant . The __init__() method for Restaurant should store two
#attributes: a restaurant_name and a cuisine_type . Make a method called describe_restaurant() that prints
#these two pieces of information, and a method called open_restaurant() that prints a message indicating that
#the restaurant is open . Make an instance called restaurant from your class . Print the two attributes
#individually, and then call both methods .
class resturant():
    """"showing a resturant."""
    def _init_(self, name, food_type)
        """establish the restaurant"""
    self.name = name.title()
    self.food_type = food_type
    def describe_resturant(self):
        """summary"""
        msg = self.name + " makes amazing " + self.food_type + "."
    def open_resturant(self):
        """message of opening"""
        msg = self.name + "come on in we are open!"
        print("\n" + msg)
resturant = resturant('Luigis', 'meatballs')
print(resturant.name)
print(resturant.food_type)
resturant.describe_resturant()
resturant.open_resturant()
exit()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the
#class, and call describe_restaurant() for each instance.
class resturant():
    """"showing a resturant."""
    def _init_(self, name, food_type)
        """establish the restaurant"""
    self.name = name.title()
    self.food_type = food_type
    def describe_resturant(self):
        """summary"""
        msg = self.name + " makes amazing " + self.food_type + "."
    def open_resturant(self):
        """message of opening"""
        msg = self.name + "come on in we are open!"
        print("\n" + msg)
luigis = resturant('Luigis', 'meatballs')
luigis.describe_resturant()
martys = resturant('Martys', 'burgers')
martys.describe_resturant()
villa_pizza = resturant('Villa PIzza', 'pizza')
villa_pizza.describe_resturant()

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
#and then create several other attributes that are typically stored in a user profile.
#Make a method called describe_user() that prints a summary of the user’s information.
#Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.
class user()
    """represents profile"""
    def_init_(self, first_name, last_name, username, email, location):
        """initializing"""
        self.first_name = first_name.title()
        Self.last_name = last_name.title()
        self.username = username
        self.email = email
    def describe_user(selfself):
        """summary"""
        print("\n + self.first_name + " " + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.email)
    def greet_user(self)
        """personal gretting"""
        print("/nice to have you back, " + self.username + "!")
bryson = user ('bryson', 'colbert', 'bcolb', 'bcolbert01@aurora.edu')
bryson.describe_user()
bryson.greet_user()

#9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
#Add an attribute called number_served with a default value of 0.
#Create an instance called restaurant from this class. Print the number of customers the restaurant has
#served, and then change this value and print it again. Add a method called set_number_served() that lets you
#set the number of customers that have been served. Call this method with a new number and print the value again.
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been
#served. Call this method with any number you like that could represent how many customers were served in,
#say, a day of business.
class resturant():
    """"showing a resturant."""
    def _init_(self, name, food_type)
        """establish the restaurant"""
    self.name = name.title()
    self.food_type = food_type
    def describe_resturant(self):
        """summary"""
        msg = self.name + " makes amazing " + self.food_type + "."
    def open_resturant(self):
        """message of opening"""
        msg = self.name + "come on in we are open!"
        print("\n" + msg)
    def set_number_served(self, additional_served):
        """number of customers that have been served"""
        self.number_served = number_served
    def additional_number_served(self, additional_served):
        """number of additional customers served"""
        self.number_served + additional_served
resturant = resturant('luigis', 'meatballs')
resturant.describe_resturant()
print("\nNumber served: " + str(resturant.number_served))
resturant.number_served = 0
print("Number served: " + str(resturant.number_served))
resturant.set_number_served(2347)
print("Number served " + str(resturant.number_served))
resturant.additional_number_served(384)
print("Number served " + str(resturant.number_served))

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
#Write a method called increment_ login_attempts() that increments the value of login_attempts by 1.
#Write another method called reset_login_attempts() that resets the value of login_ attempts to 0.
#Make an instance of the User class and call increment_login_attempts() several times.
#Print the value of login_attempts to make sure it was incremented properly,
#and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class user()
    """represents profile"""
    def_init_(self, first_name, last_name, username, email, location):
        """initializing"""
        self.first_name = first_name.title()
        Self.last_name = last_name.title()
        self.username = username
        self.email = email
    def describe_user(selfself):
        """summary"""
        print("\n + self.first_name + " " + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.email)
    def greet_user(self)
        """personal gretting"""
        print("/nice to have you back, " + self.username + "!")
    def increment_login_attempts(self):
        """value of login attempts."""
        self.login_attempts + 1
    def reset_login_attempts(self):
        """reset login_attempts to 0"""
        self.login_attemts = 0
bryson = user ('bryson', 'colbert', 'bcolb', 'bcolbert01@aurora.edu')
bryson.describe_user()
bryson.greet_user()
print("\nMaking 2 login attempts...")
bryson.increment_login_attempts()
bryson.increment_login_attempts()
print(" login attemtps: " + str(bryson.login_attempts))

#9-6.Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
#Write a class called IceCreamStand that inherits from the Restaurant class you
#wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of the class will work;
#just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
#Write a method that displays these flavors . Create an instance of IceCreamStand, and call this method.
class resturant():
    """"showing a resturant."""
    def _init_(self, name, food_type)
        """establish the restaurant"""
    self.name = name.title()
    self.food_type = food_type
    def describe_resturant(self):
        """summary"""
        msg = self.name + " makes amazing " + self.food_type + "."
    def open_resturant(self):
        """message of opening"""
        msg = self.name + "come on in we are open!"
        print("\n" + msg)
    def set_number_served(self, additional_served):
        """number of customers that have been served"""
        self.number_served = number_served
    def additional_number_served(self, additional_served):
        """number of additional customers served"""
        self.number_served + additional_served
class IceCreamStand(resturant)
    """represents to ice cream stand"""
    def _init_(self, name, food_type= 'ice cream'):
        """initializing"""
        super()._init_(name, food_type)
        self.flavors =[]
    def show_flavors(self):
        """the different flavors"""
        print("\nWe have these great flavors available:")
    for flavor in self.flavors:
        print("-" + flavor.title())
big_tonys= IceCreamStand('Big TOnys')
big_tonys.flavors = ['chocolate', 'rocky road', 'vanilla', 'strawberry']
big_tonys.descroibe_resturant()
big_tonys.show_flavors()

#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the
#User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171).
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post",
#"can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of
#privileges. Create an instance of Admin, and call your method.
class user()
    """represents profile"""
    def_init_(self, first_name, last_name, username, email):
        """initializing"""
        self.first_name = first_name.title()
        Self.last_name = last_name.title()
        self.username = username
        self.email = email
    def describe_user(selfself):
        """summary"""
        print("\n + self.first_name + " " + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.email)
    def greet_user(self)
        """personal gretting"""
        print("/nice to have you back, " + self.username + "!")
    def increment_login_attempts(self):
        """value of login attempts."""
        self.login_attempts + 1
    def reset_login_attempts(self):
        """reset login_attempts to 0"""
        self.login_attemts = 0
class admin(user):
        """administrative privileges"""
        def _init_(self, first name, last name, username, email):
        """initializing"""
        super()._init_(first name, last name, username, email):
        self.privileges = []
        def show_privileges(self):
            """privileges of admin"""
            print("\nPrivileges:")
            for privilege in self.privileges:
                print("-" + privilege)
bryson = user ('bryson', 'colbert', 'bcolb', 'bcolbert01@aurora.edu')
bryson.describe_user()
bryson.privileges = ['can add posts',
                     'can delete posts',
                     'can ban other users']
bryson.show_privileges()

#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges,
#that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this
#class. Make a Privileges instance as an attribute in the Admin class.
#Create a new instance of Admin and use your method to show its privileges.
class user()
    """represents profile"""
    def_init_(self, first_name, last_name, username, email):
        """initializing"""
        self.first_name = first_name.title()
        Self.last_name = last_name.title()
        self.username = username
        self.email = email
    def describe_user(selfself):
        """summary"""
        print("\n + self.first_name + " " + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.email)
    def greet_user(self)
        """personal gretting"""
        print("/nice to have you back, " + self.username + "!")
    def increment_login_attempts(self):
        """value of login attempts."""
        self.login_attempts + 1
    def reset_login_attempts(self):
        """reset login_attempts to 0"""
        self.login_attemts = 0
class admin(user):
        """administrative privileges"""
        def _init_(self, first name, last name, username, email):
        """initializing"""
        super()._init_(first name, last name, username, email):
        self.privileges = Privileges()
class privivleges():
    """privileges of admin"""
    def_init_(self, privileges+[])
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privileges in self.privileges:
                print("-" + privilege)
        else:
            print("-this user does not have any privileges.")
bryson = user ('bryson', 'colbert', 'bcolb', 'bcolbert01@aurora.edu')
bryson.describe_user()
bryson.privileges.show_privivleges()
print("\nAdding these privileges to user...")
bryson.privileges = ['can add posts',
                     'can delete posts',
                     'can ban other users']
bryson.show_privileges()

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
#Add a method to the Battery class called upgrade_battery(). This method should check the battery size
#and set the capacity to 85 if it isn’t already. Make an electric car with a default battery size,
#call get_range() once, and then call get_range() a second time after upgrading the battery.
#You should see an increase in the car’s range.
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        """upgrade to battery"""
        if self.battery_size == 65
            self.battery_size = 85
            print("upgrade the battery to 85.")
        else:
            print("the battery was upgraded.")
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
#Make a separate file that imports Restaurant.
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is
#working properly.
class resturant():
    """"showing a resturant."""
    def _init_(self, name, food_type)
        """establish the restaurant"""
    self.name = name.title()
    self.food_type = food_type
    def describe_resturant(self):
        """summary"""
        msg = self.name + " makes amazing " + self.food_type + "."
    def open_resturant(self):
        """message of opening"""
        msg = self.name + "come on in we are open!"
        print("\n" + msg)
    def set_number_served(self, additional_served):
        """number of customers that have been served"""
        self.number_served = number_served
    def additional_number_served(self, additional_served):
        """number of additional customers served"""
        self.number_served + additional_served

#9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
#Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance,
#and call show_privileges() to show that everything is working correctly.
class user()
    """represents profile"""
    def_init_(self, first_name, last_name, username, email):
        """initializing"""
        self.first_name = first_name.title()
        Self.last_name = last_name.title()
        self.username = username
        self.email = email
    def describe_user(selfself):
        """summary"""
        print("\n + self.first_name + " " + self.last_name)
        print(" username: " + self.username)
        print(" email: " + self.email)
    def greet_user(self)
        """personal gretting"""
        print("/nice to have you back, " + self.username + "!")
    def increment_login_attempts(self):
        """value of login attempts."""
        self.login_attempts + 1
    def reset_login_attempts(self):
        """reset login_attempts to 0"""
        self.login_attemts = 0
class admin(user):
        """administrative privileges"""
        def _init_(self, first name, last name, username, email):
        """initializing"""
        super()._init_(first name, last name, username, email):
        self.privileges = Privileges()
class privivleges():
    """privileges of admin"""
    def_init_(self, privileges+[])
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privileges in self.privileges:
                print("-" + privilege)
user import admin
bryson = user ('bryson', 'colbert', 'bcolb', 'bcolbert01@aurora.edu')
bryson.describe_user()
bryson.privileges.show_privivleges()
print("\nAdding these privileges to user...")
bryson.privileges = ['can add posts',
                     'can delete posts',
                     'can ban other users']
bryson.show_privileges()
    print("\nThe admin " + bryson.username + " has these privileges: ")
    bryson.privileges.show_privileges()

#9-14. Dice: The module random contains functions that generate random numbers in a variety of ways.
# The function randint() returns an integer in the range you provide.
# The following code returns a number between 1 and 6:Make a class Die with one attribute called sides,
#which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and
# the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a
# 20-sided die. Roll each die 10 times.
from random import randint
x = randint(1, 10)
from random import randint
class die():
    """a die that can be rolled"""
    def _init_(self, sides = 6):
    """initializing"""
    return randint(1, self.sides)
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6 sided die: ")
print(results)
d10 = Die(sides = 10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10 sided die: ")
print(results)
d20 = Die(sides = 20)
results = []
for roll_num in range(10)
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20 sided die.")
print(results)

