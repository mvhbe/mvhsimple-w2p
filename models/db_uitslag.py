#!/usr/bin/env python
# -*- coding: utf-8 -*-

db.define_table('uitslag',
                Field("wedstrijd", "reference wedstrijd"),
                Field('plaats', 'integer'),
                Field('deelnemer', 'string', length=100, notnull=True),
                Field('gewicht1', 'integer', default=0),
                Field('gewicht2', 'integer', default=0),
                Field('gewicht3', 'integer', default=0),
                Field('totaal', 'integer', default=0),
                auth.signature
                )

db.uitslag.wedstrijd.requires = IS_IN_DB(db, 'wedstrijd.id', "%(datum)s")
def valideer_plaats(wedstrijd_id):
    plaatsen = db(db.uitslag.wedstrijd==wedstrijd_id)
    db.uitslag.plaats.requires = [
        IS_NOT_EMPTY(error_message="Plaats niet ingevuld !"),
        IS_NOT_IN_DB(plaasten, db.uistlag.plaats,
                     error_message="Plaats bestaat reeds !")
    ]
