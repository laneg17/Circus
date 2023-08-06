# Circus

**Running the Program**
1. JES 6.0 required to run [GitHub JES](https://github.com/gatech-csl/jes/releases)
2. Open LaneGingras_Circus.py with JES
3. Select "Load Program" in lower left of JES interface
4. Enter "main();" (without quotations) in console


**About the Program**

This program demonstrates different photo manipulation features of JES. A goal I had with this project was to add a framework in which to present these features, and I decided on it being an amusement park with different attractions.


**Draw Shapes**

Either a square or a circle is drawn at the center of the canvas, then it is drawn again, growing in size. This repeats until the shape fills the canvas, then it starts to draw itself smaller until it reaches the original size in the center of the canvas. The user is able to input the desired canvas size, shape, background colour, and RGB colour range of the shape itself. Every time a shape is drawn it randomizes the colour based on the RGB range the user chose.

![Alt text](/Images/LaneGingras_Image1.png?raw=true "Cover")


**Lane's Elevator Ride**

The program draws circles, starting at the outer edge of the canvas. It then continues to draw itself again, getting smaller and changing colour every time. I added this because I thought if you look at it a certain way, the white circle in the middle looks like a platform moving away from you, like an elevator.

![Alt text](/Images/LaneGingras_Image2.png?raw=true "Cover")


**Photo Manipulation**

An image is selected by the user and an appropriately sized canvas is created. The canvas starts blank, and draws the selected image 1 vertical line at a time.

![Alt text](/Images/LaneGingras_Image3.png?raw=true "Cover")
![Alt text](/Images/LaneGingras_Image4.png?raw=true "Cover")
