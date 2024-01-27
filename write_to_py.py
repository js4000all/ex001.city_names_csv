import app_from_csv as apc

def main() -> None:
    with open('zipcode.py', 'w') as w:
        w.write("import app_from_csv as apc\n")
        w.write("data = [\n")
        for code in apc.read_zipcode_from_csv('data/utf_ken_all.csv'):
            w.write(f'  apc.{code},\n')
        w.write("]\n")

if __name__=='__main__':
    main()
