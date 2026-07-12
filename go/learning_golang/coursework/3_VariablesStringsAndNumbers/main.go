package main

import "fmt"

func main() {
	// strings
	var nameOne string = "mario"
	var nameTwo = "luigi"
	var nameThree string

	fmt.Println(nameOne)
	fmt.Println(nameTwo)
	fmt.Println(nameOne, nameTwo, nameThree)

	// nameOne = 25 <- This would be an error since not a string.

	nameOne = "peach"
	nameThree = "bowser"

	fmt.Println(nameOne, nameTwo, nameThree)

	// := is a short hand for var <varname> <datatype> = <value>
	// This short hand can't be used outside of the functions.
	nameFour := "yoshi"
	fmt.Println(nameFour)

	// ints
	var ageOne int = 20
	var ageTwo = 30
	ageThree := 40

	fmt.Println(ageOne, ageTwo, ageThree)

	// bits & memory
	// (int, int8, int16, int32, int64 / uint, uint8, uint16, uint32, uint64)
	// var numOne int8 = 255 <- This would fail.
	var numOne int16 = 255
	var numTwo int8 = -128
	var numThree uint = 2 // -2 would fail
	fmt.Println(numOne, numTwo, numThree)

	// (float32, float64)
	var scoreOne float32 = 25.3934
	var scoreTwo float64 = 329048902349324.32432432423 // Just use this won't make a big difference in terms of memory.
	scoreThree := 1.5                                  // Defaults to datatype to float64.

	// Can't do scoreOne+scoreTwo, types don't match.
	fmt.Println(scoreOne, scoreTwo, scoreThree, scoreTwo+scoreThree)
}
