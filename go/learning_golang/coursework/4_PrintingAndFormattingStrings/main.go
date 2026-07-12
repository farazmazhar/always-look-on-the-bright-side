package main

import (
	"fmt"
	"strings"
	"text/template"
)

// Define a struct to hold your data
type MessageData struct {
	Username  string
	Action    string
	FileCount int
}

func main() {

	// Print - Doesn't ends with \n
	fmt.Print("Hello, ")
	fmt.Print("World! \n")
	fmt.Print("new line \n")

	// Println - Ends with \n
	fmt.Println("Hello World!")
	fmt.Println("Byeee 👋")

	// Printing variables
	age := 30
	name := "faraz"

	fmt.Println("My age is", age, "and my name is", name)

	// Printf (formatted strings) %_ = format specifier (_ is a placeholder here)
	fmt.Printf("My age is %v and my name is %v\n", age, name) // %v = variable
	fmt.Printf("My age is %v and my name is %q\n", age, name) // %q = puts quotes, strings only
	fmt.Printf("age is of type %T\n", age)                    // %T is to fetch variable type
	fmt.Printf("You scored %0.1f points\n", 255.55)           // %f = float, %0.2f where 2 is for scale.

	// Sprintf (save formatted strings)
	var str = fmt.Sprintf("My age is %v and my name is %q\n", age, name) // %q = puts quotes, strings only
	fmt.Println("The saved string is", str)

	// Building strings
	// name := "faraz" // Already initiated...
	ageS := "30"
	cool := "very"

	template_ := "My name is {name} and I am {age} years old and I am {cool} cool!"

	replacer := strings.NewReplacer(
		"{name}", name,
		"{age}", ageS,
		"{cool}", cool,
	)

	var string_builder strings.Builder
	replacer.WriteString(&string_builder, template_)
	finalMessage := string_builder.String()
	fmt.Println(finalMessage)

	// text/Template
	// 1. Define the template using {{.FieldName}} syntax
	tmplText := "Notification: User {{.Username}} has successfully {{.Action}} {{.FileCount}} files."

	// 2. Parse the template
	tmpl, _ := template.New("message").Parse(tmplText)

	// 3. Create your data object (handles numbers automatically!)
	data := MessageData{
		Username:  "faraz",
		Action:    "downloaded",
		FileCount: 5,
	}

	// 4. Initialize the builder
	var builder strings.Builder

	// 5. Execute the template directly into the builder without fmt
	tmpl.Execute(&builder, data)

	finalMessageX := builder.String()
	fmt.Println(finalMessageX)

}
