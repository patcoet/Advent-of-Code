data Direction = North | East | South | West deriving (Show)

countSteps :: [String] -> Int -> Int -> Int -> Int -> Direction -> [Int]
countSteps [] n e s w _ = [n, e, s, w]
countSteps (str:ss) n e s w dir = case dir of
  North -> case head str of 'L' -> countSteps ss n e s (w + num) West
                            'R' -> countSteps ss n (e + num) s w East
  East  -> case head str of 'L' -> countSteps ss (n + num) e s w North
                            'R' -> countSteps ss n e (s + num) w South
  South -> case head str of 'L' -> countSteps ss n (e + num) s w East
                            'R' -> countSteps ss n e s (w + num) West
  West  -> case head str of 'L' -> countSteps ss n e (s + num) w South
                            'R' -> countSteps ss (n + num) e s w North
  where num = read (tail str) :: Int

thing [] dir = []
thing (str:ss) dir = case dir of
  North -> case head str of 'L' -> (West, n) : thing ss West
                            'R' -> (East, n) : thing ss East
  East  -> case head str of 'L' -> (North, n) : thing ss North
                            'R' -> (South, n) : thing ss South
  South -> case head str of 'L' -> (East, n) : thing ss East
                            'R' -> (West, n) : thing ss West
  West  -> case head str of 'L' -> (South, n) : thing ss South
                            'R' -> (North, n) : thing ss North
  where n = read (tail str) :: Int

main = do
  input <- readFile "input.txt"
  let steps = countSteps (words (filter (/= ',') input)) 0 0 0 0 North
  let updown = abs ((steps !! 0) - (steps !! 2))
  let leftright = abs ((steps !! 1) - (steps !! 3))
  putStrLn (show (updown + leftright))
