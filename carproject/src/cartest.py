'''
Created on May 17, 2013

@author: rodsur
'''
import unittest
import car

class Test(unittest.TestCase):


    def testCar(self):
        car1 = car.car()
        Test.assertEqual(self, 0, car1.getSpeed(), "speed of car 1 does not equal 0")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCar']
    unittest.main()