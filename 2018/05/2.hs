import Data.Char (toUpper)
import Data.List (sort)
import qualified Data.Text as T
import qualified Data.Text.IO as TIO

main = do
  input <- readFile "input.txt"
  let inputs = map T.pack $ map (\x -> filter (/= x) $ filter (/= (toUpper x)) $ init input) ['a' .. 'z']
  print $ head $ sort $ map (T.length . react) inputs

reactionPairs = map T.pack (aazz ++ map reverse aazz)
  where aazz = [[x] ++ [toUpper x] | x <- ['a' .. 'z']]

react input
  | T.length butt == T.length input = input
  | otherwise = react butt
  where butt = foldr (\x -> T.replace x T.empty) input reactionPairs
