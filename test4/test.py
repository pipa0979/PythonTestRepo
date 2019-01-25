from unittest import TestCase
from unittest.mock import patch
import main

class TestBlog(TestCase):
    def setUp(self):
        pass

    @patch('main.Blog.posts', return_value = 10)
    def testTheBlog(self, mock_object):
        self.assertEqual(mock_object(10,10), 10)


