data Bot = Bot
  { id :: Int,
    lo :: Int,
    hi :: Int
  }
  deriving (Eq, Show)

parse :: String -> [Int]
parse str = case take 3 str of
  "bot" -> map (\x -> read x :: Int) [wrds !! 1, wrds !! 6, wrds !! 11]
  _ -> map (\x -> read x :: Int) [wrds !! 1, wrds !! 5]
  where
    wrds = words str

give :: [Bot] -> Int -> Int -> [Bot]
give bots id value = take id bots ++ [newBot] ++ drop (id + 1) bots
  where
    newBot = give' (bots !! id) value
    give' bot value = case bot of
      (Bot id 0 0) -> Bot id value 0
      (Bot id lo 0) -> Bot id (min value lo) (max value lo)

processInstruction :: [Bot] -> String -> [Bot]
processInstruction bots instruction = case ws !! 0 of
  "bot" -> case (ws !! 5, ws !! 10) of
    ("bot", "bot") -> give (give bots' (params !! 1) (lo $ bots !! id)) (params !! 2) (hi $ bots !! id)
    ("bot", "output") -> give bots' (params !! 1) (lo $ bots !! id)
    ("output", "bot") -> give bots' (params !! 2) (hi $ bots !! id)
    ("output", "output") -> bots'
  "value" -> give bots (params !! 1) (params !! 0)
  where
    ws = words instruction
    params = parse instruction
    id = params !! 0
    bots' = take id bots ++ [Bot id 0 0] ++ drop (id + 1) bots

processable :: [Bot] -> String -> Bool
processable bots instruction = case head ws of
  "value" -> True
  "bot" -> lo bot /= 0 && hi bot /= 0
  where
    ws = words instruction
    bot = bots !! (read (ws !! 1) :: Int)

finished :: [Bot] -> Bool
finished bots = any (\x -> lo x == 17 && hi x == 61) bots

processInstructions :: [Bot] -> [String] -> [String] -> [Bot]
processInstructions bots [] [] = bots
processInstructions bots [] (instr : uctions)
  | finished bots = bots
  | processable bots instr = processInstructions (processInstruction bots instr) [] uctions
  | otherwise = processInstructions bots [instr] uctions
processInstructions bots queue [] = processInstructions bots [] queue
processInstructions bots queue@(q : ueue) instructions@(instr : uctions)
  | finished bots = bots
  | processable bots q = processInstructions (processInstruction bots q) ueue instructions
  | processable bots instr = processInstructions (processInstruction bots instr) queue uctions
  | otherwise = processInstructions bots (instr : queue) uctions

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\10\\input.txt"
  let bots = map (\x -> Bot x 0 0) [0 .. 300]
  print $ filter (\x -> lo x == 17 && hi x == 61) $ processInstructions bots [] (lines input)