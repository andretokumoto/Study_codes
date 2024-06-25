package main

import "fmt"

func test_String() {
			var palavra1,palavra2 string
	
			fmt.Println("Concatena"+" String")

			fmt.Println("Digite a primeira palavra")
			fmt.Scanln(&palavra1)	
			fmt.Println("Digite a segunda palavra")
			fmt.Scanln(&palavra2)
			fmt.Println(palavra1+" "+palavra2)
	
}

func main() {
	test_String()
}
