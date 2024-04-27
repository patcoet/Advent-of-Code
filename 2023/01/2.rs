use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    let mut sum = 0;
    println!("{sum}");
    for line in input.lines() {
        let replaced = line
            .replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "4")
            .replace("five", "5e")
            .replace("six", "6")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e");
        let filtered = replaced.chars().filter(|x| x.is_digit(10));
        let digits = filtered.collect::<Vec<char>>();
        let first_and_last = vec![digits[0], *digits.last().unwrap()];
        let value = first_and_last
            .iter()
            .collect::<String>()
            .parse::<u32>()
            .unwrap();
        sum += value;
        println!("+ {value:>2} = {}", sum);
    }
}
