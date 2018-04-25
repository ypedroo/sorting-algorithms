from mrjob.job import MRjob
class MRFriendsByAge(MRjob):
    def mapper(self,_,line):
        (_,_,agr,numberOfFriends,) = line.split(',')

        yield agr, float(numberOfFriends)

    def reducer(self, age, values):
        total = 0
        numberOfFriends = 0

        for x in values:
            total += x
            numberOfFriends += 1
        
        yield age, total /numberOfFriends
if __name__ == '__main__':
    MRFriendsByAge.run()
    
