import heapq 

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info={} 
        self.cuisines_heap={}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings) : 
            self.food_info[food]=(cuisine, rating) 
            if cuisine not in self.cuisines_heap : 
                self.cuisines_heap[cuisine]=[] 
            heapq.heappush(self.cuisines_heap[cuisine], (-rating, food)) 

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food] 
        self.food_info[food]=(cuisine, newRating) 
        heapq.heappush(self.cuisines_heap[cuisine], (-newRating, food)) 

    def highestRated(self, cuisine: str) -> str:
        heap=self.cuisines_heap[cuisine] 
        while heap : 
            rating_neg, food = heap[0] 
            if self.food_info[food][1] == -rating_neg : 
                return food 
            heapq.heappop(heap) 
        return ""
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)