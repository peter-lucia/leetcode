use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        // Approach:
        // Iterate over each element in nums
        // Add each element to each existing subset in the result, creating
        // a new item in the powerset


        let mut result: Vec<Vec<i32>> = vec![];
        result.push(vec![]);

        for num in nums {
            for subset in result.clone() {
                let mut new_subset = subset.clone();
                new_subset.push(num);
                result.push(new_subset);
            }
        }
        return result;
    }
}

