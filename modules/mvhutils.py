#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
import datetime


def huidigeDatum():
    return datetime.datetime.now().date()


def huidigJaar():
    return datetime.datetime.now().year


def beginEindeHuidigeMaand():
    vandaag = huidigeDatum()
    eerste_dag = 1
    laatste_dag = calendar.monthrange(vandaag.year, vandaag.month)[1]
    begin_maand = datetime.date(vandaag.year, vandaag.month, eerste_dag)
    einde_maand = datetime.date(vandaag.year, vandaag.month, laatste_dag)
    return begin_maand, einde_maand



