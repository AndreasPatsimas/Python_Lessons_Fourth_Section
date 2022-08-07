import unittest
from unit_testing import main

class TestMain(unittest.TestCase):

    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        num = 'aris'
        result = main.do_stuff(num)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        num = None
        result = main.do_stuff(num)
        self.assertEqual(result, "please enter a number")

    def tearDown(self):
        print("cleaning down")




