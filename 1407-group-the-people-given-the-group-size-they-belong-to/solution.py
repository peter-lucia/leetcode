
class Group:
    def __init__(self, size: int | None):
        self.size = size
        self.current_group_idx = 0
        self.elements = [[]]

    def add(self, unique_id: int):
        if len(self.elements[self.current_group_idx]) < self.size:
            self.elements[self.current_group_idx] \
                .append(unique_id)
        else:
            self.current_group_idx += 1
            self.elements.append([unique_id])


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        1. Create a new class called Group
        2. Group has a size attribute
        3. It has an add() method, that will add elements in groups, using
         their index as their unique id
        4. The group will spawn a new chunk when the size limit has been
         reached for that group

        """
        groups = {}
        for i, s in enumerate(groupSizes):
            if s not in groups:
                g = Group(size=s)
                g.add(i)
                groups[s] = g
            else:
                g = groups.get(s)
                g.add(i)
                groups[s] = g
        results = []
        for k,v in groups.items():
            results += [e for e in v.elements]
        return results




        
