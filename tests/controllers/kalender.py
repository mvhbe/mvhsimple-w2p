#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mvhutils
import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb()  # Use the test database for all tests

HUIDIG_JAAR = mvhutils.huidigJaar()


def login():
    insertUser()
    db.commit()
    auth.user = db(db.auth_user.id == 1).select()[0]


def insertUser():
    db.auth_user.insert(first_name="first", last_name="last",
                        email="first.last@telenet.be")


def insertKalender(jaar):
    db.kalender.insert(jaar=jaar)


def nieuweKalender():
    insertKalender(HUIDIG_JAAR)
    db.commit()


class KalenderController(unittest.TestCase):

    #loggedIn = False

    def setUp(self):
        #login()
        self.request = Request({})

    def tearDown(self):
        db.kalender.truncate()
        db.auth_user.truncate()
        db.commit()

    def testOverzichtGeeftGeenKalendersTerugBijLegeDb(self):
        """Geen kalenders bij lege database"""
        response = overzicht()
        self.assertEqual(0, len(response["kalenders"]))

    def testOverzichtGeeftKalenderTerug(self):
        """Kalender wordt opgehaald"""
        nieuweKalender()
        response = overzicht()
        self.assertEqual(1, len(response["kalenders"]))
