class Solution(object):
    
    def isDigitLog(self, log):
        arr = log.split(" ")
        if len(arr) > 0:
            try:
                a = int(arr[1])
                return True
            except ValueError as e:
                return False
    
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        for log in logs:
            if self.isDigitLog(log):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs = sorted(letter_logs, key=lambda arr: (arr.split(' ')[1:], arr.split(' ')[0]))
        return letter_logs + digit_logs


            
            