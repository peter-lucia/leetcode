class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; ++i) {
            int current_num = nums[i];
            int needed_num = target - current_num;
            if (map.containsKey(needed_num)) {
                ans[0] = i;
                ans[1] = map.get(needed_num);
                return ans;
            }
            map.put(current_num, i);
        }
        ans[0] = -1;
        ans[1] = -1;
        return ans;
    }
}