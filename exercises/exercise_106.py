import turtle  # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess_red = turtle.Turtle()
tess_green = turtle.Turtle()
tess_yellow = turtle.Turtle()


def create_turtles():
    tess_red.setpos(40, 40)
    tess_red.shape("circle")
    tess_red.shapesize(3)
    tess_red.fillcolor("red")
    tess_green.setpos(40, 112.5)
    tess_green.shape("circle")
    tess_green.shapesize(3)
    tess_green.fillcolor("green")
    tess_yellow.setpos(40, 185)
    tess_yellow.shape("circle")
    tess_yellow.shapesize(3)
    tess_yellow.fillcolor("yellow")


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess_red.pensize(3)
    tess_red.color("black", "darkgrey")
    tess_red.begin_fill()
    tess_red.forward(80)
    tess_red.left(90)
    tess_red.forward(200)
    tess_red.circle(40, 180)
    tess_red.forward(200)
    tess_red.left(90)
    tess_red.end_fill()


draw_housing()
tess_red.penup()
# Position tess onto the place where the green light should be
tess_red.forward(40)
tess_red.left(90)
tess_red.forward(50)
create_turtles()
# Turn tess into a big green circle
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess’ position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess_red.fillcolor(0.47, 0, 0)
        tess_yellow.fillcolor("yellow")
        tess_green.fillcolor(0.03, 0.2, 0)
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:  # Transition from state 1 to state 2
        tess_yellow.fillcolor(0.63, 0.55, 0)
        tess_red.fillcolor("red")
        tess_green.fillcolor(0.03, 0.2, 0)
        state_num = 2
        wn.ontimer(advance_state_machine, 2000)
    else:  # Transition from state 2 to state 0
        tess_yellow.fillcolor(0.63, 0.55, 0)
        tess_red.fillcolor(0.47, 0, 0)
        tess_green.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 2000)


# Bind the event handler to the space key.
wn.listen()  # Listen for events
advance_state_machine()
wn.mainloop()
