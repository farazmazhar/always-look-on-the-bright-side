package main

import "fmt"

type bill struct {
	name  string
	items map[string]float64
	tip   float64
}

// format bill
func (b bill) format() string {
	formatted_sting := "Bill Breakdown: \n"
	var total float64 = 0

	for key, value := range b.items {
		formatted_sting += fmt.Sprintf("%-25v ...$%7v \n", key+":", value)
		total += value
	}

	formatted_sting += fmt.Sprintf("%-25v ...$%7.2f", "total:", total)

	return formatted_sting
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
