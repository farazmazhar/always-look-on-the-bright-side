package main

import "fmt"

func updateName(x string) {
	x = "wedge" // Updating the "copy"... not updating the original param that was passed.
	// return x <- This can be one solution...
}

func updateNameByPointer(x *string) {
	*x = "wedge" // Passed the pointer so the original value should be updated.
}

func main() {
	// Passed by Value
	name := "tifa"
	updateName(name) // Won't do anything since being passed by value.

	fmt.Println("memory address of the name is:", &name)
	// fmt.Println(name)

	name_address := &name
	fmt.Println("memory adress                :", name_address)
	fmt.Println("value at memory adress       :", *name_address)

	updateNameByPointer(name_address)
	fmt.Println("Updated name                 :", name)
}
