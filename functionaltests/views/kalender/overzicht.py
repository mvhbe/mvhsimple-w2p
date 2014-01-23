#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functionaltest import FunctionalTest, ROOT

KALENDERSURL = ROOT + "/mvh/kalender/overzicht/"


class KalenderOverzichtView(FunctionalTest):

    def testOverzichtKalendersIsBereikbaar(self):
        """Overzicht kalenders is bereikbaar"""
        response_code = self.getResponseCode(KALENDERSURL)
        self.assertEqual(200, response_code)

    def testHeeftHoofding(self):
        """Hoofding = Overzicht kalenders"""
        self.browser.get(KALENDERSURL)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Overzicht kalenders', body.text)

    def testGeenKalendersAanwezig(self):
        """Geen kalenders aanwezig"""
        self.browser.get(KALENDERSURL)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Geen kalenders.', body.text)
