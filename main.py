#!/bin/python3
######################################################
# Author: Aaron Quino
######################################################

# Modules imported
import turtle 
import random
import math

# Main turtle defined
t = turtle.Turtle()


# Screen created with images
s = t.getscreen()
s.setup(width=500, height=500)
s.bgpic("cartoon-wood-texture-seamless-vector-260nw-1384173404.png")
s.addshape("marty3.png")
s.addshape("cheesewedge.png")
s.addshape("mouse1.png")
t.hideturtle()

# Start screen created with text and keypress event to begin
keypress = False

  # Declares keypress as True to bypass start screen loop
def start_screen():
  global keypress
  keypress = True

  # Start screen loop
while keypress == False:
  t.penup()
  t.goto(-170, 30)
  t.pendown()
  t.write("MARTY CAT", font = ('Courier New',45, "bold"))
  t.penup()
  t.goto(-10, -20)
  t.pendown()
  t.write("Press Enter to begin", align="center", font = ('Courier New',15, "bold"))
  t.tracer(0)
  t.clear()
  s.onkey(start_screen, "Enter")
  s.listen()

# Marty dictionary created and shape associated with marty turtle
marty_dict = {"turtle": turtle.Turtle(), "radius": 50}
marty_cat = marty_dict["turtle"]
marty_cat.shape("marty3.png")

# Cheese dictionary created and shape associated with cheese turtle
cheese_dict = {"turtle": turtle.Turtle(), "radius": 30}
cheese = cheese_dict["turtle"]
cheese.shape("cheesewedge.png")

# Mouse dictionary created and shape associated with mouse turtle
mouse_dict = {"turtle": turtle.Turtle(), "radius": 1}
mouse = mouse_dict["turtle"]
mouse.shape("mouse1.png")


marty_cat.tracer(0)
cheese.tracer(0)

# Main turtles set to initial positions
mouse.hideturtle()
mouse.penup()
mouse.setx(-200)
mouse.showturtle()

cheese.hideturtle()
cheese.penup()
cheese.setheading(180)
cheese.setx(250 + marty_dict["radius"])
cheese.pendown()
cheese.showturtle()

marty_cat.hideturtle()
marty_cat.penup()
marty_cat.setheading(180)
marty_cat.setx(250 + cheese_dict["radius"])
marty_cat.pendown()
marty_cat.showturtle()

# Lives and score initialized
total_lives = 3
total_score = 0

# Main while loop for game
while total_lives != 0:  
  while True:
    t.clear()
    t.penup()
    t.goto(140,-240)
    t.pendown()
    t.write("LIVES: " + str(total_lives), font = ('Courier New',15))
    t.penup()
    t.goto(0, -240)
    t.pendown()
    t.write("SCORE: " + str(total_score), font = ('Courier New',15))
    
    # Keypress event handling function for up key
    def up():
      mouse.clear()
      current_y = mouse.ycor()
      if current_y <= 200:
        new_y = current_y + 10
        mouse.sety(new_y)
      else:
        new_y = current_y
  
    # Keypress event handling function for down key
    def down():
      mouse.clear()
      current_y = mouse.ycor()
      if current_y >= -200:
        new_y = current_y - 10 
        mouse.sety(new_y)
      else:
        new_y = current_y

    s.onkey(up, "Up")
    s.onkey(down, "Down")
    s.listen()

    # Function created to detect collision between two character objects
    def are_colliding(obj1, obj2):
      collision_detected = True;
      dx = obj1["turtle"].xcor() - obj2["turtle"].xcor()
      dy = obj1["turtle"].ycor() - obj2["turtle"].ycor()
      distance = math.sqrt((dx *dx) + (dy *dy))
      if distance < (obj1["radius"]) + (obj2["radius"]):
        return collision_detected
      else:
        return False
    
    # Marty animated
    marty_cat.clear()
    marty_cat.forward(2)
    if marty_cat.xcor() <= (-300 - marty_dict["radius"]):
      marty_cat.penup()
      marty_cat.setx(250 + marty_dict["radius"])
      marty_cat.sety(random.randint(-230 + marty_dict["radius"], 230 - marty_dict["radius"]))
      marty_cat.pendown()
    marty_cat.update()
        
    if are_colliding(marty_dict, mouse_dict) == True:
      
      break
      
    # Cheese animated
    cheese.clear()
    cheese.forward(2)
    if cheese.xcor() <= (-250 - cheese_dict["radius"]):
      cheese.penup()
      cheese.setx(250 + cheese_dict["radius"])
      cheese.sety(random.randint(-230 + cheese_dict["radius"], 230 - cheese_dict["radius"]))
      cheese.pendown()
    if are_colliding(cheese_dict, mouse_dict) == True:
      cheese.penup()
      cheese.setx(250 + cheese_dict["radius"])
      cheese.sety(random.randint(-230 + cheese_dict["radius"], 230 - cheese_dict["radius"]))
      
      # Total score increased by 100 when cheese collides with mouse
      total_score += 100
  
  # Resets Marty's position when Marty collides with mouse
  marty_cat.penup()
  marty_cat.setx(250 + marty_dict["radius"])
  marty_cat.sety(random.randint(-230 + marty_dict["radius"], 230 - marty_dict["radius"]))
  marty_cat.pendown()
  
  # Total lives deducted by 1
  total_lives -= 1
  
  # Final score, lives, and GAME OVER written to the screen
  t.clear()
  t.penup()
  t.goto(140,-240)
  t.pendown()
  t.write("LIVES: 0", font = ('Courier New',15))
  t.penup()
  t.goto(0, -240)
  t.pendown()
  t.write("SCORE: " + str(total_score), font = ('Courier New',15))
  t.penup()
  t.goto(0, 0)
  t.pendown()
  t.write("GAME OVER", align="center", font = ('Courier New',55, "bold"))

  
t.update()