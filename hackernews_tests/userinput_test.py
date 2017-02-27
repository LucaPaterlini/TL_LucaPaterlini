import subprocess
import unittest
from json import loads
from rfc3986 import is_valid_uri
# CONSTANTS
LIMIT = 100
POSTS_EACH_PAGE = 30
APP_NAME = "./hackernews"
# -*-


class InputTest(unittest.TestCase):
    def test_wrong_arguments(self):
        # tests a list of wrong parameters expecting the error msg
        err_msg = "USAGE:\n--posts: how many posts to print A positive integer <= 100.\n"

        list_arg_tests = [("post", ""), ("--none", "42"), ("--posts", "101"), ("--posts", "-1")]
        self.assertEquals(subprocess.check_output([APP_NAME, ""]), err_msg)
        for name, val in list_arg_tests:
            self.assertEquals(subprocess.check_output([APP_NAME, name, val]), err_msg)

    def test_all_valid_inputs(self):
        # tests every field returned from the app
        keys_str = "[u'author', u'comments', u'points', u'rank', u'title', u'uri']"
        for z in [1, POSTS_EACH_PAGE, LIMIT]:
            result = subprocess.check_output([APP_NAME, "--posts", str(z)])
            result = loads(result)
            self.assertEquals(z, len(result))
            for i in xrange(len(result)):
                self.assertEquals(str(sorted(result[i].keys())), keys_str)
                # author_test
                self.assertTrue(isinstance(result[i]["author"], basestring))
                self.assertTrue(0 < len(result[i]["author"]) < 257)
                # title_test
                self.assertTrue(isinstance(result[i]["title"], basestring))
                self.assertTrue(0 < len(result[i]["title"]) < 257)
                # uri_test
                self.assertTrue(is_valid_uri(result[i]["uri"]))
                # points_test comments_test rank
                for c in ["points", "comments", "rank"]:
                    self.assertTrue(isinstance(result[i][c], int) and result[i][c] >= 0)

if __name__ == '__main__':
    unittest.main()
