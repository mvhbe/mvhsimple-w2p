#!/usr/bin/env python
# -*- coding: utf-8 -*-


@auth.requires_membership("admin")
def detail():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    kalender = db.kalender(db.kalender.id==wedstrijd.kalender)
    db.wedstrijd.kalender.readable = False
    db.wedstrijd.kalender.writable = False
    crud.settings.update_deletable = False
    form = crud.update(db.wedstrijd, wedstrijd,
                       next=URL("kalender", "wedstrijden", args=kalender.id))
    return dict(form=form, kalender=kalender)


@auth.requires_membership("admin")
def nieuw():
    T.force("nl")
    kalender_id = request.args(0)
    kalender = db.kalender(kalender_id)
    db.wedstrijd.kalender.readable = False
    db.wedstrijd.kalender.writable = False
    db.wedstrijd.kalender.default = kalender.id
    form = crud.create(db.wedstrijd,
                       next=URL("kalender", "wedstrijden", args=kalender_id))
    return dict(form=form, kalender=kalender)
