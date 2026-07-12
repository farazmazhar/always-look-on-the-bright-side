package main

import "fmt"

func main() {
	age := 45

	fmt.Println(age <= 50)
	fmt.Println(age >= 50)
	fmt.Println(age == 45)
	fmt.Println(age != 50)

	if age < 30 {
		fmt.Println("The age is less than 30...")
	} else if age < 40 {
		fmt.Println("The age is less than 40...")
	} else {
		fmt.Println("The age is not less than 40...")
	}

	names := []string{"mario", "luigi", "yoshi", "peach", "bowser"}

	for index, value := range names {
		if index == 1 {
			fmt.Println("Continuing at pos", index)
			continue
		}
		if index > 2 {
			fmt.Printf("Breaking at %v :(\n", index)
			break
		}

		fmt.Printf("The value at pos %v is %v...\n", index, value)
	}
}
