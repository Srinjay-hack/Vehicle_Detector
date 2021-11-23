from random import randint
import time


class Car:
    lane=[]
    def __init__(self,a,x,y,age):
        self.a=a
        self.x=x
        self.y=y
        self.lane=[]
        self.R=randint(0,255)
        self.G=randint(0,255)
        self.B=randint(0,255)
        self.isdone=False
        self.state='0'
        self.age=0
        self.max_age=age
        self.dir=None

    def getRGB(self):  #For the RGB colour
        return (self.R,self.G,self.B)

    def getTracks(self):
        return self.lane

    def getId(self): #For the ID
        return self.a

    def getState(self):
        return self.state

    def getDir(self):
        return self.dir

    def getX(self):  #for x coordinate
        return self.x

    def getY(self):  #for y coordinate
        return self.y

    def updateCoords(self, xn, yn):
        self.age = 0
        self.lane.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def setDone(self):
        self.isdone = True

    def timedOut(self):
        return self.isdone

    def going_UP(self, mid_start, mid_end):
        if len(self.lane)>=2:
            if self.state=='0':
                if self.lane[-1][1]<mid_end and self.lane[-2][1]>=mid_end:
                    state='1'
                    self.dir='up'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
           
           
    def going_DOWN(self,mid_start,mid_end):
        if len(self.lane)>=2:
            if self.state=='0':
                if self.lane[-1][1]>mid_start and self.lane[-2][1]<=mid_start:
                    start='1'
                    self.dir='down'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def age_one(self):
        self.age+=1
        if self.age>self.max_age:
            self.done=True
        return  True

#Class2

class MultiCar:
    def __init__(self,cars,xi,yi):
        self.cars=cars
        self.x=xi
        self.y=yi
        self.lane=[]
        self.R=randint(0,255)
        self.G=randint(0,255)
        self.B=randint(0,255)
        self.done=False
