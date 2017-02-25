import os
import sys
import unittest

from hackernews_lib import *


class EachFunction(unittest.TestCase):
    def __test_scaraper(self, name_input_file, name_output_file, function):
        # tests all test cases passed in name_input_file comparing the results
        #  of the function fn with the expected results in name_output_file
        fdin = open(name_input_file, "r")
        fdout = open(name_output_file, "r")
        n = int(fdin.readline())
        self.assertEquals(n, int(fdout.readline()))
        for i in range(n):
            response = function(fdin.readline() + fdin.readline())
            response = ' '.join(map(unicode, response)).encode("utf-8")
            expected_result = fdout.readline().replace("\n", "")
            self.assertEquals(response, expected_result)
        fdin.close()
        fdout.close()

    def test_sanitize_url(self):
        url = "https://news.ycombinator.com/newest?"
        url_rel = "item?id=13717740"
        self.assertEquals(sanitize_url(url, url_rel), "https://news.ycombinator.com/item?id=13717740")

    def test_scrape_top(self):
        self.__test_scaraper("./hackernews_tests/tests_input/scrape_top_in",
                             "./hackernews_tests/tests_output/scrape_top_out", scrape_top)

    def test_scrape_subtitle(self):
        self.__test_scaraper("./hackernews_tests/tests_input/scrape_subtitle_in",
                             "./hackernews_tests/tests_output/scrape_subtitle_out", scrape_subtitle)


    def test_scrape_article(self):
        # tests all test in name_input_top and name_input_subtitle comparing the results
        # of the function with the  expected results in name_output

        name_input_top = "./hackernews_tests/tests_input/scrape_top_in"
        name_input_subtitle = "./hackernews_tests/tests_input/scrape_subtitle_in"
        name_output = "./hackernews_tests/tests_output/scrape_article_out"

        fdintop = open(name_input_top, "r")
        fdintsub = open(name_input_subtitle, "r")
        fdout = open(name_output, "r")

        n = int(fdintop.readline())
        self.assertEquals(n, int(fdintsub.readline()))
        self.assertEquals(n, int(fdout.readline()))

        for i in range(n):
            response = scrape_article(fdintop.readline() + fdintop.readline(),
                                      fdintsub.readline() + fdintsub.readline())
            response = ' '.join(map(unicode, response)).encode("utf-8")
            expected_result = fdout.readline().replace("\n", "")
            self.assertEquals(response, expected_result)

        fdintop.close()
        fdintsub.close()
        fdout.close()

if __name__ == '__main__':
    unittest.main()
