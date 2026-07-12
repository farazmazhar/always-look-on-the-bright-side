package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Helper function...
func getInput(prompt string, reader *bufio.Reader) (string, error) {
	fmt.Print(prompt)
	input, err := reader.ReadString('\n')

	return strings.TrimSpace(input), err
}

func createBill() bill {
	reader := bufio.NewReader(os.Stdin)

	name, _ := getInput("Create a new bill name: ", reader)

	b := newBill(name)
	fmt.Println("New bill created!!!")
	fmt.Println()

	return b
}

func promptOptions(b bill) {
	reader := bufio.NewReader(os.Stdin)

	option, _ := getInput(
		"Choose option (a - add item, s - save bill, t - tip): ",
		reader,
	)
	fmt.Println(option)
}

func main() {
	mybill := createBill()
	promptOptions(mybill)
	fmt.Println(mybill.format())
}
