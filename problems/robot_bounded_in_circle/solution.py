
class RobotState:
    def __init__(self, x, y, direction: str = 'UP'):
        self.x = 0
        self.y = 0
        self.direction = direction
    
    def receive_instruction(self, instruction: str):
        if instruction == 'L':
            if self.direction == 'UP':
                self.direction = 'LEFT'
            elif self.direction == 'LEFT':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'RIGHT'
            elif self.direction == 'RIGHT':
                self.direction = 'UP'
        elif instruction == 'R':
            if self.direction == 'UP':
                self.direction = 'RIGHT'
            elif self.direction == 'RIGHT':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'LEFT'
            elif self.direction == 'LEFT':
                self.direction = 'UP'        
        elif instruction == 'G':
            if self.direction == 'UP':
                self.y += 1
            elif self.direction == 'LEFT':
                self.x -= 1
            elif self.direction == 'DOWN':
                self.y -= 1
            elif self.direction == 'RIGHT':
                self.x += 1

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions*4
        state = RobotState(0, 0, 'UP')
        for c in instructions:
            state.receive_instruction(c)
        if state.x == 0 and state.y == 0:
            return True
        return False
                
                
                