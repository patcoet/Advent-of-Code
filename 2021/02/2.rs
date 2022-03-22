use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let mut hor_pos = 0;
    let mut depth = 0;
    let mut aim = 0;

    let input = fs::read_to_string("input")?;

    for line in input.lines() {
        let parts: Vec<&str> = line.split(' ').collect();
        let cmd: &str = parts[0];
        let val: u32 = parts[1].parse()?;

        if cmd == "forward" {
            hor_pos += val;
            depth += aim * val;
        } else if cmd == "up" {
            aim -= val;
        } else if cmd == "down" {
            aim += val;
        }
    }

    println!("{}", hor_pos * depth);

    Ok(())
}
