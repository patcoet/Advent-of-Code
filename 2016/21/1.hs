swapPos index1 index2 str = case index1 > index2 of
  True -> swapPos index2 index1 str
  False -> part1 ++ l2 ++ part2 ++ l1 ++ part3
  where part1 = take index1 str
        l1    = [str !! index1]
        part2 = take (index2 - index1 - 1) $ drop (index1 + 1) str
        l2    = [str !! index2]
        part3 = drop (index2 + 1) str

swapLet letter1 letter2 str = case letter1 < letter2 of
  True -> swapPos index1 index2 str
  False -> swapPos index2 index1 str
  where index1 = fst $ head $ filter (\x -> snd x == letter1) $ zip [0..] str
        index2 = fst $ head $ filter (\x -> snd x == letter2) $ zip [0..] str

rotateL numSteps str = take (length str) $ drop numSteps $ concat $ repeat str

rotateR numSteps str = rotateL (mod (length str - numSteps) (length str)) str

rotateBasedOn letter str = rotateR (1 + index + additional) str
  where index = fst $ head $ filter (\x -> snd x == letter) $ zip [0..] str
        additional = if index >= 4 then 1 else 0

reverseFromTo index1 index2 str = part1 ++ reversed ++ part2
  where part1 = take index1 str
        reversed = reverse $ take (index2 - index1 + 1) $ drop index1 str
        part2 = drop (index2 + 1) str

move index1 index2 str = part1 ++ [letter] ++ part2
  where strMinus = filter (/= letter) str
        part1 = take index2 strMinus
        letter = str !! index1
        part2 = drop index2 strMinus

operate line startString = case take 2 $ words line of
    ["swap", "position"] -> swapPos (read arg1 :: Int) (read arg2 :: Int) startString
    ["swap", "letter"] -> swapLet (head arg1) (head arg2) startString
    ["rotate", "left"] -> rotateL (read arg1 :: Int) startString
    ["rotate", "right"] -> rotateR (read arg1 :: Int) startString
    ["rotate", "based"] -> rotateBasedOn (head arg1) startString
    ["reverse", _] -> reverseFromTo (read arg1 :: Int) (read arg2 :: Int) startString
    ["move", _] -> move (read arg1 :: Int) (read arg2 :: Int) startString
  where arg1 = case take 2 $ words line of
          ["rotate", "based"] -> words line !! 6
          _ -> words line !! 2
        arg2 = case head $ words line of
          "move"    -> words line !! 5
          "reverse" -> words line !! 4
          "swap"    -> words line !! 5
          _ -> ""

operates lines str = case lines of
  [] -> str
  (l:ls) -> operates ls $ operate l str

main = do
  input <- readFile "input.txt"
  print $ operates (lines input) "abcdefgh"