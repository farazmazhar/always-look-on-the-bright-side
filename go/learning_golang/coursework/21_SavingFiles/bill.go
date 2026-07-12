package main

import (
	"fmt"
	"os"
	"strings"
)

type bill struct {
	name  string
	items map[string]float64
	tip   float64
}

// With Reciever function with pointer...
func (b *bill) updateTip(tip float64) {
	b.tip = tip
}

func (b *bill) addItem(name string, price float64) {
	b.items[name] = price
}

// format bill
func (b *bill) format() string {
	var formatted_sting strings.Builder
	formatted_sting.WriteString("\n\t  --- Bill Breakdown ---\t\n")
	var total float64 = b.tip

	for key, value := range b.items {
		formatted_sting.WriteString(fmt.Sprintf("%-24v ...$ %7.2f \n", key+":", value))
		total += value
	}

	// ~38 chars long...
	formatted_sting.WriteString("-------------------------------------\n")
	formatted_sting.WriteString(fmt.Sprintf("%-24v ...$ %7.2f \n", "tip:", b.tip))
	formatted_sting.WriteString("-------------------------------------\n")
	formatted_sting.WriteString(fmt.Sprintf("%-24v ...$ %7.2f \n", "total:", total))
	formatted_sting.WriteString("-------------------------------------\n")

	return formatted_sting.String()
}

func (b *bill) save() {
	data := []byte(b.format())

	file_path := "21_SavingFiles/bills/" + b.name + ".txt"

	err := os.WriteFile(file_path, data, 0644)

	if err != nil {
		panic(err)
	}
	fmt.Printf("Your bill is saved at `%v`\n", file_path)
}

func newBill(name string) bill {
	b := bill{
		name:  name,
		items: map[string]float64{},
		tip:   0,
	}

	return b
}

func addItem(b *bill, name string, price float64) {
	// For Struct pointers, b = (*b) - Go automatically handles the (*b) part for clean syntax.
	b.items[name] = price
}

// *bill <- * pointer
func addTip(b *bill, tip_ float64) {
	// For Struct pointers, b = (*b) - Go automatically handles the (*b) part for clean syntax.
	(*b).tip = tip_
}

func whatsMyTotal(b *bill) {
	total := 0.0

	for _, prices := range b.items {
		total += prices
	}

	total += b.tip

	fmt.Println("Your total is", total)
}
