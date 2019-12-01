invert str = concat $ map show $ map (\x -> if x == '1' then 0 else 1) str

step str = str ++ "0" ++ (invert $ reverse str)

check c1 c2 = if c1 == c2 then "1" else "0"

checksum (c1:c2:[]) = if c1 == c2 then "1" else "0"
checksum (c1:c2:cs) = case c1 == c2 of
  True -> "1" ++ checksum cs
  False -> "0" ++ checksum cs

checksum' str = case even $ length cs of
  True -> checksum' cs
  False -> cs
  where cs = checksum str

generate minLength initialState = if length initialState < minLength then take minLength $ generate minLength $ step initialState else initialState

main = print $ checksum' $ generate 272 "10111011111001111"