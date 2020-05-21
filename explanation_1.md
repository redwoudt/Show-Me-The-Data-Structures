# Explanation on data structures used

I used a cache dict to allow for O(1) assess to the key-value pair.

I used a deque plus a dict counter to keep track of the lru value, this allows for O(1) removals on average 
for the lru value plus it gives O(1) to store the value for reference.

Space complexity would be O(n), where we will have 3 data structures that all have O(n)
