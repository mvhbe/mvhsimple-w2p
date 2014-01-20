# -*- coding: utf-8 -*-

import unittest
import glob
import sys
import mvhutils
suite = unittest.TestSuite()

APP = "mvh"

# get all files with tests
test_files = glob.glob('applications/' + APP + '/tests/*/*.py')

if not len(test_files):
    raise Exception("No files found for app: " + APP)

# Bring all unit tests in and their controllers/models/whatever
for test_file in test_files:
    execfile(test_file, globals())

    # Create the appropriate class name based on filename and path
    # TODO: use regex
    filename =  str.capitalize(test_file.split("/")[-1][:-3])
    directory =  str.capitalize(test_file.split("/")[-2][:-1])

    suite.addTest(unittest.makeSuite(globals()[filename+directory]))

    # Load the to-be-tested file
    execfile("applications/"+ APP + "/" + directory.lower() +
             "s/" + filename.lower() + ".py", globals())


unittest.TextTestRunner(verbosity=2).run(suite)