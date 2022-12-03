import Data.Char
import Data.List
import System.Environment

main = do
  args <- System.Environment.getArgs
  input <- lines <$> readFile (head $ args ++ ["input"]) -- Realized I could just do this instead of the readFile' stuff
  let grouped = map (take 3 . flip drop input) [0, 3 .. length input - 3]
  let badgeTypes = map (head . foldr1 intersect) grouped
  print $ sum $ map prio badgeTypes
  where prio x
          | ord x >= ord 'a' = ord x - ord 'a' + 1
          | otherwise = ord x - ord 'A' + 27
