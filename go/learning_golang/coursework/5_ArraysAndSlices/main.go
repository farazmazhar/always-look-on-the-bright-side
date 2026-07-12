package main

import "fmt"

func main() {
	// Has to be fixed length.
	// var ages [3]int = [3]int{20, 25, 30}
	// Short hand of above...
	var ages = [3]int{20, 25, 30}
	fmt.Println(ages, len(ages))

	names := [4]string{"yoshi", "mario", "peach", "bowser"}
	names[1] = "luigi"
	fmt.Println(names, len(names))

	// Slices (use arrays under the hood)
	var scores = []int{100, 50, 60}
	scores[2] = 25
	scores = append(scores, 85) // Returns a new slice, not update the existing.
	fmt.Println(scores, len(scores))

	// Slice ranges
	rangeOne := names[1:3]  // One, upto but not including three.
	rangeTwo := names[2:]   // Two till end.
	rangeThree := names[:3] // From start, upto but not including three.
	fmt.Println(rangeOne, rangeTwo, rangeThree)

	rangeOne = append(rangeOne, "koopa")
	fmt.Println(rangeOne)
}
