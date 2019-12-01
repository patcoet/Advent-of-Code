import Data.Char

-- (name, used, avail)
parseLine line = (w 0, read (takeWhile isDigit $ w 2) :: Int, read (takeWhile isDigit $ w 3) :: Int)
  where w x = words line !! x

parse input = map parseLine $ drop 2 $ lines input

pairIsViable (a, b, c) (x, y, z) = b /= 0 && a /= x && b <= z

main = do
  input <- readFile "input.txt"
  let nodes = parse input
  print $ length $ [(x, y) | x <- nodes, y <- nodes, pairIsViable x y]