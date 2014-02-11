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
def nieuw():
    T.force("nl")
    form = crud.create(db.kalender, next=URL("kalender", "overzicht"))
    return dict(form=form)


@auth.requires_membership("admin")
def detail():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    crud.settings.update_deletable = False
    form = crud.update(db.kalender, kalender, next=URL("kalender", "overzicht"))
    return dict(form=form)


@auth.requires_membership("admin")
def wedstrijden():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    db.wedstrijd.datum.represent = wedstrijd_link
    wedstrijden = (
        db(db.wedstrijd.kalender == kalender.id).
            select(db.wedstrijd.id,
                   db.wedstrijd.datum,
                   db.wedstrijd.omschrijving,
                   db.wedstrijd.aanvang,
                   db.wedstrijd.opmerkingen,
                   orderby=db.wedstrijd.datum))
    return dict(kalender=kalender, wedstrijden=wedstrijden)


@auth.requires_membership("admin")
def importeren():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    form=FORM('Te importeren wedstrijden :',
              TEXTAREA(_name='records', requires=IS_NOT_EMPTY()),
              INPUT(_type="submit", _value="Importeren"))
    if form.accepts(request,session):
        redirect(URL("kalender", "importWedstrijden", args=[kalender_id, form.vars.records]))
    # elif form.errors:
    #     response.flash = 'form has errors'
    # else:
    #     response.flash = 'please fill the form'
    return dict(kalender=kalender, form=form)


@auth.requires_membership("admin")
def importWedstrijden():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    print ">>> hier te implementen : importeren wedstrijden !"
    print "records = ", request.args(1)
    redirect(URL("kalender", "wedstrijden", args=kalender.id))
