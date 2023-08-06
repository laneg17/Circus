#Lane Gingras
#Created on: November 15, 2017
#File name: LaneGingras_Circus
#Description: You're visiting Lane's amusement park where you get to draw shapes and go on an elevator. What a park. 

import time
import random 
import os 

#main
#acts as the hub of the program, and let's players navigate to different methods (attractions)
#Variable descriptions:
#welcomeString - when first opening the game and after returning from an attraction a string is chosen from a selection to welcome back the player
#navigation    - holds the user inputted number, this is used in ifs deciding what method to call
def main ():
  welcomeString = randomWelcome ()
  navigation = ""
  
  while (navigation != "5"):
    #Navigation checkpoint
    while (navigation != "1" and navigation != "2" and navigation != "3" and navigation != "4" and navigation != "5"):
      navigation = requestString (welcomeString) 
    
    if (navigation != "5"):
      if (navigation == "1"):#draw shapes
        drawShapes ()
      elif (navigation == "2"):#elevator ride
        elevator()
      elif (navigation == "3"):#photo magic show
        photoManipulation ()
      elif (navigation == "4"):#credits
        welcomeString = ("Created by Lane Gingras\n\nSpecial Thanks to:\nMr. Radue\nMr. Timms\nMr. Osborne\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park") 
            
      if (navigation != "4"):#if credits wasn't selected then refresh the random welcome back
        welcomeString = randomWelcomeBack()
      navigation = ""#resets navigation, if this wasn't here it will skip the error check loop that the navigation is requested in 


###########################################################################################################################################################################


#randomWelcome
#randomly selects between 2 strings to welcome the player upon intial loading
def randomWelcome ():
  selection = random.randint (1,2)
  
  if (selection == 1):
    return  "Welcome to Lane's Amusement park!\nPlease enjoy your stay, and parents, be sure not to lose sight of your children in this busy plaza!\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park"
  elif (selection == 2):
    return  "Welcome to Lane's Amusement park!\nPlease keep your hands and feet inside the rides at all time as we are not liable!\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park"


###########################################################################################################################################################################


#randomWelcomeBack
#randomly selects between 3 string to welcome the play back from an attraction
def randomWelcomeBack ():
  selection = random.randint (1,3)
  
  if (selection == 1):
    return  "Yes I'll have a side of fries please - oh welcome back! Where to next?\nI'll have a medium root beer with that too please.\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park"
  elif (selection == 2):
    return  "Welcome back! Have you tried the elevator yet?\nI had it built in less than 2 weeks because I was so excited to open it to the public!\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park"
  elif (selection == 3):
    return  "I wonder what happens if they enter a float for the colour range...\nOh sorry didn't see you there, ignore my rambling. Where to next?\n\nNavigation:\n1 - Draw Shapes [10/10 'My kid lost his first tooth at this attraction!']\n2 - Lane's Elevator Ride ['It was definitely an elevator!']\n3 - Photo Manipulation\n4 - Credits\n5 - Leave Park"

