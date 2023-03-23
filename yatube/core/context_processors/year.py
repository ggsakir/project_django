from datetime import date


def year(request):
    now = date.today()
    now_year = now.year
    return {
        'year': now_year
    }
