class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        s_product = 1
        s_sum = 0
        for each in s:
            val = int(each)
            s_product *= val
            s_sum += val
        return s_product - s_sum