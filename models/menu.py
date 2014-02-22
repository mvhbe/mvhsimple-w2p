#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Visclub ',SPAN("Moed & Volharding")),XML('&trade;&nbsp;'),
                  _class="brand",_href="#")
response.title = 'Visclub Moed & Volharding'
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Guido Van Hoof'
response.meta.description = 'a cool new app'
response.meta.keywords = 'mvh, visclub, moed & volharding'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Kalender'), False, URL('default', 'kalender'), []),
    (T('Uitslag'), False, URL('default', 'uitslag'), []),
]

if auth.has_membership(role="admin"):
    response.menu.append((T('Kalenders'), False, URL('kalender', 'overzicht'), []))
    response.menu.append((T('Uitslagen'), False, URL('uitslag', 'overzicht'), []))

if "auth" in locals():
    auth.wikimenu()
