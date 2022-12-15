data Tree = Coord (Int, Int) Int
  deriving Show

main = do
  input <- readFile "input"
  let trees = parse input
  print $ length $ filter (\x -> isVisible x trees) trees

parseLine :: Int -> String -> [Tree]
parseLine y line = [Coord (x, y) (read ([line !! x])) | x <- [0 .. length line - 1]]

parse :: String -> [Tree]
parse input = concat [parseLine y ((lines input) !! y) | y <- [0 .. length (lines input) - 1]]

isVisible :: Tree -> [Tree] -> Bool
isVisible (Coord (x, y) h) trees = clear ls || clear rs || clear us || clear ds
  where
    ls = filter (\(Coord (x0, y0) h0) -> x0 < x && y0 == y) trees
    rs = filter (\(Coord (x0, y0) h0) -> x0 > x && y0 == y) trees
    us = filter (\(Coord (x0, y0) h0) -> x0 == x && y0 < y) trees
    ds = filter (\(Coord (x0, y0) h0) -> x0 == x && y0 > y) trees
    clear dir = all (\(Coord (x0, y0) h0) -> h0 < h) dir
