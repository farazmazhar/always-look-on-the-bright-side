package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	fmt.Println("Hello")

	greetings := "hello there, friends!"

	fmt.Println(strings.Contains(greetings, "hello"))
	fmt.Println(strings.ReplaceAll(greetings, "hello", "hola"))

	// Original string didn't get updated, strings.ReplaceAll returned an updated string.
	// fmt.Println(greetings)

	fmt.Println(strings.ToUpper(greetings))
	fmt.Println(strings.Index(greetings, "ll"))
	fmt.Println(strings.Index(greetings, "th"))
	fmt.Println(strings.Index(greetings, "xy")) // Returns -1
	fmt.Println(strings.Split(greetings, ","))

	ages := []int{45, 20, 35, 30, 75, 60, 50, 25}

	sort.Ints(ages) // Updates the original slice. What?
	fmt.Println(ages)

	index := sort.SearchInts(ages, 30)
	fmt.Println(index)
	index_90 := sort.SearchInts(ages, 90) // Returns where it would live in the list.
	fmt.Println(index_90)
	index_5 := sort.SearchInts(ages, 5) // Returns where it would live in the list.
	fmt.Println(index_5)
	index_49 := sort.SearchInts(ages, 49) // Returns where it would live in the list.
	fmt.Println(index_49)

	names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}
	sort.Strings(names)
	fmt.Println(names)

	fmt.Println(sort.SearchStrings(names, "bowser"))
	fmt.Println(sort.SearchStrings(names, "faraz"))

}
