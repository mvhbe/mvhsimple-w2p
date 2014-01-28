#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mvhutils
import unittest
from functionaltest import FunctionalTest, ROOT
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

#db = setupTestDb()  # Use the test database for all tests

HUIDIG_JAAR = mvhutils.huidigJaar()
KALENDERSURL = ROOT + "/mvh/kalender/overzicht/"


def insertKalender(jaar):
    db.kalender.insert(jaar=jaar)


def nieuweKalender():
    insertKalender(HUIDIG_JAAR)
    db.commit()
    kalenders = db(db.kalender.id > 0).select()
    print "kalenders = ", kalenders


class KalenderOverzichtView(FunctionalTest):

    def tearDown(self):
        db.kalender.truncate()
        db.commit()

    # def testOverzichtKalendersIsBereikbaar(self):
    #     """Overzicht kalenders is bereikbaar"""
    #     response_code = self.getResponseCode(KALENDERSURL)
    #     self.assertEqual(200, response_code)

    # def testHeeftHoofding(self):
    #     """Hoofding = Overzicht kalenders"""
    #     self.browser.get(KALENDERSURL)
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Overzicht kalenders', body.text)

    # def testGeenKalendersAanwezig(self):
    #     """Geen kalenders aanwezig"""
    #     self.browser.get(KALENDERSURL)
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Geen kalenders beschikbaar.', body.text)

    def testOverzichtKalendersGeeftKalenderWeer(self):
        """Bestaande kalender wordt weer gegeven"""
        nieuweKalender()
        response = self.browser.get(KALENDERSURL)
        print "response = ", response
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn("Wedstrijdkalender " + str(HUIDIG_JAAR), body.text)
