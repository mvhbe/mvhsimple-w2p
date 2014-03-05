#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IDE stuff for web2py
if 0:
    import db
    from gluon.globals import *
    from gluon.tools import auth, crud, T, service
    from gluon.cache import Cache
    from gluon.html import *
    from gluon.http import *
    from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
    session = Session()
    request = Request()
    response = Response()
    cache = Cache()

@auth.requires_membership("admin")
def overzicht():
    T.force("nl")
    db.kalender.jaar.represent = jaar_link
    kalenders = db(db.kalender).select(orderby=~db.kalender.jaar)
    return dict(kalenders=kalenders)

@auth.requires_membership("admin")
def wedstrijden():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    wedstrijden = (
        db(db.wedstrijd.kalender==kalender.id).select(db.wedstrijd.id,
                                                      db.wedstrijd.datum,
                                                      db.wedstrijd.omschrijving,
                                                      orderby=db.wedstrijd.datum))
    return dict(kalender=kalender, wedstrijden=wedstrijden)


@auth.requires_membership("admin")
def uitslag():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    uitslagen = (
        db(db.uitslag.wedstrijd==wedstrijd.id).select(orderby=db.uitslag.volgorde))
    return dict(wedstrijd=wedstrijd, uitslagen=uitslagen)


@auth.requires_membership("admin")
def detail():
    T.force("nl")
    uitslag_id = request.args(0)
    uitslag = db.uitslag(uitslag_id)
    db.uitslag.wedstrijd.readable = False
    db.uitslag.wedstrijd.writable = False
    valideer_volgorde(uitslag.wedstrijd.id)
    crud.settings.update_deletable = False
    form = crud.update(db.uitslag, uitslag  ,
                       next=URL("uitslag", "uitslag", args=uitslag.wedstrijd.id))
    return dict(form=form, uitslag=uitslag)


@auth.requires_membership("admin")
def nieuw():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    db.uitslag.wedstrijd.readable = False
    db.uitslag.wedstrijd.writable = False
    db.uitslag.wedstrijd.default = wedstrijd.id
    valideer_volgorde(wedstrijd_id)
    form = crud.create(db.uitslag,
                       next=URL("uitslag", "uitslag", args=wedstrijd.id))
    return dict(form=form, wedstrijd=wedstrijd)


@auth.requires_membership("admin")
def importeren():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    form=FORM(TABLE (
                     TR(
                       TD(LABEL('Importeer Bestand :')),
                       TD(INPUT(_type='file', _name='bestand', _id='bestand', requires=IS_NOT_EMPTY()))
                       ),
                     TR(
                       TD(INPUT(_type='submit',_value='Importeren'))
                       )
                     ))
    if form.accepts(request, session):
        records = form.vars.bestand.file.readlines()
        importUitslag(wedstrijd_id, records)
        redirect(URL("uitslag", "uitslag", args=wedstrijd.id))
    return dict(wedstrijd=wedstrijd, form=form)
