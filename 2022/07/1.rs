use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    let lines = input.lines().collect::<Vec<&str>>();

    let mut dir_stack = vec![];
    let mut dirs_and_contents = HashMap::new();

    for i in 0..lines.len() {
        let line = lines[i];
        let words = line.split(" ").collect::<Vec<&str>>();

        if words[1] == "cd" {
            if words[2] == ".." {
                dir_stack.pop();
            } else {
                dir_stack.push(words[2]);
            }
        }

        if line == "$ ls" {
            let mut contents = vec![];

            for j in i + 1..lines.len() {
                let line2 = lines[j];
                let words2 = line2.split(" ").collect::<Vec<&str>>();
                let val;

                if words2[0] == "$" {
                    break;
                }

                if words2[0] == "dir" {
                    let full_path2 = format!("{}/{}", &dir_stack.join("/")[1..], words2[1]);
                    val = full_path2;
                } else {
                    val = words2[0].to_string();
                }

                contents.push(val);
            }

            let full_path = format!("{}", &dir_stack.join("/")[1..]);
            dirs_and_contents.insert(full_path, contents);
        }
    }

    let mut total_total = 0;

    for (_dir, contents) in &dirs_and_contents {
        let total = contents
            .iter()
            .map(|x| total_size(&dirs_and_contents, &x))
            .sum::<u32>();

        if total <= 100000 {
            total_total += total;
        }
    }

    println!("{}", total_total);
}

fn total_size(map: &HashMap<String, Vec<String>>, key: &str) -> u32 {
    match key.parse::<u32>() {
        Ok(x) => x,
        Err(_) => {
            let contents = map.get(key).unwrap();
            let mut total = 0;

            for content in contents {
                match content.parse::<u32>() {
                    Ok(x) => total += x,
                    Err(_) => total += total_size(map, content),
                }
            }

            total
        }
    }
}
