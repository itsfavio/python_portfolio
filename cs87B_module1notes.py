'''This is a small program I wrote to verify my computation for my calc 3 class, as I had to find the dot product, magnitude and angle of vectors. It's very simple and example of object oriented programming.
'''
Spyder Editor
"""
from numpy import arccos, rad2deg

class Point:
    
    def __init__(self, x= 0, y=0):
        '''the double underscore 'hides' this method 
        from the outside code '''
        
        self.x = x
        self.y = y
       
        return
        
def mag(tree):
    ''' return the magnitude of the vector'''
    return (( (tree.x)**2 + (tree.y)**2)**.5)
    
def dot(vectorA, vectorB):
    '''only accepts two parameters)'''
    #vectorA = Point(x_0,y_0)
    #vectorB = Point(x_1,y_1)
    return (vectorA.x * vectorB.x) + (vectorA.y * vectorB.y)

def theta(vectorC, vectorD):
    
    top = dot(vectorC, vectorD)
    bottom = ( (mag(vectorC)) * (mag(vectorD)) )
    
    print(f"\ntheta: {rad2deg(arccos(top/bottom))}")
    return
        
def main():
   
    vx0 = float(input("Enter the x coordinate for the 1st vector: "))
    vy0 = float(input("Enter the y coordinate for the 1st vector: "))
    
    vx1 = float(input("\nEnter the x coordinate for the 2nd vector: "))
    vy1 = float(input("Enter the y coordinate for the 2nd vector: "))
    
    theta_input1 = Point(vx0,vy0)
    theta_input2 = Point(vx1,vy1)
    
    
    print(f"\nThe magnitude of the 1st vector is {mag(theta_input1)}.\
          \nThe magnitude of the 2nd vector is {mag(theta_input2)}.\n")

    print(f"The dot product of the two vectors is \
{dot(theta_input1,theta_input2)}")

    return theta(theta_input1,theta_input2)

main()







