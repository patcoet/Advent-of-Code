triples row = [('.', row !! 0, row !! 1)] ++ [(row !! (i-1), row !! i, row !! (i+1)) | i <- [0 .. length row], i > 0, i < (length row) - 1] ++ [(row !! (length row - 2), row !! (length row - 1), '.')]

trapOrNot triple = case triple of
  ('^', '^', '.') -> '^'
  ('.', '^', '^') -> '^'
  ('^', '.', '.') -> '^'
  ('.', '.', '^') -> '^'
  _               -> '.'

nextRow startRow = map trapOrNot $ triples startRow

rows startingRow = [startingRow] ++ rows (nextRow startingRow)

countSafeTiles rows = length $ filter (== '.') $ concat rows

main = do
  input <- readFile "input.txt"
  print $ countSafeTiles $ take 40 $ rows $ init input