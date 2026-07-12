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
		"Choose option (a - add item, t - tip, s - save bill): ",
		reader,
	)

	switch option {
	case "a":
		name, _ := getInput("Item  name: ", reader)
		price, _ := getInput("Item price: ", reader)

		fmt.Println(name, price)
		// b.addItem(name, price)
	case "t":
		tip, _ := getInput("Tip amount: ", reader)

		fmt.Println(tip)
		// b.updateTip(tip)
	case "s":
		fmt.Println("s")
	default:
		fmt.Println("Not a valid option...")
		promptOptions(b)
	}
}

func main() {
	mybill := createBill()
	promptOptions(mybill)
	fmt.Println(mybill.format())
}
