/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; ++i) {
    let current_num = nums[i]
    let needed_num = target - current_num;
    if (map.has(needed_num)) {
      return [i, map.get(needed_num)];
    }
    map.set(current_num, i);
  }
  return [-1, -1];

};