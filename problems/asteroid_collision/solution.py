class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # first failed approach with stacks: two stacks, asteroids and result
        # pop asteroid from asteroids
        # put asteroid into result
        # check if top item of result and top item of asteroids conflict
        # put winner into result or remove both if they cancel out
        # continue until asteroids is empty and result is full
        
        
        # asteroids = [10, 2, -5]
        # result = []
        
        # asteroids = [-5]
        # result = [10, 2]
        
        # right = -5  # asteroids[0]
        # left = 2  # result[-1]
        
        # if right < 0 and left > 0:
        #    handle collision
        # otherwise:
        #    put right into top of result

                
        # second approach
        # start with i = 0, j = 1
        # check for collision between i and j
        # if no collision, increment both i and j
        # if collision, if elem at j wins, pop(i) and let i = j and j += 1
        # if collision and if elem at i wins, pop(j) and keep i and j the same
        # if collision and cancel each other out, pop(i), pop(j), let i -= 1, j = i 
        
        # can assume len(asteroids) >= 2
        i = 0
        j = 1
        
        while j < len(asteroids):
            if self.is_collision(asteroids[i], asteroids[j]):
                if abs(asteroids[i]) > abs(asteroids[j]):
                    asteroids.pop(j)
                elif abs(asteroids[i]) < abs(asteroids[j]):    
                    asteroids.pop(i)
                    if i > 0:
                        i -= 1
                        j -= 1
                elif asteroids[j] < 0 and abs(asteroids[j]) == abs(asteroids[j]):
                    asteroids.pop(i)
                    asteroids.pop(i) # elem at j is now at i
                    if i > 1:
                        i -= 2
                        j -= 2
                    elif i > 0:
                        i -= 1
                        j -= 1
            else:
                i += 1
                j += 1
        return asteroids
                    
            
    def is_collision(self, left, right):
        return right < 0 and left > 0
        
            
        
        