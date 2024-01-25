import csv
import dataclasses as dc
import typing as ty

@dc.dataclass
class City:
    code: str
    name: str
    prefecture: str
    prefecture_code: str

def read_cities_from_csv(file_path: str) -> ty.Iterator[City]:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            city = City(code=row[0], name=row[1], prefecture=row[2], prefecture_code=row[3])
            yield city

def main() -> None:
    # csv from https://postaladdress.jp/municipality/download
    cities = read_cities_from_csv('data/2023-12-29.143241.5587175873201664418617.csv')
    print(len(list(cities)))

if __name__=='__main__':
    main()
