import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        '''Hi this is a comment'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # testing if 10 +5 will be equal if if

    def test_do_stuff2(self):
        test_param = 'asdqwezxc'
        result = main.do_stuff(test_param)
        # here because we return the error we just returning its class instance so this one will get true
        # we chose the value error because we convert the num to int so it will give us value error if we input string
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


# now we call here the main file
if __name__ == '__main__':
    unittest.main()
