import Data.Char

main = do
  input <- readFile "input.txt"
  print $ length $ react' $ filter (/= '\n') input

caseOf c
  | isLower c = "lower"
  | isUpper c = "upper"

react "" = ""
react (c:"") = [c]
react (c1:c2:str)
  | caseOf c1 /= caseOf c2 && toUpper c1 == toUpper c2 = react str
  | otherwise = c1 : react (c2:str)

react' str
  | (length $ react str) == length str = react str
  | otherwise = react' $ react str
