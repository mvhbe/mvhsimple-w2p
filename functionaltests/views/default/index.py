#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functionaltest import FunctionalTest, ROOT


class DefaultIndexView(FunctionalTest):

    def testKanHomePageZien(self):

        # John opens his browser and goes to the home-page of the tukker app
        self.browser.get(ROOT + '/mvh/')

        # He's looking at the homepage and sees the Heading
        # "Visclub Moed & Volharding"
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Visclub Moed & Volharding', body.text)
