package main

import "fmt"

func main() {
	menu := map[string]float64{
		"soup":    4.99,
		"pie":     7.99,
		"salad":   3.99,
		"pudding": 3.55, // Adding comma here is not optional.
	}

	fmt.Println(menu)
	fmt.Println(menu["pie"])

	// Looping map
	for key, value := range menu {
		fmt.Println(key, "-", value)
	}

	// Ints as key type
	phonebook := map[int]string{
		3367279869: "faraz",
		3334551606: "mama",
		3334048419: "papa",
	}

	fmt.Println(phonebook)
	fmt.Println(phonebook[3367279869])

	phonebook[3367279869] = "its-a me..."
	fmt.Println(phonebook)

	phonebook[3334551606] = "mamama"
	fmt.Println(phonebook)
}
