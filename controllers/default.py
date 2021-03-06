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

import mvhutils

# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    begin_maand, einde_maand = mvhutils.beginEindeHuidigeMaand()
    query = ((db.wedstrijd.datum >= begin_maand)&
             (db.wedstrijd.datum <= einde_maand))
    wedstrijden = db(query).select(db.wedstrijd.datum,
                                   db.wedstrijd.omschrijving,
                                   db.wedstrijd.aanvang,
                                   db.wedstrijd.opmerkingen)
    return dict(wedstrijden=wedstrijden)

def kalender():
    T.force("nl")
    jaar = str(mvhutils.huidigJaar())
    kalender = db.kalender(db.kalender.jaar==jaar)
    query = (db.wedstrijd.kalender==kalender)
    wedstrijden = db(query).select(db.wedstrijd.datum,
                                   db.wedstrijd.omschrijving,
                                   db.wedstrijd.aanvang,
                                   db.wedstrijd.opmerkingen,
                                   orderby=db.wedstrijd.datum)
    return dict(wedstrijden=wedstrijden, huidig_jaar=jaar)


def uitslag():
    T.force("nl")
    jaar = str(mvhutils.huidigJaar())
    kalender = db.kalender(db.kalender.jaar==jaar)
    uitslagen = db(db.uitslag)._select(db.uitslag.wedstrijd, distinct=True)
    print "uitslagen = ", uitslagen
    wedstrijden = db((db.wedstrijd.kalender==kalender) &
                     (db.wedstrijd.id.belongs(uitslagen))).select(db.wedstrijd.id,
                                       db.wedstrijd.datum,
                                       db.wedstrijd.omschrijving,
                                       orderby=db.wedstrijd.datum
    )
    print "wedstrijden = ", wedstrijden
    return dict(wedstrijden=wedstrijden, jaar=jaar)


def reglement():
    T.force("nl")
    jaar = str(mvhutils.huidigJaar())
    huidigReglement = db.reglement(db.reglement.jaar==jaar)
    return dict(jaar="2014", reglement=huidigReglement)


def wedstrijduitslag():
    T.force("nl")
    wedstrijd_id = request.args(0)
    wedstrijd = db.wedstrijd(wedstrijd_id)
    uitslagen = (
        db(db.uitslag.wedstrijd==wedstrijd.id).select(orderby=db.uitslag.volgorde))
    return dict(wedstrijd=wedstrijd, uitslagen=uitslagen)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
