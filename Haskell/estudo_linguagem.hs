--Primeiro contato com a linguagem 

--define main como função principal
module Main where

-- IO() define a função como entrada/saida
main :: IO () 
--main = putStrLn "Hello, world!"

main = do putStr "Qual seu nome: "
          nome <- getLine
          putStr "sua idade:"
          idade <- getLine
          putStrLn ("Ola, seu nome é " ++ nome++ " e sua idade é " ++idade++" anos")