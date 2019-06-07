import json
import hashlib


class My_iterator_hash:
    def __init__(self, path):
        with open(path, encoding='utf8') as file:
            data = json.load(file)
            self.count = -1
            self.data = data
            self.result = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.data) - 1:
            raise StopIteration
        self.count += 1
        byte = str.encode(self.data[self.count])
        hash = hashlib.md5(byte)
        return hash.digest()


if __name__ == '__main__':
    countries = My_iterator_hash('data/countries_and_link.json')
    for coutry in countries:
        print(coutry)

