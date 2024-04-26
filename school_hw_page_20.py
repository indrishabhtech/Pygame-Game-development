import matplotlib.pyplot as plt
import math

# DDA FUNCTION FOR LINE GENERATION
def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    
    # find Absolute differences
    steps = max(abs(dx), abs(dy))
    # calculate the increment in x and y
    xinc = dx / steps
    yinc = dy / steps
    # start with first point
    x = float(x0)
    y = float(y0)
    # make a list of coordinates
    x_coordinates = []
    y_coordinates = []
    
    for i in range(steps):
        # append the x, y coordinates in respective list
        x_coordinates.append(x)
        y_coordinates.append(y)
        
        # increment the values
        x = x + xinc
        y = y + yinc
        
    # plot the line with the coordinates list
    plt.plot(x_coordinates, y_coordinates)
    plt.show()

# Driver code
if __name__ == "__main__":
    # coordinates of 1st point
    x0, y0 = 20, 20
    
    # coordinates of 2nd point
    x1, y1 = 60, 50
    
    # function call
    DDA(x0, y0, x1, y1)
