impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut count = 0;
        for val in arr.iter() {
            if (val % 2 != 0) {
                count += 1;
                if (count >= 3) {
                    return true;
                }
            } else {
                count = 0;
            }
        }
        return false;
    }
}