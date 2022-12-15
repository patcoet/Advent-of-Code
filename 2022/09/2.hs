import Data.List

approach (x0, y0) (x1, y1)
  | x0 - x1 > 1 && y0 - y1 > 1 = (x0 - 1, y0 - 1)
  | x0 - x1 > 1 && y0 - y1 < -1 = (x0 - 1, y0 + 1)
  | x0 - x1 < -1 && y0 - y1 > 1 = (x0 + 1, y0 - 1)
  | x0 - x1 < -1 && y0 - y1 < -1 = (x0 + 1, y0 + 1)
  | x0 - x1 > 1 = (x0 - 1, y0)
  | x0 - x1 < -1 = (x0 + 1, y0)
  | y0 - y1 > 1 = (x0, y0 - 1)
  | y0 - y1 < -1 = (x0, y0 + 1)
  | otherwise = (x1, y1)

-- Given a list of coords where the first one has been moved, return the list with the move propagated:
propagate :: [(Int, Int)] -> [(Int, Int)]
propagate (c0:[]) = [c0]
propagate (c0:c1:cs) = c0 : nc1 : (tail $ propagate (nc1:cs))
  where nc1 = approach c0 c1

move coords dir = case dir of
  'U' -> (x, y - 1) : tail coords
  'L' -> (x - 1, y) : tail coords
  'R' -> (x + 1, y) : tail coords
  'D' -> (x, y + 1) : tail coords
  where (x, y) = head coords

moveAndPropagate coords dir = propagate $ move coords dir

recurse _ [] = []
recurse coords dirs = [result] ++ recurse result (tail dirs)
  where result = moveAndPropagate coords (head dirs)

main = do
  input <- readFile "input"
  let lines_ = lines input
      wordsed = map words lines_
      parsed = concat $ map (\x -> replicate (read $ x !! 1) $ head $ x !! 0) wordsed
      coords = replicate 10 (0, 0)
      moves = recurse coords parsed
  print $ length $ nub $ map last $ moves
