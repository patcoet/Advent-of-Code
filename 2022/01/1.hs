import Data.List
import System.Environment

main = do
  args <- System.Environment.getArgs
  input <- readFile' args
  let groups = groupBy (\_ y -> y /= "") $ lines input
  let filteredGroups = map (filter (/= "")) groups
  let parsedGroups = map (map read) filteredGroups
  let sums = map sum parsedGroups
  print $ foldr1 max sums
  where readFile' [] = readFile "input"
        readFile' x = readFile $ head x
