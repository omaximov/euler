fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

evenFibsSum :: Int -> Int
evenFibsSum limit = sum $ filter (even) $ takeWhile (<limit) fibs
