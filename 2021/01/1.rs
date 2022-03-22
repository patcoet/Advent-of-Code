use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("input")?;
    let mut prev_num = 0;
    let mut num_increases = 0;

    for (n, line) in input.lines().enumerate() {
        if n > 0 && line.parse::<u32>()? > prev_num {
            num_increases += 1;
        }
        prev_num = line.parse::<u32>()?;
    }

    println!("{}", num_increases);
    Ok(())
}
