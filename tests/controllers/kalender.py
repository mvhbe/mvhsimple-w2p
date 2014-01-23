#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from gluon.globals import Request, Session, Storage, Response


class KalenderController(unittest.TestCase):

    def setUp(self):
        self.request = Request({})

    def tearDown(self):
        pass

    def testGeenKalenders(self):
        """Geen kalenders bij lege database"""
        response = overzicht()
        self.assertEqual(0, len(response["kalenders"]))
