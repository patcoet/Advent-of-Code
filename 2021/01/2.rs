use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("input")?;
    let mut num_increases = 0;

    let nums: Vec<u32> = input.lines().map(|x| x.parse::<u32>().unwrap()).collect();

    for n in 3..nums.len() {
        let prev_sum: u32 = nums[n - 3..n].iter().sum();
        let new_sum: u32 = nums[n - 2..=n].iter().sum(); // =n: inclusive of n

        if n > 2 && new_sum > prev_sum {
            num_increases += 1;
        }
    }

    println!("{}", num_increases);
    Ok(())
}
