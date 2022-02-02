use std::fs;

fn main() {
  let contents = fs::read_to_string("input.txt").expect("Error reading file.");
  let mut sum = 0;

  for mass in contents
    .split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
  {
    let mut fuel_amount = mass / 3 - 2;
    while fuel_amount > 0 {
      sum += fuel_amount;
      fuel_amount = fuel_amount / 3 - 2;
    }
  }

  println!("Sum of fuel requirements: {}", sum);
}
