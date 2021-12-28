"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # Approach: DFS
        # 1. Find the employee id
        # 2. Run DFS on the employee id, summing total importance along the way
        
        
        employees_map = {}
        
        for emp in employees:
            employees_map[emp.id] = emp
        
        desired_employee = employees_map[id]
        
        def dfs(employee: Employee, total: int):
            
            if not employee:
                return 0
            
            result = total + employee.importance
            
            for sub_id in employee.subordinates:
                result += dfs(employees_map[sub_id], total)
                
            return result
        
                
        return dfs(desired_employee, 0)
            
            
        