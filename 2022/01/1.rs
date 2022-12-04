use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();

    let mut groups = vec![];
    let mut group = vec![];
    for line in input.lines() {
        if line.len() > 0 {
            group.push(line.parse::<u32>().unwrap());
        } else {
            groups.push(group);
            group = vec![];
        }
    }
    let sums = groups
        .iter()
        .map(|x| x.iter().sum::<u32>())
        .collect::<Vec<u32>>();

    println!("{:?}", sums.iter().reduce(std::cmp::max).unwrap());
}
