
class Solution:
	
	def containsDuplicate(self, nums: List[int]) ->  bool:
		"""
		create set
		if any num is already in the set
		return true
		otherwise return false
		"""
		
		s = set()
		
		for num in nums:
			if num in s:
				return True
			else:
				s.add(num)
		return False



				
	
	