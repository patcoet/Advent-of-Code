subsOfLength :: Int -> String -> [String]
subsOfLength n str
  | length str < n = []
  | otherwise = take n str : subsOfLength n (tail str)

isMirrored :: String -> Bool
isMirrored [a, b, c, d] = a /= b && a == d && b == c

containsAbba :: String -> Bool
containsAbba str = any isMirrored $ subsOfLength 4 str

divide :: String -> String -> (String, String)
divide str hyper
  | elem '[' str = next
  | otherwise = (str, hyper)
  where
    part1 = takeWhile (/= '[') str ++ " " ++ tail (dropWhile (/= ']') str)
    part2 = tail $ dropWhile (/= '[') (takeWhile (/= ']') str) ++ " "
    next = divide part1 (hyper ++ part2)

supportsTls :: String -> Bool
supportsTls ip = containsAbba (fst parts) && not (containsAbba $ snd parts)
  where
    parts = divide ip ""

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\07\\input.txt"
  print $ length $ filter (== True) $ map supportsTls $ lines input