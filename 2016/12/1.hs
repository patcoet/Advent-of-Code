import Debug.Trace
import Text.Read

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\12\\input.txt"
  print $ thing 0 0 0 0 (lines input) 0

thing a b c d instrs i = case i >= length instrs of
  True -> a
  False -> case op of
    "cpy" -> case readMaybe arg1 :: Maybe Int of
      (Just x) -> case arg2 of
        "a" -> thing x b c d instrs (i + 1)
        "b" -> thing a x c d instrs (i + 1)
        "c" -> thing a b x d instrs (i + 1)
        "d" -> thing a b c x instrs (i + 1)
      Nothing -> case arg1 of
        "a" -> case arg2 of
          "a" -> thing a b c d instrs (i + 1)
          "b" -> thing a a c d instrs (i + 1)
          "c" -> thing a b a d instrs (i + 1)
          "d" -> thing a b c a instrs (i + 1)
        "b" -> case arg2 of
          "a" -> thing b b c d instrs (i + 1)
          "b" -> thing a b c d instrs (i + 1)
          "c" -> thing a b b d instrs (i + 1)
          "d" -> thing a b c b instrs (i + 1)
        "c" -> case arg2 of
          "a" -> thing c b c d instrs (i + 1)
          "b" -> thing a c c d instrs (i + 1)
          "c" -> thing a b c d instrs (i + 1)
          "d" -> thing a b c c instrs (i + 1)
        "d" -> case arg2 of
          "a" -> thing d b c d instrs (i + 1)
          "b" -> thing a d c d instrs (i + 1)
          "c" -> thing a b d d instrs (i + 1)
          "d" -> thing a b c d instrs (i + 1)
    "inc" -> case arg1 of
      "a" -> thing (a + 1) b c d instrs (i + 1)
      "b" -> thing a (b + 1) c d instrs (i + 1)
      "c" -> thing a b (c + 1) d instrs (i + 1)
      "d" -> thing a b c (d + 1) instrs (i + 1)
    "dec" -> case arg1 of
      "a" -> thing (a - 1) b c d instrs (i + 1)
      "b" -> thing a (b - 1) c d instrs (i + 1)
      "c" -> thing a b (c - 1) d instrs (i + 1)
      "d" -> thing a b c (d - 1) instrs (i + 1)
    "jnz" -> case readMaybe arg1 :: Maybe Int of
      (Just x) -> case x of
        0 -> thing a b c d instrs (i + 1)
        x -> thing a b c d instrs (i + (read arg2 :: Int))
      Nothing -> case arg1 of
        "a" -> case a /= 0 of
          True -> thing a b c d instrs (i + (read arg2 :: Int))
          False -> thing a b c d instrs (i + 1)
        "b" -> case b /= 0 of
          True -> thing a b c d instrs (i + (read arg2 :: Int))
          False -> thing a b c d instrs (i + 1)
        "c" -> case c /= 0 of
          True -> thing a b c d instrs (i + (read arg2 :: Int))
          False -> thing a b c d instrs (i + 1)
        "d" -> case d /= 0 of
          True -> thing a b c d instrs (i + (read arg2 :: Int))
          False -> thing a b c d instrs (i + 1)
  where
    instr = instrs !! i
    op = words instr !! 0
    arg1 = words instr !! 1
    arg2 = words instr !! 2
