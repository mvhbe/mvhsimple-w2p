#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


def setupTestDb():
    testDb = DAL('sqlite:memory:')
    for tableName in db.tables:
        tableCopy = [copy.copy(table) for table in db[tableName]]
        testDb.define_table(tableName, *tableCopy)
    return testDb
