#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        db(db.wedstrijd.kalender==kalender.id).select(db.wedstrijd.id,
                                                      db.wedstrijd.datum,
                                                      db.wedstrijd.omschrijving,
                                                      db.wedstrijd.aanvang,
                                                      db.wedstrijd.opmerkingen,
                                                      orderby=db.wedstrijd.datum))
    return dict(kalender=kalender, wedstrijden=wedstrijden)
