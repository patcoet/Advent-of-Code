data Direction = North | East | South | West

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

main = do
  input <- readFile "input.txt"
  let steps = countSteps (words (filter (/= ',') input)) 0 0 0 0 North
  let updown = abs ((steps !! 0) - (steps !! 2))
  let leftright = abs ((steps !! 1) - (steps !! 3))
  putStrLn (show (updown + leftright))
