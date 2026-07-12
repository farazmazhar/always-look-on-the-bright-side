# Learning Golang



## Initialize Go Module

`go mod init MODULE_NAME`

This created `go.mod` file.

## Dependencies related cheatsheet

```
Task 	                              Command
Remove Go module dependency 	      go get module@none
Clean unused dependencies 	        go mod tidy
Check why a dependency exists 	    go mod why module
View module dependency graph 	      go mod graph
Remove globally installed Go tool 	rm $(go env GOPATH)/bin/tool-name
Clear Go module cache 	            go clean -modcache
```

This adds the requirements in the `go.mod` file and created `go.sum` file which seems to contain checksums.
