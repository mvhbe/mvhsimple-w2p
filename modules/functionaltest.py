#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest  # for Python <= 2.6
except:
    import unittest
import sys
import urllib2
from selenium import webdriver
import subprocess
import os.path

ROOT = 'http://localhost:8000'


class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.web2py = start_web2py_server()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    @classmethod
    def tearDownClass(self):
        self.browser.close()
        self.web2py.kill()

    def get_response_code(self, url):
        """Returns the response code of the given url

        url     the url to check for
        return  the response code of the given url
        """
        handler = urllib2.urlopen(url)
        return handler.getcode()


def start_web2py_server():
    #noreload ensures single process
    print os.path.curdir
    return subprocess.Popen(
        ['python', '../../web2py.py',
         'runserver', '-a "testing"', '-p 8000']
    )


# def run_functional_tests(pattern=None):
#     print 'running tests'
#     if pattern is None:
#         tests = unittest.defaultTestLoader.discover('fts')
#     else:
#         pattern_with_globs = '*%s*' % (pattern,)
#         tests = unittest.defaultTestLoader.discover('fts',
#                                                     pattern=pattern_with_globs)

#     runner = unittest.TextTestRunner()
#     runner.run(tests)


# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         run_functional_tests()
#     else:
#         run_functional_tests(pattern=sys.argv[1])
