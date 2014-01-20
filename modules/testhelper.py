def form_postvars(tablename, fields, request, action="create", record_id=None):
    """
    Creates the appropriate request vars for forms
    """
    for field_name in fields:
        request.vars[field_name] = fields[field_name]

    if action == "create":
        request.vars["_formname"] = tablename + "_" + action
    elif action == "update":
        request.vars["_formname"] = tablename + "_" + str(record_id)
        request.vars["id"] = record_id
    elif action == "delete":
        request.vars["_formname"] = tablename + "_" + str(record_id)
        request.vars["id"] = record_id
        request.vars["delete_this_record"] = True
    else:
        raise Exception("The form action '", action, "' does not exist")
