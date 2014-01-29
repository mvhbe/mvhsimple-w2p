#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime
import unittest
import mvhutils

VANDAAG = datetime.datetime.now().date()
JAAR = datetime.datetime.now().year
BEGIN_MAAND = datetime.date(VANDAAG.year, VANDAAG.month, 1)
EINDE_MAAND = datetime.date(VANDAAG.year, VANDAAG.month,
                            calendar.monthrange(VANDAAG.year,
                                                VANDAAG.month)[1])


class MvhutilsModule(unittest.TestCase):

    def testHuidigeDatum(self):
        """Datum van vandaag wordt terug gegeven"""
        vandaag = mvhutils.huidigeDatum()
        self.assertEqual(VANDAAG, vandaag)

    def testHuidigJaar(self):
        """Huidig jaar wordt terug gegeven"""
        self.assertEqual(JAAR, mvhutils.huidigJaar())

    def testBeginEindeHuidigeMaand(self):
        """Begin en einde huidige maand wordt terug gegeven"""
        begin_maand, einde_maand = mvhutils.beginEindeHuidigeMaand()
        self.assertEqual(BEGIN_MAAND, begin_maand)
        self.assertEqual(EINDE_MAAND, einde_maand)

    def testIsUur(self):
        """Uur validatie werkt correct"""
        defaultError = "Uur (UU:MM) foutief !"
        customError = "Error !"

        geldigUur = IS_UUR()
        defaultError = "Uur (UU:MM) foutief !"
        uur, error = geldigUur("00:00")
        self.assertEqual(error, None)
        uur, error = geldigUur("23:59")
        self.assertEqual(error, None)
        uur, error = geldigUur("00u00")
        self.assertEqual(error, defaultError)
        uur, error = geldigUur("24:00")
        self.assertEqual(error, defaultError)

        geldigUur = IS_UUR(customError)
        uur, error = geldigUur("00:00")
        self.assertEqual(error, None)
        uur, error = geldigUur("23:59")
        self.assertEqual(error, None)
        uur, error = geldigUur("00u00")
        self.assertEqual(error, customError)
        uur, error = geldigUur("24:00")
        self.assertEqual(error, customError)

