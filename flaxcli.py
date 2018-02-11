from urllib import parse, request
import xmltodict
import string
import collections


class FlaxCli:

    def query_word(self, word):
        word = word.lower()

        params = {
            'o': 'xml',
            'a': 'g',
            'rt': 'r',
            'sa': 'CollocationQuery',
            's': 'CollocationQuery',
            'c': 'collocations',
            's1.threshold': 0.5,
            's1.startNum': 0,
            's1.sampleNum': 100,
            's1.perPage': 100,
            's1.query': word,
            's1.dbName': 'Wikipedia'
        }

        uri = 'http://flax.nzdl.org/greenstone3/flax?' + parse.urlencode(params)

        xml = request.urlopen(uri).read().decode('UTF8')
        query = xmltodict.parse(xml, force_list=('colloSamples', 'colloType'))['page']['pageResponse']['colloQuery']

        if 'colloSamples' not in query:
            return []

        samples = query['colloSamples']
        collocations = []

        for sample in samples:
            if 'colloType' not in sample:
                continue

            if isinstance(sample['colloType'], collections.OrderedDict):
                sample['colloType'] = [sample['colloType']]

            for colloType in sample['colloType']:
                for collo in colloType['collo']:
                    collocations.append(collo['text'])

        return collocations

    def query_text(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

        unique_words = set(list(words))
        num_words = len(unique_words)

        _ret = []

        for i, word in enumerate(unique_words):
            cols = self.query_word(word)

            for col in cols:
                if col in text:
                    _ret.append(col)

            print('%.2f%%' % ((i / num_words) * 100))

        unique = list(set(_ret))
        return unique
