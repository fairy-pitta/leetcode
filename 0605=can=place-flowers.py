class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        li = [0] + flowerbed + [0]
        pos = 0

        cur = 0
        while cur < len(li):
            print(cur)
            if li[cur] == 0:
                cnt = 0
                while cur < len(li) and li[cur] == 0:
                    cnt += 1
                    cur += 1
                pos += (cnt-1)//2
            else:
                cur += 1
        
        print(pos)
        if pos >= n:
            return True
        return False

                
                
        