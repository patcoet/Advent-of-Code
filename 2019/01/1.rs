use std::fs;

fn main() {
  let contents = fs::read_to_string("input.txt").expect("Error reading file.");
  let mut reqs = Vec::new();

  for mass in contents
    .split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
  {
    reqs.push(mass / 3 - 2);
  }

  println!(
    "Sum of fuel requirements: {}",
    reqs.into_iter().sum::<i32>()
  );
}
