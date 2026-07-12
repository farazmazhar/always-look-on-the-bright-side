package main

import (
	"bill_generator_api/api"

	"github.com/gin-gonic/gin"
)

func main() {
	api.InitDB()
	r := gin.Default()

	//routes
	r.POST("/order", api.CreateOrder)
	r.GET("/orders", api.GetOrders)
	r.GET("/order/:OrderId", api.GetOrder)
	r.PUT("/order/:OrderId", api.UpdateOrder)
	r.DELETE("/order/:OrderId", api.DeleteOrder)

	r.Run(":8080")
}
