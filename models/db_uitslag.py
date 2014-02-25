#!/usr/bin/env python
# -*- coding: utf-8 -*-

db.define_table('uitslag',
                Field("wedstrijd", "reference wedstrijd"),
                Field('plaats', 'integer'),
                Field('deelnemer', 'string', length=100, notnull=True,
                      label="Deelnemer(s)"),
                Field('gewicht1', 'integer',
                      label="Gewicht reeks 1"),
                Field('gewicht2', 'integer',
                      label="Gewicht reeks 2"),
                Field('gewicht3', 'integer',
                      label="Gewicht reeks 3"),
                Field('totaal', 'integer',
                      label="Totaal gewicht"),
                auth.signature
                )

db.uitslag.wedstrijd.requires = [
    IS_IN_DB(db, 'wedstrijd.id', "%(datum)s")
]
db.uitslag.deelnemer.requires = [
    IS_NOT_EMPTY(error_message="Deelnemer(s) niet ingevuld !")
]

def valideer_plaats(wedstrijd_id):
    plaatsen = db(db.uitslag.wedstrijd==wedstrijd_id)
    db.uitslag.plaats.requires = [
        IS_NOT_EMPTY(error_message="Plaats niet ingevuld !"),
        IS_NOT_IN_DB(plaatsen, 'uitslag.plaats',
                     error_message="Plaats bestaat reeds !")
    ]
