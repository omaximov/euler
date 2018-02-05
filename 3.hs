import Data.Numbers.Primes

factors :: (Integral a) => a -> [a]
factors x = [y | y <- [1..x-1], x`mod`y==0, isPrime y]
