import System.Environment

sScore "X" = 1
sScore "Y" = 2
sScore "Z" = 3

oScore "A" "Y" = 6
oScore "A" "Z" = 0
oScore "B" "X" = 0
oScore "B" "Z" = 6
oScore "C" "X" = 6
oScore "C" "Y" = 0
oScore x y = 3

main = do
  args <- System.Environment.getArgs
  input <- fmap words <$> lines <$> readFile' args
  print $ sum [sScore (x !! 1) + oScore (x !! 0) (x !! 1) | x <- input]
  where readFile' [] = readFile "input"
        readFile' x = readFile $ head x
