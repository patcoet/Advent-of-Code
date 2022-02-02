import Data.Char
import Data.List
import Data.List.Split

lineToSortedLetters :: String -> [Char]
lineToSortedLetters str = sort (concat (init (splitOn "-" str)))

letNum :: [Char] -> [(Char, Int)] -> [(Char, Int)]
letNum [] pairs = reverse pairs
letNum (c : cs) pairs = letNum (dropWhile (== c) cs) ((c, length (filter (== c) cs) + 1) : pairs)

sortedTuples :: [(Char, Int)] -> [(Char, Int)]
sortedTuples xs = sortBy (\(_, x) (_, y) -> compare y x) xs

fiveMostCommonLetters :: String -> [Char]
fiveMostCommonLetters str = map fst $ take 5 (sortedTuples (letNum (lineToSortedLetters str) []))

isARealRoom :: String -> Bool
isARealRoom str = init (tail (dropWhile (/= '[') str)) == fiveMostCommonLetters str

idNumber :: String -> Int
idNumber str = read (filter isDigit str) :: Int

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\04\\input.txt"
  let rooms = lines input
  let realRooms = filter isARealRoom rooms
  let sumOfRealIds = sum (map idNumber realRooms)
  print sumOfRealIds