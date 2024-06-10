#lang typed/racket

;codigo de hello world para primeiro contato com a linguagem
(define-type SrN (U String Number))
(: tog ((Listof SrN) -> String))
(define (tog l)
  (apply string-append
         (filter string? l)))
(tog (list 5 "hello "
           1/2 "from Racket" (sqrt -1)))