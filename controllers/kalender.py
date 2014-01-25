#!/usr/bin/env python
# -*- coding: utf-8 -*-


def overzicht():
    T.force("nl")
    #db.kalender.jaar.represent = jaar_link
    kalenders = db(db.kalender).select(orderby=~db.kalender.jaar)
    return dict(kalenders=kalenders)
