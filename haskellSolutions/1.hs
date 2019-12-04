import Data.List (union)

threeAndFive :: Int -> Int
threeAndFive limit = sum $ filter (<limit) $ union [3*x | x <- [1..limit]]  [5*x | x <- [1..limit]]