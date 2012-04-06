'''
Created on 05.04.2012

@author: Alexey
'''
import unittest
import s3

class Test(unittest.TestCase):


    def setUp(self):
        self.index, self.graph = s3.crawl_web('http://www.udacity.com/cs101x/final/multi.html')


    def tearDown(self):
        pass


    def test1(self):
        self.assertEqual(s3.multi_lookup(self.index, ['Python']), 
                               ['http://www.udacity.com/cs101x/final/a.html', 
                                'http://www.udacity.com/cs101x/final/b.html'])

    def test2(self):
        self.assertEqual(s3.multi_lookup(self.index, ['Monty', 'Python']), 
                               ['http://www.udacity.com/cs101x/final/a.html'])

    def test3(self):
        self.assertEqual(s3.multi_lookup(self.index, ['Python', 'programming', 'language']),
                               ['http://www.udacity.com/cs101x/final/b.html'])

    def test4(self):
        self.assertEqual(s3.multi_lookup(self.index, ['Thomas', 'Jefferson']),
                               ['http://www.udacity.com/cs101x/final/a.html', 
                                'http://www.udacity.com/cs101x/final/b.html'])
    def test5(self):
        self.assertEqual(s3.multi_lookup(self.index, ['most', 'powerful', 'weapon']),
                               ['http://www.udacity.com/cs101x/final/a.html'])
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()