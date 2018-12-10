
# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot
# the first 5000 cubic numbers.
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.scatter(x_values, cubes, edgecolor= 'none', s=40)
plt.title("cubes", fontsize= 25)
plt.xlabel('value', fontsize= 15)
plt.ylabel('cube of value', labelsize= 15)
plt.tick_params(axis= 'both', lablesize = 15)
plt.show()
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
plt.scatter(x_values, cubes, edgecolor= 'none', s=40)
plt.title("cubes", fontsize= 25)
plt.xlabel('value', fontsize= 15)
plt.ylabel('cube of value', labelsize= 15)
plt.tick_params(axis= 'both', lablesize = 15)
plt.axis([0, 5100, 0, 5100**3])
plt.show()

# 15-2. Colored Cubes: Apply a colormap to your cubes plot.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
plt.scatter(x_values, cubes, edgecolor= 'none', c= cubes, cmap= plt.cm.BuGn, s=40)
plt.title("cubes", fontsize= 25)
plt.xlabel('value', fontsize= 15)
plt.ylabel('cube of value', labelsize= 15)
plt.tick_params(axis= 'both', lablesize = 15)
plt.axis([0, 5100, 0, 5100**3])
plt.show()

# 15-3.Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with plt.plot().
# To simulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values
# and rw.y_values, and include a linewidth argument. Use 5000 instead of 50,000 points.
from random_walk import Randomwalk
while true:
    rw = randomwalk(5000)
    rw.fill_walk()
    plt.figure(dpi= 130, figsize= (10, 6))
    point_numbers = list(range(rw.num_points))
    plt.point(rw.x_values, rw.y_values, linewidth = 1)
    plt.scatter(0, 0, c='blue', edgecolors ='none', s=80)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=80)
    plt.axes().get_xaxis().set_visible(false)
    plt.axes().get_yaxis().set_visible(false)
    plt.show()
    keep_running = input("make another one? (y/n): ")
    if keep_running == 'n':
        break

# 15-4. Modified Random Walks: In the class RandomWalk, x_step and y_step are generated from the same set
# of conditions. The direction is chosen randomly from the list [1, -1] and the distance from
# the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of
# your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from
# the x or y direction list.
while true:
    rw = randomwalk(5000)
    rw.fill_walk()
    plt.figure(dpi= 130, figsize= (10, 6))
    point_numbers = list(range(rw.num_points))
    plt.point(rw.x_values, rw.y_values, linewidth = 1)
    plt.scatter(0, 0, c='blue', edgecolors ='none', s=80)
    plt.scatter(rw.x_values[6], rw.y_values[8], c='blue', edgecolors='none', s=80)
    plt.axes().get_xaxis().set_visible(false)
    plt.axes().get_yaxis().set_visible(false)
    plt.show()

# 15-5. Refactoring: The method fill_walk() is lengthy. Create a new method called get_step() to determine
#  the direction and distance for each step, and then calculate the step. You should end up with two calls
# to get_step() in fill_walk(): This refactoring should reduce the size of fill_walk() and make the method
#  easier to read and understand.
x_step = get_step()
y_step = get_step()
class randomwalk():
    """generate randomwalk"""
    def_init_(self, num_points=5000)
    """attributes of rw"""
        self.num_points = num_points
        self.x_values = [2]
        self.y_values = [2]
    def get_step(self):
        """direction and distance of rw"""
        direction = choice([1,-1])
        direction = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
    def fill_step(self):
        """points in the walk"""
        while len(self.x_values) < self.num_points
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] x x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#15-6. Automatic Labels: Modify die.py and dice_visual.py by replacing the list we used to set the
#value of hist.x_labels with a loop to generate this list automatically. If you’re comfortable with
#list comprehensions, try replacing the other for loops in die_visual.py and dice_visual.py with
#comprehensions as well.
die = die()
results = [die.roll for roll_num in range(100)]
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
hist = pygal.bar()
hist.title = "results of d6 100x"
hist.x_lables = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "result"
hist.y_title = "frequency"
hist.add('d6', frequencies)

#15-7. Two D8s: Create a simulation showing what happens if you roll two eightsided dice 1000 times.
# Increase the number of rolls gradually until you start to see the limits of your system’s capabilities.
die_1 = die(8)
die_2 = die(8)
results = []
for roll_num in range(1000)
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result= die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequency.append(frequency)
hist = pygal.bar()
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "result"
hist,y_title = "frequency"
hist.add('d8 + d8', frequency)

#15-8. Three Dice: If you roll three D6 dice, the smallest number you can roll is 3 and the largest number
#  is 18. Create a visualization that shows what happens when you roll three D6 dice.
die_1 = die(8)
die_2 = die(8)
die_3 = die(8)
results = []
for roll_num in range(1000)
    result = die_1.roll() + die_2.roll + die_3.rol()
    results.append(result)
frequencies = []
max_result= die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results+1):
    frequency = results.count(value)
    frequency.append(frequency)
hist = pygal.bar()
hist.title = "result d8 3x roll 1000x"
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = "result"
hist,y_title = "frequency"
hist.add('d8 + d8 + d8', frequency)

#15-9. Multiplication: When you roll two dice, you usually add the two numbers together to get the result.
# Create a visualization that shows what happens if you multiply these numbers instead.
die_1 = die(8)
die_2 = die(8)
results = []
for roll_num in range(1000)
    result = die_1.roll() * die_2.roll()
    results.append(result)
frequencies = []
max_result= die_1.num_sides * die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequency.append(frequency)
hist = pygal.bar()
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "result"
hist,y_title = "frequency"
hist.add('d8 * d8', frequency)

#15-10. Practicing with Both Libraries: Try using matplotlib to make a die-rolling visualization,
# and use Pygal to make the visualization for a random walk.
die_1 = die(8)
die_2 = die(8)
results = []
for roll_num in range(1000)
    result = die_1.roll() * die_2.roll()
    results.append(result)
hist.title = "result of d8 roll 1000x"
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "result"
hist,y_title = "frequency"
