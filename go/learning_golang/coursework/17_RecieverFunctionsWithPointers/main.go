package main

import "fmt"

func main() {
	mybill := newBill("Faraz")
	mybill.addItem("eggs", 259.99)
	mybill.addItem("milk", 171.01)
	mybill.addItem("duck", 499.99)
	mybill.addItem("suga", 69.69)

	mybill.updateTip(0.31)

	fmt.Println(mybill.format())
}
