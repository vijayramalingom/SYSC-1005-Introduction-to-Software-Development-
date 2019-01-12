"""
SYSC 1005 Fall 2017 Lab 9, Parts 2 and 3
"""

def get_points():
    """ (None) -> set of  tuples
    
    Return a set of (x, y) points, with each point stored in a tuple.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(pt1, pt2, pt3):
    sumx = pt1[0] + pt2[0]+ pt3[0]
    sumy = pt1[1] + pt2[1] + pt3[1]
    n = 3
    sumxy = (pt1[0] * pt1[1]) + (pt2[0] * pt2[1]) + (pt3[0] * pt3[1])
    sumxx = pt1[0]**2 + pt2[0]**2 + pt3[0]**2
    m = (sumx * sumy - n * sumxy) / (sumx * sumx - n * sumxx)
    b = (sumx * sumxy - sumxx * sumy ) / (sumx * sumx - n * sumxx)
    return (m, b)

def read_points(filename):
    counter = 0
    infile = open(filename, 'r')
    points = [(0,0), (0,0), (0,0)]
    for line in infile:
        numbers = line.split()
        points[counter] = float(numbers[0]), float(numbers[1])
        counter = counter + 1
    infile.close()
    return points
    
if __name__ == "__main__":
    
    [point1, point2, point3] = read_points('data.txt')

    m, b = fit_line_to_points(point1, point2, point3)

    print('the best fit line is y = ', m , 'x + ', b)
    
   

