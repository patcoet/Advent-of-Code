import Data.Char
import Data.List
import System.Environment

data ListItem = L [ListItem] | I Int
  deriving (Read, Show)

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

groupParsedLines :: [ListItem] -> [(ListItem, ListItem)]
groupParsedLines (l1:l2:[]) = [(l1, l2)]
groupParsedLines (l1:l2:ls) = (l1, l2) : groupParsedLines ls

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let grouped = groupParsedLines $ parseLines $ filter (/= "") $ lines input
  print $ sum [n + 1 | n <- [0 .. length grouped - 1], checkPair' [fst $ grouped !! n] [snd $ grouped !! n] == True]
