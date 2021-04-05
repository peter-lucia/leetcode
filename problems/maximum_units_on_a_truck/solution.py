class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # sort boxTypes by number of units per box decreasing
        boxTypes.sort(key=lambda val: val[1], reverse=True)
        # add a box into the truck until you reach the truck size
        units_added = 0
        boxes_added = 0
        box_idx = 0
        while boxes_added < truckSize:
            if boxTypes[box_idx][0] == 0:
                box_idx += 1
            if box_idx > len(boxTypes) - 1:
                break
            boxTypes[box_idx][0] -= 1
            units_added += boxTypes[box_idx][1]
            boxes_added += 1
        return units_added
            