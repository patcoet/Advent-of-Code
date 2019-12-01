import Data.Char
import qualified Data.Set as S
import Numeric
import Debug.Trace

-- Given "123-456", returns (123, 456)
parseLine input = (a, b)
  where a = read (takeWhile isDigit input) :: Int
        b = read (tail $ dropWhile isDigit input) :: Int

parse input = map parseLine $ lines input

numIsBlockedBy num (a, b) = num >= a && num <= b

nonBlockedNumbers blockList = [x | x <- [0..], all (== False) $ map (numIsBlockedBy x) blockList]

thing x blockList = case all (== False) $ map (numIsBlockedBy x) blockList of
  True -> x
  False -> case mod x 10000 == 0 of
    True -> trace ("Tried " ++ show x ++ "; blocklist length is " ++ show (length blockList)) $ thing (x+1) $ filter (\(a, b) -> b >= x) blockList
    False -> thing (x+1) blockList

isSubsetOf (a, b) (x, y) = a >= x && b <= y

-- Given a list of filters, returns the filters that are wholly contained within other filters
redundantFilters filterList = [x | x <- filterList, any (== True) [isSubsetOf x y | y <- filterList, x /= y]]

-- -- Given two filters, combine them if possible, returning either Nothing or Just (a+b)
-- combineFilters (a, b) (x, y) = case a >
--   case a < x of
--   True -> if b >= x then Just (a, y) else Nothing
--   False -> if y <= b then Just (x, b) else Nothing

main = do
  input <- readFile "input.txt"
  let filters = parse input
  let rfilters = redundantFilters filters
  let filters2 = filter (\x -> notElem x rfilters) filters
  print $ thing 0 filters2
  -- print $ filter (\x -> elem x rfilters) filters