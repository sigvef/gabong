import requests
import datetime


def middag(phenny, input):

    def get_menu_for_campus(campus):
        r = requests.get(
            'http://www.sit.no/dagensmiddag_json/?campus=' + campus.lower())
        data = r.json()
        week_number = data.keys()[0]
        week_day = [
            'mandag',
            'tirsdag',
            'onsdag',
            'torsdag',
            'fredag',
            'fredag',
            'fredag',
        ][datetime.datetime.today().weekday()]
        return data[week_number][week_day]

    for campus in 'Hangaren', 'Realfag':
        phenny.say('_' + campus + '_: ' +
                   ' | '.join(filter(lambda x: x,
                              get_menu_for_campus(campus).split('\n'))))

middag.commands = ['middag']
