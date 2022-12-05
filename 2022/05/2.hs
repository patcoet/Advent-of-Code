import Data.Char
import Data.List
import System.Environment

processInstr stacks (num:from:to:[]) 
  | from < to = pre ++ [newFrom] ++ mid ++ [newTo] ++ post
  | otherwise = pre ++ [newTo] ++ mid ++ [newFrom] ++ post
  where newFrom = drop (num + 1) (stacks !! from)
        newTo = (take (num + 1) (stacks !! from)) ++ stacks !! to
        sm = min from to
        la = max from to
        pre = take sm stacks
        post = drop (la + 1) stacks
        mid = take (la - sm - 1) $ drop (sm + 1) stacks

processInstrs stacks (instr:instrs)
  | instrs == [] = processInstr stacks instr
  | otherwise = processInstrs (processInstr stacks instr) instrs

main = do
  args <- System.Environment.getArgs
  input <- readFile $ head args
  let stacks = filter (/= "") $ map (filter isLetter) $ transpose $ lines $ takeWhile (not . isDigit) input
  let instrs = map (map ((\x -> x - 1) . \x -> read x :: Int) . filter ((\x -> not $ elem x ["move", "from", "to"])) . words) $ lines $ dropWhile (/= 'm') input
  print $ map head $ processInstrs stacks instrs
