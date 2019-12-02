main = do
  input <- readFile "input.txt" -- Input file looks like "51360\n95527\n72603\n".
  let massList = map (\x -> read x :: Int) $ words input -- Turn into ["51360","95527","72603"], then [51360,95527,72603].
  let calculateFuel mass = (div mass 3) - 2 -- div x y returns x divided by y with decimals truncated.
  let fuelReq = foldr (\x y -> calculateFuel x + y) 0 massList -- For our short example input, the foldr operation here would be equivalent to calculateFuel 51360 + (calculateFuel 95527 + (calculateFuel 72603 + 0)).
  putStrLn $ "Sum of fuel requirements for all modules: " ++ show fuelReq
