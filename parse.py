import csv
import glob
import os

from bs4 import BeautifulSoup


def extract_table(rider_file):
    with open(rider_file, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table.riderRanking__table")

    headers = [th.text.encode("utf-8") for th in table.select("tr th")]

    filename = os.path.split(rider_file)[1].split(".")[0]

    with open("data/csv/" + filename + ".csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])
    print("Wrote {}.csv!".format(filename))


def main():
    if not os.path.exists('data/csv'):
        os.mkdir('data/csv')

    for rider_file in glob.glob("./data/*/*"):
        extract_table(rider_file)


if __name__ == "__main__":
    main()
