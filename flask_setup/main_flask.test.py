#!/usr/bin/env python
import unittest
from main_flask import app

class Routes_Tests(unittest.TestCase):
	def test_links(self):
        	holder = app.test_client(self)
        	response = holder.get('/links', content_type='html/text')
        	self.assertEqual(response.status_code, 200)
        	self.assertEqual(response.data, b'<h1> A set of links</h1>')

	def test_everything_else(self):
        	holder = app.test_client(self)
        	response = holder.get('a', content_type='html/text')
        	self.assertEqual(response.status_code, 404)
        	self.assertTrue(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()

