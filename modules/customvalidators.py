#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon.validators import Validator


class IS_UUR(Validator):
    """
    Valideer of een uur geldig is.
    Formaat : UU:MM
    Geldige waarden :
        - uren : tussen 00 en 23
        - minuten : tussen 00 en 59
    """

    def __init__(self, error_message="Uur (UU:MM) foutief !"):
        self.error_message = error_message

    def __call__(self, uur):
        error = None
        if not self.valideer_lengte(uur):
            error = self.error_message
        uren, scheidingsteken, minuten = self.splits(uur)
        uren_ok = self.valideer_uren(uren)
        scheidingsteken_ok = self.valideer_scheidingsteken(scheidingsteken)
        minuten_ok = self.valideer_minuten(minuten)
        if uren_ok and minuten_ok and scheidingsteken_ok:
            pass
        else:
            error = self.error_message
        return (uur, error)

    def valideer_lengte(self, value):
        return (len(value) == 5)

    def valideer_uren(self, uren):
        return  ('00' <= uren <= '23')

    def valideer_minuten(self, minuten):
        return ('00' <= minuten <= '59')

    def valideer_scheidingsteken(self, teken):
        return (teken == ':')

    def splits(self, uur):
        return (uur[0:2], uur[2:3], uur[3:])
