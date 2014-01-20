#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functionaltest import FunctionalTest, ROOT


class DefaultController(FunctionalTest):

    def testCanViewHomePage(self):

        # John opens his browser and goes to the home-page of the tukker app
        #self.browser.get(ROOT + '/mvhsimple/')

        self.assertEqual(200, self.getResponseCode(ROOT + '/mvhsimple/'))
        # He's looking at the homepage and sees the Heading "Messages With 300 Chars"
        #body = self.browser.find_element_by_tag_name('body')
        #self.assertIn('Messages With 300 Chars', body.text)