###########################################################################################################################################################################
  
  
#drawShapes 
#Variable descriptions:
#canvas             - empty picture
#canvasWidth        - user defined canvas width value 
#canvasHeight       - user defined canvas height value
#redRange           - user defined range the red value can become for the shape colour drawn in the canvas
#greenRange         - user defined range the green value can become for the shape colour drawn in the canvas
#blueRange          - user defined range the blue value can become for the shape colour drawn in the canvas
#rangePass          - if the user enters a range that follows proper format it will leave the loop
#rangeIntFail       - this is used to check if the user entered any character that isn't a number or a dash
#delay              - user defined delay between drawn ovals
#shape              - user defined shape to be drawn in the canvas
#width              - width of the drawn shape
#height             - height of the drawn shape
#drawLimit          - different for square and oval, sets the limit to how far they need to draw before starting to get smaller
#red0,green0,blue0  - the first number entered in the range from 'colour'Range, used for error checking
#red1,green1,blue1  - the second number entered in the range from 'colour'Range, used for error checking
def drawShapes ():
  #Variable declaration
  canvasWidth = 1
  canvasHeight = 1
  redRange = ""
  blueRange = ""
  greenRange = ""
  rangePass = false
  rangeIntFail = false
  delay = 11
  shape = ""
  width = 1
  height = 1
  
  #asks user for canvas width and height
  canvasWidth = requestInteger ("How *wide* would you like the canvas to be?\n\nRequirements:\nMust be an *even* number\n100-1000 supported")
  while (canvasWidth % 2 != 0 or canvasWidth > 1000 or canvasWidth < 100): #error checking to make sure value is between 100 and 1000
    canvasWidth = requestInteger ("Error: Canvas width must be an even number and between 100-1000.\n\nHow *wide* would you like the canvas to be?\n\nRequirements:\nMust be an *even* number\n100-1000 supported")
  canvasHeight = requestInteger ("How *high* would you like the canvas to be?\n\nRequirements:\nMust be an *even* number\n100-1000 supported")
  while (canvasHeight % 2 != 0 or canvasHeight > 1000 or canvasHeight < 100): #error checking to make sure value is between 100 and 1000
    canvasHeight = requestInteger ("Error: Canvas height must be an even number and between 100-1000.\n\nHow *high* would you like the canvas to be?\n\nRequirements:\nMust be an *even* number\n100-1000 supported")
  
  
  #asks user to input canvas colour
  canvasColour = requestString ("What *colour* would you like the *canvas* background to be?\n\nSupported Colours:\nBlack, white, grey, red, blue, green")
  canvasColour = canvasColour.lower ()
  while (canvasColour != "black" and canvasColour != "white" and canvasColour != "red" and canvasColour != "blue" and canvasColour != "green" and canvasColour != "grey"): #error checking to make sure value is a supported colour
    canvasColour = requestString ("Error: Please choose one the supported colours.\n\nWhat *colour* would you like the *canvas* background to be?\n\nSupported Colours:\nBlack, white, red, blue, green")
    canvasColour = canvasColour.lower ()
  
  #changes color to appropriate r,g,b values based on string inputted
  if (canvasColour == 'black'):
    canvasColour = Color (0,0,0)
  elif (canvasColour == 'white'):
    canvasColour = Color (255,255,255)
  elif (canvasColour == 'red'):
    canvasColour = Color (255,0,0)
  elif (canvasColour == 'green'):
    canvasColour = Color (0,255,0)
  elif (canvasColour == 'blue'):
    canvasColour = Color (0,0,255)
  elif (canvasColour == 'grey'):
    canvasColour = Color (100,100,100)
  
  
  canvas = makeEmptyPicture (canvasWidth,canvasHeight,canvasColour)
  show (canvas)
  
  
  #sets shape starting position
  x = canvasWidth / 2 - 1
  y = canvasHeight / 2 - 1
  
  #asks user which shape they would like drawn (oval and square supported)
  shape = requestString ("What *shape* would you like drawn?\n\nSquare and Oval supported")
  while (shape.lower () != "oval" and shape.lower () != "square"):
    shape = requestString ("Error: invalid shape entered.\n\nWhat *shape* would you like drawn?\n\nSquare and Oval supported")
  
  #this sets how much each shape needs to grow to cover the whole canvas before starting to shrink
  if (shape.lower() == "oval"):
    drawLimit = -120
  elif (shape.lower() == "square"):
    drawLimit = 0
    
  
  #asks user to input red colour range
  redRange = requestString ("What would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
  while (rangePass == false):
    rangeIntFail = false
    
    if (redRange.find ("-") == -1):#error check, makes sure there is a dash
      redRange = requestString ("Error: No dash found. See format example.\n\nWhat would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
    else:    
      redRange = redRange.split('-')#splits the two numbers from either side of the dash
      red0 = redRange [0]
      red1 = redRange [1]
      
      if (len(redRange) == 2 and red0 != "" and red1 != ""):#makes sure there isn't an empty character in the list
        for counter in range (0, len(redRange [0])):
          if (ord (red0[counter:counter+1]) < 48 or ord (red0[counter:counter+1]) > 57):#makes sure a number was entered
            rangeIntFail = true
            break
        if (rangeIntFail == false):
          for counter in range (0, len(redRange[1])):
            if (ord (red1[counter:counter+1]) < 48 or ord (red1[counter:counter+1]) > 57):#makes sure a number was entered
              rangeIntFail = true
              break
        if (rangeIntFail == false):#if it passes, convert the string to an int
            redRange [0] = int(redRange[0])
            redRange [1] = int(redRange[1])
        else: 
          redRange = requestString ("Error: You entered a letter or symbol other than '-' in your range. Have a look at our format example.\n\nWhat would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      
      if (len(redRange)!=2 and rangeIntFail == false):#if there are more than 2 elements in the list then error
        redRange = requestString ("Error: More than 3 elements found in your input. See format example.\n\nWhat would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (redRange [0] < 0 or redRange [0] > 255 or redRange [1] < 0 or redRange [1] > 255 ):#makes sure the numbers entered are within 0-255
        redRange = requestString ("Error: Range can only be a max of 0-255. Why don't you take a look at our format example?\n\nWhat would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (redRange [0] > redRange [1]):#makes sure the first number in the range isn't bigger than the second
        redRange = requestString ("Error: The first number in the range cannot be bigger than the second.\n\nWhat would you like the *Red colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      else:
        rangePass = true
  
  rangePass = false
  #asks user to input green colour range
  greenRange = requestString ("What would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
  while (rangePass == false):
    rangeIntFail = false
  
    if (greenRange.find ("-") == -1):#error check, makes sure there is a dash
      greenRange = requestString ("Error: No dash found. See format example.\n\nWhat would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
    else:
      greenRange = greenRange.split('-')#splits the two numbers from either side of the dash
      green0 = greenRange [0]
      green1 = greenRange [1]
      
      if (len(greenRange) == 2 and green0 != "" and green1 != ""):#makes sure there isn't an empty character in the list
        for counter in range (0, len(greenRange [0])):
          if (ord (green0[counter:counter+1]) < 48 or ord (green0[counter:counter+1]) > 57):#makes sure a number was entered
            rangeIntFail = true
            break
        if (rangeIntFail == false):
          for counter in range (0, len(greenRange[1])):
            if (ord (green1[counter:counter+1]) < 48 or ord (green1[counter:counter+1]) > 57):#makes sure a number was entered
              rangeIntFail = true
              break
        if (rangeIntFail == false):#if it passes, convert the string to an int
            greenRange [0] = int(greenRange[0])
            greenRange [1] = int(greenRange[1])
        else: 
          greenRange = requestString ("Error: You entered a letter or symbol other than '-' in your range. Have a look at our format example.\n\nWhat would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      
      if (len(greenRange)!=2 and rangeIntFail == false):#if there are more than 2 elements in the list then error
        greenRange = requestString ("Error: More than 3 elements found in your input. See format example.\n\nWhat would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (greenRange [0] < 0 or greenRange [0] > 255 or greenRange [1] < 0 or greenRange [1] > 255 ):#makes sure the numbers entered are within 0-255
        greenRange = requestString ("Error: Range can only be a max of 0-255. Why don't you take a look at our format example?\n\nWhat would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (greenRange [0] > greenRange [1]):#makes sure the first number in the range isn't bigger than the second
        greenRange = requestString ("Error: The first number in the range cannot be bigger than the second.\n\nWhat would you like the *Green colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      else:
        rangePass = true
        
  rangePass = false
  #asks user to input blue colour range
  blueRange = requestString ("What would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
  while (rangePass == false):
    rangeIntFail = false
  
    if (blueRange.find ("-") == -1):#error check, makes sure there is a dash
      blueRange = requestString ("Error: No dash found. See format example.\n\nWhat would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
    else:
      blueRange = blueRange.split('-')#splits the two numbers from either side of the dash
      blue0 = blueRange [0]
      blue1 = blueRange [1]
      
      if (len(blueRange) == 2 and blue0 != "" and blue1 != ""):#makes sure there isn't an empty character in the list
        for counter in range (0, len(blueRange [0])):
          if (ord (blue0[counter:counter+1]) < 48 or ord (blue0[counter:counter+1]) > 57):#makes sure a number was entered
            rangeIntFail = true
            break
        if (rangeIntFail == false):
          for counter in range (0, len(blueRange[1])):
            if (ord (blue1[counter:counter+1]) < 48 or ord (blue1[counter:counter+1]) > 57):#makes sure a number was entered
              rangeIntFail = true
              break
        if (rangeIntFail == false):#if it passes, convert the string to an int
            blueRange [0] = int(blueRange[0])
            blueRange [1] = int(blueRange[1])
        else: 
          blueRange = requestString ("Error: You entered a letter or symbol other than '-' in your range. Have a look at our format example.\n\nWhat would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      
      if (len(blueRange)!=2 and rangeIntFail == false):#if there are more than 2 elements in the list then error
        blueRange = requestString ("Error: More than 3 elements found in your input. See format example.\n\nWhat would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (blueRange [0] < 0 or blueRange [0] > 255 or blueRange [1] < 0 or blueRange [1] > 255 ):#makes sure the numbers entered are within 0-255
        blueRange = requestString ("Error: Range can only be a max of 0-255. Why don't you take a look at our format example?\n\nWhat would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      elif (blueRange [0] > blueRange [1]):#makes sure the first number in the range isn't bigger than the second
        blueRange = requestString ("Error: The first number in the range cannot be bigger than the second.\n\nWhat would you like the *Blue colour range* to be?\n\nFormat example (without the quotes): '5-100'\nMax range 0-255")
      else:
        rangePass = true
  
  
  #asks user how long the delay between making another shape should be
  delay = requestNumber ("How long would you like the *delay* between shapes drawn to be?\n\n0-10 seconds supported")
  while (delay < 0 or delay > 10):
    delay = requestNumber ("Error: The delay may only be 0-10 seconds.\n\nHow long would you like the *delay* between shapes drawn to be?\n\n0-10 seconds supported")
  
  
  #The shapes will get bigger with the canvas reshreshing based on user inputted delay
  while (x >= drawLimit or y >= drawLimit):
    if (redRange[0] == redRange [1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      r = int(redRange [0])
    else:
      r=random.randrange(int(redRange[0]), int(redRange[1]))
    if (greenRange[0] == greenRange [1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      g = int(greenRange[0])
    else:
      g=random.randrange(int(greenRange[0]), int(greenRange[1]))
    if (blueRange[0] == blueRange[1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      b = int(blueRange[0])
    else:
      b=random.randrange(int(blueRange[0]), int(blueRange[1]))
    
    #adjusts the width, height, x and y position of the shape to keep it centered
    width += 30
    height += 30
    x -= 15
    y -= 15
    
    #draws the appropriate shape
    if (shape.lower () == "oval"):
      addOvalFilled (canvas, x, y, width, height, makeColor (r,g,b))
    elif (shape.lower () == "square"):
      addRectFilled (canvas, x, y, width, height, makeColor (r,g,b))
    
    repaint (canvas)
    time.sleep (delay)
 
  #The shape getting progressivly smaller
  while (x <= canvasWidth / 2):
    if (redRange[0] == redRange [1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      r = int(redRange [0])
    else:
      r=random.randrange(int(redRange[0]), int(redRange[1]))
    if (greenRange[0] == greenRange [1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      g = int(greenRange[0])
    else:
      g=random.randrange(int(greenRange[0]), int(greenRange[1]))
    if (blueRange[0] == blueRange[1]):#if the range entered is just 1 number. ex. 255-255, then just set it to 255
      b = int(blueRange[0])
    else:
      b=random.randrange(int(blueRange[0]), int(blueRange[1]))
    
    #adjusts the width, height, x and y position of the shape to keep it centered
    width -= 30
    height -= 30
    x += 15
    y += 15
    
    #draws the appropriate shape
    if (shape.lower () == "oval"):
      addOvalFilled (canvas, x, y, width, height, makeColor (r,g,b))
    elif (shape.lower () == "square"):
      addRectFilled (canvas, x, y, width, height, makeColor (r,g,b))
      
    repaint (canvas)
    time.sleep (delay)
  #explore (canvas)
  
  
###########################################################################################################################################################################


#elevator
#This draws circles on a canvas and creates an illusion of a white platform moving down
#variable descriptions:
#canvas  - an empty picture where the empty ovals will be drawn
#x       - the x position of the oval
#y       - the y position of the oval
#r       - red value for oval colour
#g       - green value for oval colour
#b       - blue value for oval colour
#width   - the width of the oval
#height  - the height of the oval
#delay   - this holds the delay between ovals drawn to simulate how fast the elevator is moving
def elevator():
  canvas = makeEmptyPicture (500,500,white)
  show (canvas)
  
  x = -111
  y = -111
  width = 720
  height = 720
  r = 0
  g = 170
  b = 200
  
  
  #asks user how long the delay before the next circle drawn should be
  delay = requestNumber ("Welcome to Lane's famous elevator! How fast would you like it go?\n\n1-10km/h supported.")
  while (delay < 1 or delay > 10):
    delay = requestNumber ("Error: This can only go 1-10km/h.\n\nHow fast would you like it go?\n\n1-10km/h supported.")
    
  delay = 1 - ((delay + 90)/100.0)#this converts the km unit to milliseconds - 10km=0 seconds 1km=1 second
  
  for counter in range(0,360):
    if (counter % 2 == 0):#only draws an oval every other line
      addOval (canvas, x,y,width,height,makeColor(r,g,b))
    #next 4 lines adjust the circle to keep it centered
    x += 1
    y += 1
    width -= 2
    height -= 2
    if (counter >= 132 and counter <= 202):
      g = g - 2
      b = b + 2
    elif (counter >= 216 and counter <= 288):
      b = b-2
      r = r+3
    repaint (canvas)
    time.sleep (delay)
    
    
###########################################################################################################################################################################


#photoManipulation
#takes a user selected photo, makes an empty canvas the same size, and randomly places columns of the photos on the canvas without repeating any columns
#variable descriptions:
#file - user selected photo
#x    - holds the value from the list of shuffled columns
def photoManipulation ():
  file = pickAFile()
  filePos = file.rfind(".", 0, len(file))
  type = file [filePos:]
           
  if (type == ".png" or type == ".jpg"):
    file = makePicture(file)
    
    widthArray = range (0, getWidth(file))
    random.shuffle (widthArray)
    canvas = makeEmptyPicture (getWidth(file),getHeight(file),white)
  
    for column in range (0, getWidth(file)):
      x = int(widthArray [column])
      for y in range (0, getHeight(file)):
        setColor (getPixel(canvas,x,y),makeColor(getRed(getPixel(file,x,y)),getGreen(getPixel(file,x,y)),getBlue(getPixel(file,x,y))))
      repaint(canvas)
  elif (file == "None"):
    print "Cancel was selected."
  else:
    print "Oops! Did not choose a picture file. \nType is: " + type[1:]      