#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.functionaltest import FunctionalTest, ROOT

MVHURL = ROOT + "/mvh/"


class DefaultIndexView(FunctionalTest):

    def testHomePageIsBereikbaar(self):
        """Home page is bereikbaar"""
        response_code = self.getResponseCode(MVHURL)
        self.assertEqual(200, response_code)

    def testHeeftHeader(self):
        """Hompe page heeft header"""
        self.browser.get(MVHURL)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Wedstrijden deze maand', body.text)

    def testGeenWedstrijdenAanwezig(self):
        """Geen wedstrijden aanwezig"""
        self.browser.get(MVHURL)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Geen wedstrijden.', body.text)
