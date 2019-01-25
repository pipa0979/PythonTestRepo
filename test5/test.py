from unittest import TestCase
from unittest.mock import patch
import main

class TestBlog(TestCase):
    def setUp(self):
        pass

    @patch('main.Blog')
    def testTheBlog(self, mock_object):
        blog = mock_object()
        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response)

