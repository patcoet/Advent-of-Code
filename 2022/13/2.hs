import Data.Char
import Data.List
import System.Environment

data ListItem = L [ListItem] | I Int
  deriving (Eq, Read)

checkPair :: [ListItem] -> [ListItem] -> [Bool]
checkPair [] [] = []
checkPair [] _ = [True]
checkPair _ [] = [False]
checkPair (x:xs) (y:ys) = case (x, y) of
  (L x', L y') -> checkPair x' y' ++ checkPair xs ys
  (L _, I y') -> checkPair (x:xs) (L [I y']:ys)
  (I x', L _) -> checkPair (L [I x']:xs) (y:ys)
  (I x', I y') -> case compare x' y' of
    LT -> [True]
    GT -> [False]
    EQ -> checkPair xs ys

checkPair' xs ys = head $ checkPair xs ys

parseLine :: String -> ListItem
parseLine line = parsed
  where
    grouped = groupBy (\x y -> isDigit x && isDigit y) line
    f x = if x == "[" then "L [" else if isDigit (head x) then "I " ++ x else x
    replaced = concat $ map f grouped
    parsed = read replaced :: ListItem

parseLines :: [String] -> [ListItem]
parseLines (l:[]) = [parseLine l]
parseLines (l:ls) = parseLine l : parseLines ls

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let parsed = parseLines $ filter (/= "") $ lines input ++ ["[[2]]", "[[6]]"]
      sorted = sortBy (\x y -> if checkPair' [x] [y] == True then LT else GT) parsed
      isDivider x = x == parseLine "[[2]]" || x == parseLine "[[6]]"
  print $ foldr1 (*) [n + 1 | n <- [0 .. length sorted - 1], isDivider (sorted !! n)]
