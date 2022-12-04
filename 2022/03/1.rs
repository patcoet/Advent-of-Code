use std::fs;

fn main() {
    let input = fs::read_to_string("test").unwrap();

    let mut sum = 0;

    for line in input.lines() {
        let (p1, p2) = line.split_at(line.len() / 2);
        for chr in p1.chars() {
            if p2.contains(chr) {
                if chr.is_lowercase() {
                    sum += chr as u32 - 'a' as u32 + 1;
                } else {
                    sum += chr as u32 - 'A' as u32 + 27;
                }
                break;
            }
        }
    }

    println!("{sum}");
}
