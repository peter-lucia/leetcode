class Logger:

    def __init__(self):
        self.message_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_map:
            self.message_map[message] = timestamp
            return True
        if timestamp - self.message_map[message] < 10:
            return False
        
        self.message_map[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)