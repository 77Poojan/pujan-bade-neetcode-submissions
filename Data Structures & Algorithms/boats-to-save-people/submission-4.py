class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)

        i = 0 
        j = n - 1
        boat = 0


        while i <= j:
            count = people[j] + people[i]
            if count <= limit:
                i += 1 
            boat += 1
            j -= 1
        
        return boat