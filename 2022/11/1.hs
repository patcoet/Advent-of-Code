import Control.Lens.At
import Control.Lens.Setter
import Data.Char
import Data.List
import System.Environment

data Monkey = Monkey Int [Int] (Int -> Int) (Int -> Bool) Int Int Int
instance Ord Monkey where
  compare (Monkey _ _ _ _ _ _ insps1) (Monkey _ _ _ _ _ _ insps2) = compare insps1 insps2
instance Eq Monkey where
  (==) (Monkey _ _ _ _ _ _ insps1) (Monkey _ _ _ _ _ _ insps2) = insps1 == insps2

parseMonkey :: [String] -> Monkey
parseMonkey (l0:l1:l2:l3:l4:l5:[]) = Monkey num items op test ift iff 0
  where
    num = read $ init $ words l0 !! 1
    items = map read $ map (takeWhile isDigit) $ drop 2 $ words l1
    op = \x -> div ((if words l2 !! 4 == "+" then (+) else (*)) x (if isDigit (head (words l2 !! 5)) then read (words l2 !! 5) else x)) 3
    test = \x -> mod x (read (words l3 !! 3)) == 0
    ift = read $ last $ words l4
    iff = read $ last $ words l5

addItem :: Int -> Monkey -> Monkey
addItem item (Monkey num items op test ift iff insps) = Monkey num (items ++ [item]) op test ift iff insps

removeItems :: Monkey -> Monkey
removeItems (Monkey num items op test ift iff insps) = Monkey num [] op test ift iff (insps + length items)

processMonkey :: [Monkey] -> Monkey -> [Monkey]
processMonkey monkeys (Monkey _ [] _ _ _ _ _) = monkeys
processMonkey monkeys (Monkey num (item:items) op test ift iff insps) = processMonkey monkeys' monkey'
  where target = if test (op item) then ift else iff
        monkeys' = ix num %~ removeItems $ ix target %~ addItem (op item) $ monkeys
        monkey' = Monkey num items op test ift iff (insps + 1)

doRound :: [Monkey] -> Int -> [Monkey]
doRound monkeys n
  | n == length monkeys = monkeys
  | otherwise = doRound monkeys' $ n + 1
  where monkeys' = processMonkey monkeys (monkeys !! n)

doRounds :: [Monkey] -> Int -> [Monkey]
doRounds monkeys 0 = monkeys
doRounds monkeys n = doRounds (doRound monkeys 0) (n - 1)

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let monkeys = [parseMonkey $ take 6 $ drop n $ lines input | n <- 0:[7, 14 .. length $ lines input]]
      after20 = doRounds monkeys 20
      twoMostActive = take 2 $ sortBy (flip compare) after20
      insps (Monkey _ _ _ _ _ _ x) = x
  print $ foldr1 (*) $ map insps twoMostActive
