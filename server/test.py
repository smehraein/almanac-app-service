import json
import os
# from app import app
import unittest

class SimpleTest(unittest.TestCase):

    def test_true(self):
        self.assertEqual (1+1, 2)

    #basic setup
    # def setUp(self):
    #     app.config['TESTING'] = True
    #     self.app = app.test_client()

    #test that hitting the '/news' api route returns a list structure
    # def test_news(self):
    #     rv = self.app.get('/news')
        # assert "Did the redis thing" in rv.data


    # #test that hitting the '/top' route with a category returns a list structure
    # def test_top(self):
    #     rv = self.app.get('/top/health')
    #     resp = json.loads(rv.data)
    #
    #     self.assertIsInstance(resp, list)

    #test that hitting the '/date/<date>' route with a date returns a list structure
    # def test_date(self):
    #     rv = self.app.get('/date/2015-12-08')
    #     resp = json.loads(rv.data)
    #
    #     self.assertIsInstance(resp, list)
    #
    # def test_landing(self):
    #     rv = self.app.get('/')
    #     assert "JOB SEARCH DIESEL!!!!!!!!!!" in rv.data

if __name__ == '__main__':
    unittest.main()
