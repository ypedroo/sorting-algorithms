
from mrjob.job import MRJob

class MRWordFreqCount(MRJob):
    def mapper(self, _,line):
        for word in line:
            yield word, 1
    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordFreqCount.run()
