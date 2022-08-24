import turtle
import time
class Swimmer(turtle.Turtle):
    """New class Swimmers which inherits from turtle.Turtle. This class takes additional parameters
    name, gender, and age as attributes of Swimmer objects. Includes method to print
    parameters in neat, organized table, as well as redefines and augments the turtle.forward method."""
    def __init__(self, name, gender, age):
        """This function defines parameters/attribute fields of Swimmer class."""
        super().__init__()
        #name field takes user input and makes first letter capitalized, rest lower case
        self.name = name.title()
        #gender field takes user input and makes first letter capitalized, rest lower case
        self.gender = gender.title()
        self.age = int(age)

    # Method to return name, gender, and age parameters in neatly tabulated manner,
    #   which are the attributes of Swimmer objects.
    def users(self):
        return '{0:<20}{1:<20}{2:<20}'.format(self.name, self.gender, str(self.age))

    # Method inherits from turtle.forward, and takes name, gender, and age as parameters.
    #   Anytime a Swimmer object is called to move forward, it will create an 
    #   additional turtle called text. Then, the Swimmer will draw a body of water,
    #   after which, the Swimmer will change color based on the gender attribute
    #   and will swim the amount of laps equal to the age input attribute, while the text Turtle
    #   counts laps in the process and updates the counter on the screen. 
    #   Finally, the Swimmer will write "Name enjoyed his/her swim!"
    #   Though this inherits from turtle.forward method, this is notably different and rather
    #   than a distance to move forward (in pixels) being taken as a parameter, this method
    #   takes name, gender, and age instead and completely redfines the function .forward.
    def forward(self, name, gender, age):
        #create text Turtle and hide it
        text = turtle.Turtle()
        text.hideturtle()

        # fill body of water with light blue color and set draw speed
        self.fillcolor('lightblue')
        self.begin_fill()
        self.speed(8)
        text.speed(1)
        # set initial screen coordinates of Swimmer object and text Turtle object
        self.up()
        text.up()
        self.goto(-400, -200)
        text.goto(0, -148)
        self.down()

        # begin drawing water, draw waves on top of the water
        self.circle(25, 90)
        for i in range(15):
            self.seth(270)
            self.circle(25, 180)
        self.seth(270)
        self.circle(25, 90)
        self.seth(270)
        # super().forward(dist) inherits and uses turtle.forward method rather than
        #   this redefined method. draw the rest of the body of water once waves are
        #   completed.
        super().forward(200)
        self.right(90)
        super().forward(800)
        self.right(90)
        super().forward(200)
        self.end_fill()
        # move Swimmer object 50 pixels above starting point of water drawing
        #   to initial swim position
        self.up()
        self.seth(90)
        super().forward(50)
        self.right(90)
        self.down()
        # get x and y coordinates of initial swim position, add 20 to y for text that
        #   Swimmer object will write once it finishes swimming
        x = int(self.xcor())
        y = int(self.ycor() + 20)

        #if gender attribute is male, change Swimmer color to blue. if female, change to pink.
        if gender.upper() == 'MALE':
            self.color('blue')
        if gender.upper() == 'FEMALE':
            self.color('hotpink')

        # create counter for text Turtle to write lap count with
        j = 0
        # iterate through range of int(age/2) to swim one lap forward across pool
        #   and one lap back the other way across pool that amount of times   
        for i in range(int(age/2)):
            # swim across the pool
            super().forward(800)
            # add 1 to counter after each lap
            j+=1
            # clear text of previous lap counter so new counter can be written
            text.clear()
            # write lap counter on screen after each lap
            text.write(f"Lap {j}", align='center', font=('Times New Roman', 16, 'italic'))

            # swim back the other way across the pool
            self.right(180)
            super().forward(800)
            j+=1
            text.clear()
            text.write(f"Lap {j}", align='center', font=('Times New Roman', 16, 'italic'))
            self.right(180)
        # if age is odd number, Swimmer will only swim the floor of (age/2) times across
        #   and back the other way across the pool, so swim one additional lap so # of laps
        #   equals age attribute
        if age % 2 != 0:
            super().forward(800)
            j+=1
            text.clear()
            text.write(f"Lap {j}", align='center', font=('Times New Roman', 16, 'italic'))
        # move Swimmer to initial swim position (albeit 20 pixels higher) for writing final message
        self.up()
        self.goto(x, y)
        self.down()
        # alter message written by Swimmer based on gender
        if gender.upper() == 'MALE':
            self.write(f"{name.title()} enjoyed his swim!", font=('Times New Roman', 20, 'bold'))
        if gender.upper() == 'FEMALE':
            self.write(f"{name.title()} enjoyed her swim!", font=('Times New Roman', 20, 'bold'))
        # add time delay to clear entire drawing, in case Swimmers attributes are determined by user
        #   input, allowing for multiple Swimmers to function at the same time.
        time.sleep(3)
        text.clear()
        text.hideturtle()
        self.hideturtle()


def main():
    """This function takes as input from the user the name, gender, and age of a swimmer. 
    It will then add these parameters to associated lists defined below. If a user continues
    without entering any input into any field, function will stop taking input and make sure
    only complete attribute groups including all of name, gender, and age, are included in lists.
    Then, function will create turtle window, and create Swimmer objects for however many people the
    user inputted, or input groupings the user completed, and then use the .forward method from Swimmer class
    to draw Swimmers as defined in Swimmer class."""

    # initialize lists
    swimmer_names = []
    genders = []
    ages = []
    # take user input and add each parameter/value/attribute to lists
    name_input = input("Please enter your name: ")
    swimmer_names.append(name_input)
    gender_input = input("Please enter your gender: ")
    genders.append(gender_input)
    age_input = int(input("Please enter your age: "))
    ages.append(age_input)

    # will continue taking input for additional Swimmers as long as user enters information
    #   for all three fields.
    while name_input and gender_input and age_input:
        name_input = input("Please enter your name: ")
        if not name_input:
            break
        swimmer_names.append(name_input)
        gender_input = input("Please enter your gender: ")
        if name_input and not gender_input:
            swimmer_names.pop()
            break
        genders.append(gender_input)
        age_input = int(input("Please enter your age: "))
        if (name_input and gender_input) and not age_input:
            swimmer_names.pop()
            genders.pop()
            break
        ages.append(age_input)
    # create list of all Swimmers to iterate through for drawing.
    turtle_list = []
    # number of Swimmers to create
    num_turtles = len(swimmer_names)
    # print formatted header of attribute list
    print()
    print("Swimmers are:")
    print('{0:<20}{1:<20}{2:<20}'.format('Name:', 'Gender:', 'Age:'))

    #create turtle window
    wn = turtle.Screen()
    wn.bgcolor('orange')
    # create Swimmers based on number of people user inputed, add each swimmer to list
    for i in range(num_turtles):
        t = Swimmer(swimmer_names[i], genders[i], ages[i])
        print(t.users())
        turtle_list.append(t)
    # for each Swimmer in list, use swimmer.forward method using parameters name, gender, and age
    #   for each Swimmer inputted. 
    for i in range(len(turtle_list)):
        turtle_list[i].forward(swimmer_names[i], genders[i], ages[i])
        turtle_list[i].clear()
    wn.exitonclick()
# call main function
main()
