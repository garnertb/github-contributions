import json
import requests
from bs4 import BeautifulSoup

GITHUB_URL = 'https://github.com/'


def get_contributions(usernames):
    """
    Get a github user's public contributions.
    :param usernames: A string or sequence of github usernames.
    """
    contributions = {'users': [], 'total': 0}

    if isinstance(usernames, str) or isinstance(usernames, unicode):
        usernames = [usernames]

    for username in usernames:
        response = requests.get('{0}{1}'.format(GITHUB_URL, username))

        if not response.ok:
            contributions['users'].append({username: dict(total=0)})
            continue

        bs = BeautifulSoup(response.content, "html.parser")
        total = bs.find('div', {'class': 'contributions-calendar'}).findPrevious('h3')
        contributions['users'].append({username: dict(total=int(total.text.split()[0].replace(',', '')))})
        contributions['total'] += int(total.text.split()[0].replace(',', ''))

    return json.dumps(contributions, indent=4)

