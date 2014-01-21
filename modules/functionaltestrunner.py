#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import glob

suite = unittest.TestSuite()

APP = "mvh"

# get all files with tests
test_files = glob.glob('applications/' + APP + '/functionaltests/*/*/*.py')

if not len(test_files):
    raise Exception("No files found for app: " + APP)

# Bring all unit tests in and their controllers/models/whatever
for test_file in test_files:
    execfile(test_file, globals())

    # Create the appropriate class name based on filename and path
    # TODO: use regex
    filename = str.capitalize(test_file.split("/")[-1][:-3])
    controller = str.capitalize(test_file.split("/")[-2])
    directory = str.capitalize(test_file.split("/")[-3][:-1])

    suite.addTest(unittest.makeSuite(globals()[controller+filename+directory]))


unittest.TextTestRunner(verbosity=2).run(suite)
