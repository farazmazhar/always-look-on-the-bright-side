package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

		parsed_price, err := strconv.ParseFloat(price, 64)

		if err != nil {
			fmt.Println("The price must be a number...")
			promptOptions(b)
		}

		b.addItem(name, parsed_price)
		promptOptions(b)
	case "t":
		tip, _ := getInput("Tip amount: ", reader)

		parsed_tip, err := strconv.ParseFloat(tip, 64)

		if err != nil {
			fmt.Println("The tip must be a number...")
			promptOptions(b)
		}

		b.updateTip(parsed_tip)
		promptOptions(b)
	case "s":
		fmt.Println("Your final bill...", b.format())
	default:
		fmt.Println("Not a valid option...")
		promptOptions(b)
	}
}

func main() {
	mybill := createBill()
	promptOptions(mybill)
}
