#!/usr/bin/env python
# -*- coding: utf-8 -*-

db.define_table('reglement',
                Field('jaar', 'string', length=4, unique=True, notnull=True),
                Field('reglement', 'text'),
                auth.signature
                )

db.reglement.jaar.requires = [
    IS_INT_IN_RANGE(1900, 2999, "Jaar ongeldig !"),
    IS_NOT_IN_DB(db, db.reglement.jaar, error_message="Jaar bestaat reeds !")
]

