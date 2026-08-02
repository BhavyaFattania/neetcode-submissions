class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        def time_taken(capacity,weights,days):
            
            days_taken =0
            day_capacity = capacity
            i=0
            
            while i <len(weights):
                while day_capacity >0 and i<len(weights) and weights[i] <=day_capacity:
                    day_capacity-=weights[i]
                    i+=1
                days_taken+=1
                if days_taken > days:
                    return False
                day_capacity = capacity
    
            if days_taken > days:
                return False
            elif days_taken <=days:
                return True

            
        while low <=high:
            mid = (low+high)//2
            can_ship = time_taken(mid,weights,days)
            if can_ship:
                high = mid-1
            else:
                low = mid+1
        return low