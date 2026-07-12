package main

import "fmt"

func main() {
	mybill := newBill("Faraz")
	addItem(&mybill, "eggs", 260)
	addItem(&mybill, "milk", 170)
	addItem(&mybill, "duck", 500)
	addItem(&mybill, "suga", 69.69)

	// &mybill <- & makes sure that the memory address is being passed.
	addTip(&mybill, 0.31)
	whatsMyTotal(&mybill)
	fmt.Println(mybill)
}
