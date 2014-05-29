#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO veld plaats per reeks toevoegen + html aanpassen
# TODO veld opmerking toevoegen + html aanpassen
# TODO extra tabel voorzien voor de vaste plaatsen
# TODO schema vijver toevoegen met de vaste plaatsen


def uitslag_link(plaats, id):
    return A(plaats, _href=URL('uitslag', 'detail',args=id))


def importUitslag(wedstrijdId, uitslagLijnen):
    for lijn in uitslagLijnen:
        volgorde, deelnemer, plaats, gewicht1, gewicht2, gewicht3, totaal = lijn.split(";")
        db.uitslag.insert(wedstrijd=wedstrijdId,
                          volgorde=volgorde,
                          deelnemer=deelnemer,
                          plaats=plaats,
                          gewicht1=gewicht1,
                          gewicht2=gewicht2,
                          gewicht3=gewicht3,
                          totaal=totaal
                          )


def valideer_plaats():
    return [IS_NOT_EMPTY(error_message="Plaats niet ingevuld !")]

db.define_table('uitslag',
                Field("wedstrijd", "reference wedstrijd"),
                Field('volgorde', 'integer'),
                Field('deelnemer', 'string', length=100, notnull=True,
                      label="Deelnemer(s)"),
                Field('plaats1', 'integer',
                      label="Plaats reeks 1"),
                Field('gewicht1', 'integer',
                      label="Gewicht reeks 1"),
                Field('plaats2', 'integer',
                      label="Plaats reeks 2"),
                Field('gewicht2', 'integer',
                      label="Gewicht reeks 2"),
                Field('plaats3', 'integer',
                      label="Plaats reeks 3"),
                Field('gewicht3', 'integer',
                      label="Gewicht reeks 3"),
                Field('totaal', 'integer',
                      label="Totaal gewicht"),
                Field('opmerking', 'string', length=100,
                      label="Opmerking"),
                auth.signature
                )

db.uitslag.wedstrijd.requires = [
    IS_IN_DB(db, 'wedstrijd.id', "%(datum)s")
]
db.uitslag.deelnemer.requires = [
    IS_NOT_EMPTY(error_message="Deelnemer(s) niet ingevuld !")
]
db.uitslag.plaats1.requires = [
    valideer_plaats
]
db.uitslag.plaats2.requires = [
    valideer_plaats
]
db.uitslag.plaats3.requires = [
    valideer_plaats
]


def valideer_volgorde(wedstrijd_id):
    #volgorde = db(db.uitslag.wedstrijd==wedstrijd_id)
    db.uitslag.volgorde.requires = [
        IS_NOT_EMPTY(error_message="Volgorde niet ingevuld !"),
        #IS_NOT_IN_DB(volgorde, 'uitslag.volgorde',
        #             error_message="Volgorde bestaat reeds !")
    ]
