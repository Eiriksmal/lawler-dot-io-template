from datetime import datetime

def current_copyright(unused):
    """Return the copyright footer """
    first = 2019
    year = datetime.now().strftime('%Y')
    diff = int(year) - first
    return '&copy;2019&ndash;' + year if diff > 0 else '&copy;' + year
