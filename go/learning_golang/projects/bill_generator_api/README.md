# Bill Generator API - Demo Project

Reference: https://roadmap.sh/golang/rest-api

## Initialize Go Module

`go mod init bill_generator`

This created `go.mod` file.

## REST API dependencies

```sh
go get -u github.com/gin-gonic/gin # framework for building web applications
go get -u gorm.io/gorm # Go-based Object Relational Mapper (ORM)
go get -u gorm.io/driver/postgres # db drivers
go get -u gorm.io/driver/sqlite # db drivers
go get -u github.com/joho/godotenv
```

Use duckdb for a later projects -> https://duckdb.org/docs/current/clients/go
`go get github.com/duckdb/duckdb-go/v2``

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

## gorm

Adding `gorm.Model` adds the following fields. If you want custom primary key, don't add it.

```go
type Model struct {
	ID        uint           `gorm:"primaryKey"`
	CreatedAt time.Time
	UpdatedAt time.Time
	DeletedAt gorm.DeletedAt `gorm:"index"`
}```
