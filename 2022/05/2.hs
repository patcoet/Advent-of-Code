import Control.Lens.At
import Control.Lens.Setter
import Data.Char
import Data.List
import System.Environment

processInstr stacks (num:from:to:[]) = stacks'
  where
    from' = from - 1
    to' = to - 1
    stacks' = ix from' %~ drop num $ stacks''
    stacks'' = ix to' %~ (take num (stacks !! from') ++) $ stacks

processInstrs stacks (instr:instrs)
  | instrs == [] = processInstr stacks instr
  | otherwise = processInstrs (processInstr stacks instr) instrs

main = do
  args <- System.Environment.getArgs
  input <- readFile $ head $ args ++ ["input"]
  let
    sPart = lines $ takeWhile (not . isDigit) input
    stacks = filter (/= "") $ map (filter isLetter) $ transpose sPart
    iPart = lines $ dropWhile (/= 'm') input
    instrs = map (map read . filter (any $ not . isLetter) . words) iPart
  print $ map head $ processInstrs stacks instrs
