import Data.List

columns :: [String] -> [String]
columns strs = case length $ head rest of
  0 -> [map head strs]
  _ -> map head strs : columns rest
  where
    rest = map tail strs

occurrences :: Char -> String -> Int
occurrences c str = length $ filter (== c) str

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\06\\input.txt"
  print $ map (\col -> maximumBy (\x y -> compare (occurrences x col) (occurrences y col)) col) $ columns $ lines input