package main

import (
	"fmt"
	"strings"
)

func getInitials(name string) (string, string) {
	upper_name := strings.ToUpper(name)
	split_name := strings.Split(upper_name, " ")

	var initials []string

	for _, value := range split_name {
		initials = append(initials, value[:1])
	}

	if len(initials) > 1 {
		return initials[0], initials[1]
	}

	return initials[0], "_"
}

func main() {
	first_name_one, second_name_one := getInitials("Faraz Mazhar")
	fmt.Println(first_name_one, second_name_one)

	first_name_two, second_name_two := getInitials("Gordon Freeman")
	fmt.Println(first_name_two, second_name_two)

	first_name_three, second_name_three := getInitials("Mirana")
	fmt.Println(first_name_three, second_name_three)

}
