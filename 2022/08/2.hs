import Data.List

data Tree = Coord {tx :: Int, ty :: Int, th :: Int}
  deriving Show

main = do
  input <- readFile "input"
  let trees = parse input
  print $ [scenicScore tree trees | tree <- trees]

parse :: String -> [Tree]
parse input = concat [parseLine y ((lines input) !! y) | y <- [0 .. length (lines input) - 1]]
  where parseLine y line = [Coord x y (read ([line !! x])) | x <- [0 .. length line - 1]]

scenicScore tree@(Coord x y h) trees = score tree u * score tree l * score tree r * score tree d
  where
    -- Half of these sorts might be unnecessary?
    -- I think the filtering is what takes time - maybe we want to store the values in a 2D array instead?
    -- Or one array of rows and one array of columns
    u = sortBy (\t1 t2 -> flip compare (ty t1) (ty t2)) $ filter (\t -> tx t == x && ty t < y) trees
    l = sortBy (\t1 t2 -> flip compare (tx t1) (tx t2)) $ filter (\t -> tx t < x && ty t == y) trees
    r = sortBy (\t1 t2 -> compare (tx t1) (tx t2)) $ filter (\t -> tx t > x && ty t == y) trees
    d = sortBy (\t1 t2 -> compare (tx t1) (tx t2)) $ filter (\t -> tx t == x && ty t > y) trees
    score tree [] = 0
    score tree trees = case th tree > th (head trees) of
      True -> 1 + score tree (tail trees)
      False -> 1
