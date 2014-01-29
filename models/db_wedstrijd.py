#!/usr/bin/env python
# -*- coding: utf-8 -*-

from customvalidators import IS_UUR

def wedstrijd_string(datum):
    return datum

def wedstrijd_link(datum, row):
    return A(datum.strftime("%d/%m/%Y"),
             _href=URL('wedstrijd', 'detail',args=row.id))

db.define_table('wedstrijd',
                Field("kalender", "reference kalender"),
                Field('datum', 'date', unique=True, notnull=True, required=True),
                Field('omschrijving', 'string', length=100, notnull=True,
                      required=True),
                Field('aanvang', 'string', length=5, notnull=True,
                      required=True, default="13:30"),
                Field('opmerkingen', 'text'),
                auth.signature
)

db.wedstrijd.kalender.requires = IS_IN_DB(db, db.kalender.id, "%(jaar)s")
db.wedstrijd.omschrijving.requires = [
    IS_NOT_EMPTY(error_message="Omschrijving niet ingevuld !")
]
db.wedstrijd.datum.requires = [
    IS_DATE(format='%d/%m/%Y',
            error_message="Datum (DD/MM/JJJJ) niet ingevuld !"),
    IS_NOT_IN_DB(db, db.wedstrijd.datum,
                 error_message="Datum bestaat reeds !")
]
uurGeldig = IS_UUR()
db.wedstrijd.aanvang.requires = [
    IS_NOT_EMPTY(error_message="Uur (UU:MM) niet ingevuld !"),
    uurGeldig(db.wedstrijd.aanvang)
    # IS_TIME(error_message="Uur (UU:MM) foutief !")
]
