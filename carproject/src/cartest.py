'''
Created on May 17, 2013

@author: rodsur
'''
import unittest
import car

class Test(unittest.TestCase):


    def testCarStart(self): #tests initilization of cars and checks variables
        print("Starting start test")
        car1 = car.car()
        car2 = car.car(position=20)
        car1.setNextCar(car2)
        Test.assertEqual(self, 0, car1.getSpeed(), "speed of car 1 does not equal 0")
        Test.assertEqual(self, 0, car1.getPosition(), "Position of car 1 does not equal 0")
        Test.assertEqual(self, 0, car1.getAccel(), "Acceleration of car 1 does not equal 0")
        Test.assertEqual(self, 100, car1.getMaxSpeed(), "Max Speed of car 1 does not equal 100")
        Test.assertEqual(self, 20, car1.getDistanceForward(car2), "Distance between cars is not 20")
        Test.assertEqual(self, 20, car2.getDistanceBehind(car1), "Distance from car 2 to car 1 is not 20")
    
    def testCarSpeed(self): #should check speed
        print("Starting speed test")
        car1 = car.car(mode="override")
        car1.setSpeed(20)
        Test.assertEqual(self, 0, car1.getPosition(), "Car 1 was not where assumed")
        Test.assertEqual(self, 20, car1.getSpeed(), "Car 1 is not driving with assumed speed")
        car1.act()
        Test.assertEqual(self, 20, car1.getPosition(), "Car 1 was still not where assumed")
        car1.setSpeed(30)
        car1.act()
        Test.assertEqual(self, 50, car1.getPosition(), "Car 1 was not where assumed")
    
    def testCarAccel(self):
        print("Starting acceleration test")
        car1 = car.car(mode="automatic")
        Test.assertEqual(self, 0, car1.getPosition(), "car 1 was not at 0")
        car1.setSpeedAim(50)
        car1.act()
        Test.assertEqual(self, 2, car1.getPosition(), "Car 1 was not at 2")
        Test.assertEqual(self, 2, car1.getSpeed(), "Car did not have a speed of 2")
        car1.act()
        Test.assertEqual(self, 6, car1.getPosition(), "Car was not at 6")
        Test.assertEqual(self, 4, car1.getSpeed(), "Car did was not at speed 4")
        count = 0
        while (count < 25):
            car1.act()
            count = count + 1
        Test.assertEqual(self, 750, car1.getPosition(), "car was not at expected position")
        Test.assertEqual(self, 50, car1.getSpeed(), "car has either crossed or not reached speed limit")
        car1.act()
        Test.assertEqual(self, 800, car1.getPosition(), "car has not moved after achieving max speed")
    
    def testKeepDistance(self):
        print("Starting acceleration test")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCar']
    unittest.main()