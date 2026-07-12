package main

import "fmt"

func main() {
	x := 0

	// Acts as a `while` loop.
	for x < 5 {
		fmt.Println("value of x is:", x)
		x++
	}

	// for i := 0; i < 5; i++ {
	// 	fmt.Println("value of i is:", i)
	// }
	for i := range 5 {
		fmt.Println("value of i is:", i)
	}

	names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}
	// for i := 0; i < len(names); i++ {
	// 	fmt.Println(names[i])
	// }
	for i := range names {
		fmt.Println(names[i])
	}

	for index, value := range names {
		fmt.Printf("The name %v is at index %v\n", value, index)
	}

	for _, value := range names {
		fmt.Printf("The name is %v\n", value)
		value = "new string" // This wouldn't update the slice since value is in a differnet scope.
	}

	fmt.Println(names)

}
