parse :: String -> (String, Int)
parse str = case elem 'x' str of
  True -> parse $ pre ++ rep post param1 param2
  False -> (str, length str)
  where
    pre = takeWhile (/= '(') str
    post = tail $ dropWhile (/= ')') str
    param1 = read (takeWhile (/= 'x') $ tail $ dropWhile (/= '(') str) :: Int
    param2 = read (takeWhile (/= ')') $ tail $ dropWhile (/= 'x') str) :: Int

rep :: String -> Int -> Int -> String
rep str a b = replace '(' '[' (replace 'x' 'X' $ replace ')' ']' replicated) ++ drop a str
  where
    replicated = concat $ replicate b $ take a str
    replace c1 c2 s = case elem c1 s of
      True -> replace c1 c2 $ takeWhile (/= c1) s ++ [c2] ++ tail (dropWhile (/= c1) s)
      False -> s

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\09\\input.txt"
  print $ parse $ concat $ lines input
