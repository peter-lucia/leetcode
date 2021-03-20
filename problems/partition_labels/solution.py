class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        Find the overlap between each letters, construct the 
        partition sizes using the overlap information
        """
        n = len(S)
        # get the min and max position of each letter
        lookup = {}
        for i, letter in enumerate(S):
            lookup[letter] = {}
            lookup[letter]["max"] = i
        S = [c for c in S]
        S.reverse()
        for i, letter in enumerate(S):
            lookup[letter]["min"] = n-1-i
        positions = list(lookup.items())
                
        # sort by starting position
        positions.sort(key=lambda val: val[1]["min"])
        
        # get each partition index
        def get_partition_points(arr):
            n = len(arr)
            max_pos = arr[0][1]["max"]
            result = []
            for letter, info in arr[1:]:
                if info["min"] > max_pos:
                    # found a partition point
                    result.append(info["min"])
                max_pos = max(max_pos, info["max"])
            return result
        result1 = get_partition_points(positions)
        result1.append(n)
        result = []
        
        # get the length of each partition
        min_val = 0
        for each in result1:
            result.append(each - min_val)
            min_val = each
        return result
            
        
        
            