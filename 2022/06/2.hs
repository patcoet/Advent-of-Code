import Data.List
import System.Environment

main = do
  args <- System.Environment.getArgs
  input <- readFile $ head $ args ++ ["input"]
  let n = 14
      isMarker x = nub x == x
      td x = take n $ drop x input
  print $ fst $ head $ filter snd [(x + n, isMarker $ td x) | x <- [0 ..]]
