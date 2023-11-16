import random
def generateRandomPointsWithTrend(line, count, tolerance):
    """
    This function returns a list of XY-Coordinate pairs. 
    The parameters are used to generate random numbers.
        - line is a string that represents the right half of an
          equation. The value of line is used to create a linear
          equation. When this string is substitued into the eval 
          function, the eval function converts the text in line into
          actual code.
        - count is the number of XY-Coordinate pairs in the list.
        - tolerance is used to adjust how close the random numbers
          are to the equation line.
          
    The structure of the generated list should be [x1, y1, x2, y2, x3, y3]
    where the values in the list are all integers.
    """
    points = []
    random.seed(int(input("Seed: ")))
    for i in range(count):
        x = random.randint(0, 100)
        y = eval(line) + random.randint(-tolerance, tolerance)
        points.append(str(x))
        points.append(str(y))
    return points

def printPoints(xs, ys):
    """
    This function should accept 2 parameters: xs and ys. Both of these parameters
    are lists. The lists xs and ys are parallel lists. An XY-Coordinate pair can be formed 
    by accessing values in the lists xs and ys at the same index postion. This function
    should return the table of XY-Coordinate pairs as a string. 
    Example: 
        xs = [1,1,2,3]
        ys = [1,2,3,4]
        Given the lists xs and ys the returned string should have the following structure:
        x   y
        1   1
        1   2
        2   3
        3   4
        The purpose of this function is so that the XY-Coordinate pairs could be copied and
        pasted into the website desmos.com so that you can visualize the data points.
    """
    new_string = "x\ty\n"

    for x,y in zip(xs,ys):
        new_string += f"{x}\t{y}\n"

    return new_string



def separatePointsList(points):
    """
    This function takes a single list of XY-Coordinate pairs and creates two separate
    lists. The first list should have all of the x-values from the list points. The second list 
    should have all of the y-values from the list ponits. The values in the returned lists should
    be in the same order as they are in the list points.
    Example
        points = [1, 1, 1, 2, 2, 3, 3, 4]
        xs = [1,1,2,3]
        ys = [1,2,3,4]
    """
    xs = []
    ys = []

    for i in range(len(points)):
        if ((i+1) % 2) != 0:
            xs.append(points[i])
        elif ((i+1) % 2) == 0:
            ys.append(points[i])

    return xs, ys



def computeRegression(points):
    """
    This function should compute a line of regression of the data points in the list 
    points. The list points should have the following structure [x1, y1, x2, y2, x3, y3]
    where the values in the list are all integers. To complete this function, you will need to 
    implement the two equations given above. This math may seem intmidating, but this function
    is far from the most dificult problem presented this semester. 
    - You will need to find the average of all of the x values.
    - You will need to find the average of all of the y values.
    - To compute the summations, you need to iterate over the XY-Coordinates and substitute 
      the values for the current iteration into the formula for m. The iteration is the summation!
    """

    xs, ys = separatePointsList(points)
    list_xy = []
    for i in range(len(xs)):
        xy = int(xs[i])*int(ys[i])
        list_xy.append(xy)
    sum_of_xy = sum(list_xy)


    x_squared_list = []
    for i in range(len(xs)):
        x_squared = int(xs[i])**2
        x_squared_list.append(x_squared)
    sum_of_x_squared = sum(x_squared_list)

    string_xs = []
    for i in range(len(xs)):
        b = int(xs[i])
        string_xs.append(b)
    new_xs = string_xs

    string_ys = []
    for i in range(len(ys)):
        v = int(ys[i])
        string_ys.append(v)
    new_ys = string_ys
    

    xs_average = sum(new_xs)/len(new_xs)
    ys_average = sum(new_ys)/len(new_ys)


    
    numerator = sum_of_xy - (len(xs)*xs_average*ys_average)
    denominator = sum_of_x_squared - (len(xs)*(xs_average**2))
    m = numerator/denominator

    c = ys_average - (m*xs_average)
    y1 = f"y = {m:.2f}*x {c:.2f}"

    return y1

        
    
if __name__ == "__main__":
    p = generateRandomPointsWithTrend(input("y = (enter the rest of the equation)"), int(input("Number of points")), int(input("Tolerance: ")))
    xs, ys = separatePointsList(p)
    print(printPoints(xs, ys))
    print("line of regression", computeRegression(p))
