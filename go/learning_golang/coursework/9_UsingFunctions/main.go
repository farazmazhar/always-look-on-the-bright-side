package main

import (
	"fmt"
	"math"
)

func sayGreeting(name string) {
	fmt.Printf("Good morning, %v!\n", name)
}

func sayBye(name string) {
	fmt.Printf("Goodbye, %v!\n", name)
}

func cycleNames(names []string, f func(string)) {
	for _, name := range names {
		f(name)
	}
}

func circleArea(radius float64) float64 {
	return math.Pi * radius * radius
}

func main() {
	sayGreeting("faraz")
	sayGreeting("freeman")

	sayBye("faraz")
	sayBye("freeman")

	cycleNames([]string{"cloud", "tifa", "barret"}, sayGreeting)
	cycleNames([]string{"cloud", "tifa", "barret"}, sayBye)

	areaOne := circleArea(10.5)
	areaTwo := circleArea(150)

	fmt.Println(areaOne, areaTwo)
	fmt.Printf("CircleOne is %10.3f\nCircleTwo is %10.3f\n", areaOne, areaTwo)
}
