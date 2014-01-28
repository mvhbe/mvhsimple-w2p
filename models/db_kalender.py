#!/usr/bin/env python
# -*- coding: utf-8 -*-


def jaar_string(jaar):
    return "Wedstrijdkalender " + jaar


def jaar_link(jaar, row):
    return A(jaar_string(jaar), _href=URL('kalender', 'detail', args=row.id))


def wedstrijden_link(row):
    return A("wedstrijden", _href=URL("kalender", "wedstrijden", args=row.id))

db.define_table('kalender',
                Field('jaar', 'string', length=4, unique=True, notnull=True),
                Field('opmerkingen', 'text'),
                auth.signature
                )

db.kalender.jaar.represent = jaar_string
db.kalender.jaar.requires = [IS_INT_IN_RANGE(1900, 2999,
                                             "Jaar ongeldig !"),
                             IS_NOT_IN_DB(db, db.kalender.jaar,
                                          error_message="Jaar bestaat reeds !")
                            ]
