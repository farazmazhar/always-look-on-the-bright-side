package main

import "fmt"

func updateName(x string) {
	x = "wedge" // Updating the "copy"... not updating the original param that was passed.
	// return x <- This can be one solution...
}

func updateMenu(y map[string]float64) {
	y["coffee"] = 2.99
}

func main() {
	// Passed by Value
	name := "tifa"
	updateName(name) // Won't do anything since being passed by value.
	fmt.Println(name)

	// Passed by Reference
	menu := map[string]float64{
		"pie":       2.99,
		"ice cream": 69.69,
	}
	updateMenu(menu)
	fmt.Println(menu)
}
