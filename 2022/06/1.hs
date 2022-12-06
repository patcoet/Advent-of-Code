import Data.List
import System.Environment

main = do
  args <- System.Environment.getArgs
  input <- readFile $ head $ args ++ ["input"]
  let n = 4
      isMarker x = nub x == x
      td x = take n $ drop x input
  print $ head [x + n | x <- [0 ..], isMarker $ td x]
