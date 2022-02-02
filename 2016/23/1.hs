import Text.Read

main = do
  input <- readFile "input.txt"
  print $ thing (7, 0, 0, 0) (lines input) 0

rSet n x (a, b, c, d) = case n of
  'a' -> (x, b, c, d)
  'b' -> (a, x, c, d)
  'c' -> (a, b, x, d)
  'd' -> (a, b, c, x)

rGet n (a, b, c, d) = case n of
  'a' -> a
  'b' -> b
  'c' -> c
  'd' -> d

cpy arg1 arg2 registers = case readMaybe arg1 :: Maybe Int of
  (Just x) -> rSet arg2 x registers
  Nothing  -> rSet arg2 (rGet (head arg1) registers) registers

inc arg1 registers = rSet arg1 ((rGet arg1 registers) + 1) registers

dec arg1 registers = rSet arg1 ((rGet arg1 registers) - 1) registers

instructionIsValid instruction = case words instruction of
  ["cpy", _, arg2] -> case readMaybe arg2 :: Maybe Int of
    (Just x) -> False
    _ -> True
  _ -> True

toggle instructionList index = case index < 0 || index >= length instructionList of
  True -> instructionList
  False -> case words instr of
    ["inc", arg1] -> take index instructionList ++ ["dec " ++ arg1] ++ drop (index+1) instructionList
    ["dec", arg1] -> take index instructionList ++ ["inc " ++ arg1] ++ drop (index+1) instructionList
    ["tgl", arg1] -> take index instructionList ++ ["inc " ++ arg1] ++ drop (index+1) instructionList
    ["cpy", arg1, arg2] -> take index instructionList ++ ["jnz " ++ arg1 ++ " " ++ arg2] ++ drop (index+1) instructionList
    ["jnz", arg1, arg2] -> take index instructionList ++ ["cpy " ++ arg1 ++ " " ++ arg2] ++ drop (index+1) instructionList
  where instr = instructionList !! index

thing registers@(a, b, c, d) instrs i = case i >= length instrs of
  True -> a
  False -> case instructionIsValid instr of
    True -> case op of
      "cpy" -> thing (cpy arg1 (head arg2) registers) instrs (i+1)
      "inc" -> thing (inc (head arg1) registers) instrs (i+1)
      "dec" -> thing (dec (head arg1) registers) instrs (i+1)
      "jnz" -> case readMaybe arg1 :: Maybe Int of
        (Just x) -> case x of
          0 -> thing registers instrs (i+1)
          x -> case readMaybe arg2 :: Maybe Int of
            (Just x) -> thing registers instrs (i+x)
            Nothing  -> case i + (rGet (head arg2) registers) >= length instrs of
              True -> a
              False -> thing registers instrs (i+(rGet (head arg2) registers))
        Nothing -> case arg1 of
          "a" -> case a /= 0 of
            True -> thing registers instrs (i+(read arg2 :: Int))
            False -> thing registers instrs (i+1)
          "b" -> case b /= 0 of
            True -> thing registers instrs (i+(read arg2 :: Int))
            False -> thing registers instrs (i+1)
          "c" -> case c /= 0 of
            True -> thing registers instrs (i+(read arg2 :: Int))
            False -> thing registers instrs (i+1)
          "d" -> case d /= 0 of
            True -> thing registers instrs (i+(read arg2 :: Int))
            False -> thing registers instrs (i+1)
      "tgl" -> case readMaybe arg1 :: Maybe Int of
        (Just x) -> thing registers (toggle instrs $ i+x) (i+1)
        Nothing  -> thing registers (toggle instrs $ i+(rGet (head arg1) registers)) (i+1)
    False -> thing registers instrs (i+1)
  where instr = if i < length instrs then instrs !! i else instrs !! 0
        op = words instr !! 0
        arg1 = words instr !! 1
        arg2 = words instr !! 2