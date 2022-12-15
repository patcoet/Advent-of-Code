use std::cmp;
use std::collections::HashMap;
use std::fs;

#[derive(Eq, Debug, Hash, PartialEq, Ord, PartialOrd)]
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
            let mut is_start = false;
            let height = if chr == 'S' {
                is_start = true;
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
                dist: if is_start { 0 } else { 69420 },
            };

            nodes.insert((x as u32, y as u32), node);
        }
    }

    loop {
        let mut values = nodes
            .iter()
            .filter(|n| !n.1.visited)
            .collect::<Vec<(&(u32, u32), &Node)>>();
        values.sort_by(|a, b| a.1.dist.cmp(&b.1.dist));
        let (cx, cy, ch) = (values[0].1.x, values[0].1.y, values[0].1.height);

        let neighbor_coords = nodes
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
            let tent_dist = nodes.get(&(cx, cy)).unwrap().dist + 1;
            let new_dist = cmp::min(nodes.get(&nc).unwrap().dist, tent_dist);
            nodes.entry(nc).and_modify(|x| x.dist = new_dist);
        }

        nodes.entry((cx, cy)).and_modify(|x| x.visited = true);

        if nodes.get(&dest_coords).unwrap().visited {
            println!("{}", nodes.get(&dest_coords).unwrap().dist);
            break;
        }
    }
}
