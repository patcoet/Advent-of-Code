import Data.Char
import Data.List
import System.Environment

main = do
  args <- System.Environment.getArgs
  input <- lines <$> readFile' args
  let splitSacks = [splitAt (div (length x) 2) x | x <- input]
  let mistakes = [head $ intersect (fst x) (snd x) | x <- splitSacks]
  print $ sum [prio x | x <- mistakes]
  where readFile' [] = readFile "input"
        readFile' x = readFile $ head x
        prio x
          | ord x >= ord 'a' = ord x - ord 'a' + 1
          | otherwise = ord x - ord 'A' + 27
