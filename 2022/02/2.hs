import Data.Char
import System.Environment

-- This is harder to understand than my part 1 approach, but it looks nicer!
score abc xyz = sScore + oScore
  where ss = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]
        i = ord (head abc) - ord 'A'
        j = ord (head xyz) - ord 'X'
        sScore = (ss !! i) !! j
        oScore = [0, 3, 6] !! j

main = do
  args <- System.Environment.getArgs
  input <- fmap words <$> lines <$> readFile' args
  print $ sum [score (x !! 0) (x !! 1) | x <- input]
  where readFile' [] = readFile "input"
        readFile' x = readFile $ head x
