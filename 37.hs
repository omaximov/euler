import Data.Numbers.Primes as P
import Data.Digits as D
import Data.List

truncateNumber :: Int -> [Int]
truncateNumber x =
  let xs = (inits $ D.digits 10 x) ++ (tails $ D.digits 10 x)
  in
    [D.unDigits 10 y | y <- xs, not (null y), D.unDigits 10 y /= x]++[x]

truncatablePrime :: Int -> Bool
truncatablePrime n = all P.isPrime (truncateNumber n)
