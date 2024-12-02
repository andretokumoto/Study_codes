: fibonacci ( n -- ) 
  0 1 swap \ Inicializa os dois primeiros números da sequência (0 e 1) e coloca n no topo da pilha
  ?do \ Inicia um loop que executa n vezes
    . \ Imprime o número atual da sequência
    over + swap \ Calcula o próximo número da sequência e ajusta a pilha
  loop ; \ Fim do loop

\ Exemplo de uso: exibe os primeiros N números da sequência de Fibonacci, onde N é o número na pilha
5 
fibonacci \ Chama a palavra fibonacci com o argumento 5 