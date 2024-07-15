fun operandos(){

    val valor1 = 10
    val valor 2 = 4

    val resultado
    resultado = valor1 + valor2
    println($resultado)

    resultado = valor1 * valor2
    println($resultado)

    resultado = valor1 / valor2
    println($resultado)

}

fun operacoes_string() {
    val str1 = "Olá"
    val str2 = "Mundo"


    val concatenacao = str1 + " " + str2
    println("Concatenação: $concatenacao")
    val comprimento = concatenacao.length
    println("Comprimento: $comprimento")
    val caractere = concatenacao[1]
    println("Caractere na posição 1: $caractere")
    val maiusculas = concatenacao.uppercase()
    println("Maiúsculas: $maiusculas")
    val minusculas = concatenacao.lowercase()
    println("Minúsculas: $minusculas")
}

fun main(){
    operandos()
    operacoes_string()
}
