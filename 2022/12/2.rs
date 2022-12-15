use std::cmp;
use std::collections::HashMap;
use std::fs;

#[derive(Clone, Eq, Debug, Hash, PartialEq, Ord, PartialOrd)]
struct Node {
    pub x: u32,
    pub y: u32,
    pub height: u32,
    pub visited: bool,
    pub dist: u32,
}

fn main() {
    let mut nodes: HashMap<(u32, u32), Node> = HashMap::new();
    let mut dest_coords = (0, 0);

    let input = fs::read_to_string("input").unwrap();
    for (y, line) in input.lines().enumerate() {
        for (x, chr) in line.chars().enumerate() {
            let height = if chr == 'S' {
                0
            } else if chr == 'E' {
                dest_coords = (x as u32, y as u32);
                'z' as u32 - 'a' as u32
            } else {
                chr as u32 - 'a' as u32
            };

            let node = Node {
                x: x as u32,
                y: y as u32,
                height: height,
                visited: false,
                dist: 69420,
            };

            nodes.insert((x as u32, y as u32), node);
        }
    }

    let start_currs = nodes
        .iter()
        .filter(|n| n.1.height == 0)
        .map(|n| (n.1.x, n.1.y, n.1.height))
        .collect::<Vec<(u32, u32, u32)>>();

    let mut steps_needed = vec![];

    dbg!(start_currs.len());
    let mut i = 0;

    // This is really slow since it redoes all the pathfinding for every element of start_currs,
    // but it's fast enough that I don't want to do it properly right now!
    for sc in start_currs {
        dbg!(i);
        i += 1;
        let mut loop_nodes = nodes.clone();
        let mut first_loop = true;
        loop {
            let (cx, cy, ch);
            if !first_loop {
                let mut values = loop_nodes
                    .iter()
                    .filter(|n| !n.1.visited)
                    .collect::<Vec<(&(u32, u32), &Node)>>();
                values.sort_by(|a, b| a.1.dist.cmp(&b.1.dist));
                (cx, cy, ch) = (values[0].1.x, values[0].1.y, values[0].1.height);
            } else {
                (cx, cy, ch) = sc;
                loop_nodes.entry((cx, cy)).and_modify(|n| n.dist = 0);
                first_loop = false;
            }

            let neighbor_coords = loop_nodes
                .iter()
                .filter(|n| !n.1.visited)
                .filter(|n| {
                    (cx as i32 - n.1.x as i32).abs() + (cy as i32 - n.1.y as i32).abs() <= 1
                        && !(n.1.x == cx && n.1.y == cy)
                })
                .filter(|n| n.1.height as i32 - ch as i32 <= 1)
                .map(|n| *n.0)
                .collect::<Vec<(u32, u32)>>();

            for nc in neighbor_coords {
                let tent_dist = loop_nodes.get(&(cx, cy)).unwrap().dist + 1;
                let new_dist = cmp::min(loop_nodes.get(&nc).unwrap().dist, tent_dist);
                loop_nodes.entry(nc).and_modify(|x| x.dist = new_dist);
            }

            loop_nodes.entry((cx, cy)).and_modify(|x| x.visited = true);

            if loop_nodes.get(&dest_coords).unwrap().visited {
                steps_needed.push(loop_nodes.get(&dest_coords).unwrap().dist);
                break;
            }
        }
    }

    println!(
        "{}",
        steps_needed
            .iter()
            .fold(steps_needed[0], |x, y| cmp::min(x, *y))
    );
}
