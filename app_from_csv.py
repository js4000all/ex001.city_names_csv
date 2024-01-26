import csv
import dataclasses as dc
import typing as ty

@dc.dataclass
class ZipCode:
    code: str
    prefecture: str
    city: str
    street: str

def read_zipcode_from_csv(file_path: str) -> ty.Iterator[ZipCode]:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            city = ZipCode(code=row[2], prefecture=row[6], city=row[7], street=row[8])
            yield city

def main() -> None:
    # csv from https://postaladdress.jp/municipality/download
    codes = read_zipcode_from_csv('data/utf_ken_all.csv')
    print(len(list(codes)))

if __name__=='__main__':
    main()
