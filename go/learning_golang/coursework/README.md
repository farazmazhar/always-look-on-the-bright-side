# Learning Golang

- Tutorial: https://www.youtube.com/watch?v=etSN4X_fCnM&list=PL4cUxeGkcC9gC88BEo9czgyS72A3doDeM&index=1
- Repo: https://github.com/iamshaunjp/golang-tutorials
- To try after the course: https://gophercises.com/

## Tutorial 1 - Introduction and Steup

Code: [1_IntroductionAndSetup/test.go](./1_IntroductionAndSetup/test.go)

## Tutorial 2 - Your First Go File

Code: [2_YourFirstGoFile/main.go](./2_YourFirstGoFile/main.go)

Exporting a method (public?), the function starts with a capital letter.

The Rule of Capitalization

Go's access control is remarkably simple and is enforced entirely by the compiler:
- Uppercase letter (e.g., ExecuteTask): The function is exported (public). It can be called by any other package that imports the package it belongs to.
- Lowercase letter (e.g., calculateInternal): The function is unexported (private). It can only be seen and called from within the exact same package.

To run a file: `go run <filename>.go`

## Tutorial 3 - Variables Strings & Numbers

Code: [3_VariablesStringsAndNumbers/main.go](./3_VariablesStringsAndNumbers/main.go)

Variables are double quoted.

Relevent Link(s): https://go.dev/ref/spec#Numeric_types

## Tutorial 4 - Printing & Formatting Strings

Code: [4_PrintingAndFormattingStrings/main.go](./4_PrintingAndFormattingStrings/main.go)

fmt - Used to format stirngs and print them on stdout.

Relevent Link(s): https://pkg.go.dev/fmt

## Tutorial 5 - Arrays & Slices

Code: [5_ArraysAndSlices/main.go](./5_ArraysAndSlices/main.go)

Arrays are fixed length. -> [3]int{20, 25, 30}
Slices use arrays under the hood. Dynamic length, I beleive. -> []int{20, 25, 30}
  Basically, a list in Python is a slice in Go.

Slice ranges similar to [::] thing in Python.

## Tutorial 6 - The Standard Library

Code: [6_TheStandardLibrary/main.go](./6_TheStandardLibrary/main.go)

Link: https://pkg.go.dev/std

Don't need to manually import the packages, referring them generally would get them imported by the IDE extension.

Some methods may return new copy while some may update the existing variable.

## Tutorial 7 - Loops

Code: [7_Loops/main.go](./7_Loops/main.go)

Go always uses `for`, even for `while` loops.

## Tutorial 8 - Booleans & Conditionals

Code: [8_BooleansAndConditionals/main.go](./8_BooleansAndConditionals/main.go)

Conditional Operators:
- and => &&
- or  => ||

Use brackets to set precedence like `if (age > 18 && hasTicket) || isAdmin { ... }`.

## Tutorial 9 - Using Functions

Code: [9_UsingFunctions/main.go](./9_UsingFunctions/main.go)

Functions can be passed as parameters to other functions but also have the type of the expected parameters of that function.

## Tutorial 10 - Multiple Return Values

Code: [10_MultipleReturnValues/main.go](./10_MultipleReturnValues/main.go)

In this case, put the return types in `(...)` brackets.

## Tutorial 11 - Package Scope

Code: 
- [11_PackageScope/main.go](./11_PackageScope/main.go)
- [11_PackageScope/greetings.go](./11_PackageScope/greetings.go)

For variables, symbols, and functions defined in a package, you do not need to manually import them.
They are available in all the files inside a package.

Although symbols are available, but other files also need to be part of command to run code.

```sh
go run 11_PackageScope/main.go 11_PackageScope/greetings.go
```

The symbols defined in a scope other than package, even in a function that belong to that package,
if won't be accessible by the other files.

## Tutorial 12 - Maps


Code: [12_Maps/main.go](./12_Maps/main.go)

Sort of like dicts in Python.
Made up of Key-Value pairs.
Keys must have same datatype while same goes for values that they should also be of the same type.

`range` keyword is used to traverse through the iterables so even maps can be iterated using it.

## Tutorial 13 - Pass By Value

Code: [13_PassByValue/main.go](./13_PassByValue/main.go)

Go makes "copies" of values when passed into a function.

- Variable Types
  - Non-Pointer Values - Passed By Value
    - Strings
    - Ints
    - FLoats
    - Booleans
    - Arrays
    - Structs
    - ...
  - Pointer Wrapper Values - Passed By Reference
    - Slices
    - Maps
    - Functions
    - ...

## Tutorial 14 - Pointers

Code: [14_Pointers/main.go](./14_Pointers/main.go)

`&variable` where `&` gives the memory address.
`*pointer` will give the value and can also be updated.

## Tutorial 15 - Structs

Code: 
- [15_Structs/main.go](./15_Structs/main.go)
- [15_Structs/bill.go](./15_Structs/bill.go)

...other files also need to be part of command to run code.

No classes in go. Use structs instead to build blueprints.

`type structname struct {...`

Struct pointer (*bill)	Implicit dereference	Go automatically handles the (*b) part for clean syntax.

## Tutorial 16 - Reciever Functions

Code: 
- [16_RecieverFunctions/main.go](./16_RecieverFunctions/main.go)
- [16_RecieverFunctions/bill.go](./16_RecieverFunctions/bill.go)

Receiver function makes a copy of the object, and are not passed by reference.

Seems like (b bill) in the following statement is like class methods.

`func (bill) format() string {`

## Tutorial 17 - Receiver Functions with Pointers

Code: 
- [17_RecieverFunctionsWithPointers/main.go](./17_RecieverFunctionsWithPointers/main.go)
- [17_RecieverFunctionsWithPointers/bill.go](./17_RecieverFunctionsWithPointers/bill.go)

If the object is complex, passing the pointer is easier on the system.
Should it always be pointer?

## Tutorial 18 - User Input

Code: 
- [18_UserInput/main.go](./18_UserInput/main.go)
- [18_UserInput/bill.go](./18_UserInput/bill.go)

The `bufio.Reader` needs to know the input source.

## Tutorial 19 - Switch Statements

Code: 
- [19_UserInput/main.go](./19_UserInput/main.go)
- [19_UserInput/bill.go](./19_UserInput/bill.go)

```go
swtich varname {
	case "abc":
		...
	default:
		...
}```` 


## Tutorial 20 - Parsing Floats

Code: 
- [20_ParsingFloats/main.go](./20_ParsingFloats/main.go)
- [20_ParsingFloats/bill.go](./20_ParsingFloats/bill.go)

gofix - Use `string_variable.WriteString` instead of `+=`.

## Tutorial 21 - Saving Files

Code: 
- [21_SavingFiles/main.go](./21_SavingFiles/main.go)
- [21_SavingFiles/bill.go](./21_SavingFiles/bill.go)

`panic(err)` == `raise err`

## Tutorial 22 - Interfaces

Code:
- [22_Interfaces/main.go](./22_Interfaces/main.go)

Interfaces are not part of the struct... 
Just away to group functions together, for a lack of better term.
Reason: so you dont have write duplicate function for the structs
with the same Reciever Functions but with different implementation.

Declaring interface be like...

```go
type interface_name interface {
	method1() float64
	method2() int
	...
}
````
