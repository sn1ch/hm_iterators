import json
import hashlib


def hashing(path):
    count = 0
    with open(path, encoding='utf8') as file:
        data = json.load(file)
        while count != len(data):
            byte = str.encode(data[count])
            hash = hashlib.md5(byte)
            yield hash.digest()
            count += 1


if __name__ == '__main__':
    for county in hashing('data/countries_and_link.json'):
        print(county)
