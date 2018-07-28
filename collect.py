import urllib2
import os

from bs4 import BeautifulSoup


def get_riders(link):
    response = urllib2.urlopen(link)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    rider_list = soup.select_one("div.list--competitors")

    for rider in rider_list.find_all("span", {"class": "runner"}):
        link = rider.a['href']
        name = link.split('/')[5]
        persona = rider.text.strip().title()
        team = link.split('/')[4]

        yield {"link": link,
               "name": name,
               "persona": persona.encode("utf-8"),
               "team": team}


def collect_rider(rider):
    response = urllib2.urlopen("https://www.letour.fr{}".format(rider["link"]))
    html = response.read()

    print("Now writing {}...".format(rider["persona"])),

    with open("data/{}/{}.html".format(rider['team'], rider['name']), 'w') as f:
        f.write(html)

    print("Done!")


def main():
    riders = get_riders("https://www.letour.fr/en/riders")

    for rider in riders:
        team_path = "./data/" + rider['team']
        if not os.path.exists(team_path):
            os.mkdir(team_path)
        collect_rider(rider)


if __name__ == "__main__":
    if not os.path.exists('data'):
        os.mkdir('data')
    main()
