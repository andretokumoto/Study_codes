  #= 
  Esta função tem os elementos básicos de variáveis e operações com string
  =#
  function operadores_basicos()
    # Definições de variáveis e tipos dinâmicos das mesmas
    mensagem = "Olá, mundo!"
    println(mensagem)
    println(typeof(mensagem))
    x = 1
    println(x)
    println(typeof(x))
    # Concatenação de strings
    mensagem1 = "Concatena "
    mensagem2 = "strings"
    println(mensagem1 * mensagem2)
    # A função trunc não arredonda, apenas trunca a expressão como definido (neste caso, como inteiro)
    println("trunc =", trunc(Int64, 3.99999))
end

# Função com elementos matemáticos
function operadores_matematicos(numero)
    # Operadores geométricos
    println("seno :", sin(numero))
    println("cosseno: ", cos(numero))
    # Operadores aritméticos
    println("raiz: ", sqrt(numero))
    println("exp: ", exp(numero))
end

# Função com elementos de comparação e repetição
function operadores_comparacao_e_repeticao(numero)
    continua = "s"
    fat = 1
    while continua == "s"
        println("Digite a opção:")
        println("1 - Fatorial")
        println("2 - Sair")
        opcao = readline()
        if opcao == "1"
            for i in 1:numero
                fat = fat * i
            end
            continua = "n"
            return fat
        elseif opcao == "2"
            continua = "n"
            return "nada"
        else
            println("Digite uma opção válida")
        end
    end
end

function main()
    println("Digite um número:")
    entrada = readline()  # Lê uma linha de entrada do usuário
    numero = parse(Float64, entrada)  # Converte a entrada para o tipo Float64
    operadores_basicos()
    operadores_matematicos(numero)
    println(operadores_comparacao_e_repeticao(numero))
end

main()
