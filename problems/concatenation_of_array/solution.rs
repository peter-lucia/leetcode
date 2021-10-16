impl Solution {
    fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![];
        result.extend(&nums);
        result.extend(&nums);
        return result;

    }
}