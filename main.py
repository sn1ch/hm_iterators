import json
from pprint import pprint


class My_iterator:
    def __init__(self, path):
        with open(path, encoding='utf8') as file:
            data = json.load(file)
            self.count = -1
            self.data = data
            self.result = []

    def __iter__(self):
        return self

    def __next__(self):
        URL = 'https://en.wikipedia.org/wiki/'
        if self.count == len(self.data) - 1:
            raise StopIteration
        self.count += 1
        country = str(self.data[self.count]['name']['common'])
        data = country + ' - ' + URL + country.replace(" ", "_")
        self.result.append(data)
        with open('data/countries_and_link.json', 'w', encoding='utf8') as file:
            json.dump(self.result, file, ensure_ascii=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    countries = My_iterator('data/countries.json')
    for item in countries:
        item
    pprint(countries.result)
