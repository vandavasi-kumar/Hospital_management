def labtech_context(request):
    if request.user.is_authenticated:
        labtech = getattr(request.user, 'lab_report', None)
    else:
        labtech = None

    return {'labtech': labtech}