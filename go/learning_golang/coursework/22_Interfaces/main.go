package main

import (
	"fmt"
	"math"
)

type shape interface {
	area() float64
	circumf() float64
}

type square struct {
	length float64
}

type circle struct {
	radius float64
}

// Square hole...
func (s square) area() float64 {
	return s.length * s.length
}

func (s square) circumf() float64 {
	return s.length * 4
}

// Sq... Circle hole...
func (c circle) area() float64 {
	return math.Pi * math.Pow(c.radius, 2)
}

func (c circle) circumf() float64 {
	return 2 * math.Pi * c.radius
}

func printShapeInfo(s shape) {
	fmt.Printf("Area of %T is: %0.2f \n", s, s.area())
	fmt.Printf("Circumference of %T is: %0.2f \n", s, s.circumf())
}

func main() {
	shapes := []shape{
		square{length: 15.2},
		square{length: 5.1},
		circle{radius: 3.14},
		circle{radius: 1},
		square{length: 121.2},
		square{length: 5.231},
		circle{radius: 12.14},
		circle{radius: 12132},
		square{length: 121542},
		square{length: 30.1341},
		circle{radius: 3.444},
		circle{radius: 100},
		square{length: 1522},
		square{length: 100541},
		circle{radius: 3.34344},
		circle{radius: 34},
		square{length: 1511.2},
		square{length: 5340},
		circle{radius: 1919},
		circle{radius: 3434},
	}

	for index, shape := range shapes {
		fmt.Printf("Shape number %v -> %v", index, shape)
		printShapeInfo(shape)
	}
}
