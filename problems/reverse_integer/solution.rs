impl Solution {
    pub fn reverse(mut x: i32) -> i32 {
    // example: let x = 32

    let mut is_neg: bool = false;
    if x < 0 {
        is_neg = true;
    }
    x = x.abs();
    let mut values: Vec<i32> = Vec::new();

    // vec = {2, 3}
    let mut i: u32 = 0;
    while (10 as i32).pow(i) <= x {
        values.push(x % 10);
        x /= 10;
    }
    // debug
    // println!("values = {0:?}", values);
    // reverse the vector
    values.reverse();


    let mut result: i64 = 0;

    // result = 0
    // result += 2*10**0
    // result += 3*10**1
    i = 0;
    for v in values {
        result += (v as i64)*(10 as i64).pow(i);
        if result > (2 as i64).pow(31) - 1 {
            return 0;
        }
        i += 1;
    }

    return if is_neg {-result as i32} else {result as i32}; 
    }
}