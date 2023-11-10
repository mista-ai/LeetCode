class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        places = sorted(score, reverse=True)
        places_dict = dict()
        for i in range(len(places)):
            if i > 2:
                places_dict[places[i]] = str(i + 1)
            elif i == 0:
                places_dict[places[i]] = 'Gold Medal'
            elif i == 1:
                places_dict[places[i]] = 'Silver Medal'
            else:
                places_dict[places[i]] = 'Bronze Medal'

        return [places_dict[x] for x in score]