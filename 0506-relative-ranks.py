class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_order = []

        for i in range(len(score)):
            rank_order.append([score[i], i])
        
        rank_order = sorted(rank_order, key = lambda x: x[0], reverse = True)

        for j in range(len(score)):
            if j == 0:
                rank_order[j].append("Gold Medal")
            elif j == 1:
                rank_order[j].append("Silver Medal")
            elif j == 2:
                rank_order[j].append("Bronze Medal")
            else:
                rank_order[j].append(str(j+1))
        
        ans_list = ["" for _ in range(len(score))]

        for k in range(len(score)):
            ans_list[rank_order[k][1]] = rank_order[k][2]
        
        return ans_list
        


        