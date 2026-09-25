class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        count = 0
        left = 0
        right = len(people)-1
        while left <=right:
            if people[left]+people[right] <= limit:
                left+=1
                right-=1
                count+=1
            elif people[left]+people[right] > limit:
                count+=1
                right-=1
            
        return count
