#!/usr/bin/env python
# -*- coding: utf-8 -*-

def uitslag_link(plaats, id):
    return A(plaats, _href=URL('uitslag', 'detail',args=id))


def importUitslag(wedstrijdId, uitslagLijnen):
    for lijn in uitslagLijnen:
        volgorde, deelnemer, plaats1, gewicht1, locatie1, plaats2, gewicht2, \
            locatie2, plaats3, gewicht3, locatie3, totaal = lijn.split(";")
        db.uitslag.insert(wedstrijd=wedstrijdId,
                          volgorde=volgorde,
                          deelnemer=deelnemer,
                          plaats1=plaats1,
                          gewicht1=gewicht1,
                          locatie1=locatie1,
                          plaats2=plaats2,
                          gewicht2=gewicht2,
                          locatie1=locatie1,
                          plaats2=plaats2,
                          gewicht3=gewicht3,
                          locatie3=locatie3,
                          totaal=totaal,
                          opmerking=opmerking
                          )


db.define_table('uitslag',
                Field("wedstrijd", "reference wedstrijd"),
                Field('volgorde', 'integer'),
                Field('deelnemer', 'string', length=100, notnull=True,
                      label="Deelnemer(s)"),
                Field('plaats1', 'integer'),
                Field('gewicht1', 'integer',
                      label="Gewicht reeks 1"),
                Field('locatie1', 'string', length=3,
                      label='Locatie Reeks 1'),
                Field('plaats2', 'integer'),
                Field('gewicht2', 'integer',
                      label="Gewicht reeks 2"),
                Field('locatie2', 'string', length=3,
                      label='Locatie Reeks 2'),
                Field('plaats3', 'integer'),
                Field('gewicht3', 'integer',
                      label="Gewicht reeks 3"),
                Field('locatie3', 'string', length=3,
                      label='Locatie Reeks 3'),
                Field('totaal', 'integer',
                      label="Totaal gewicht"),
                Field('opmerking', 'string', length=100,
                      label='Opmerking'),
                auth.signature
                )

db.uitslag.wedstrijd.requires = [
    IS_IN_DB(db, 'wedstrijd.id', "%(datum)s")
]
db.uitslag.deelnemer.requires = [
    IS_NOT_EMPTY(error_message="Deelnemer(s) niet ingevuld !")
]
db.uitslag.plaats.requires = [
    IS_NOT_EMPTY(error_message="Plaats niet ingevuld !")
]

def valideer_volgorde(wedstrijd_id):
    #volgorde = db(db.uitslag.wedstrijd==wedstrijd_id)
    db.uitslag.volgorde.requires = [
        IS_NOT_EMPTY(error_message="Volgorde niet ingevuld !")
        #IS_NOT_IN_DB(volgorde, 'uitslag.volgorde',
        #             error_message="Volgorde bestaat reeds !")
    ]
