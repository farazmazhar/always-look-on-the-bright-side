package api

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func InitDB() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Failed to connect to database:", err)
	}

	dsn := os.Getenv("DB_URL")
	DB, err = gorm.Open(sqlite.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("Failed to connect to database:", err)
	}

	// migrate the schema... {} at the end to initialise before passing to automigrate.
	if err := DB.AutoMigrate(&Order{}); err != nil {
		log.Fatal("Failed to migrate schema:", err)
	}

	if err := DB.AutoMigrate(&LineItem{}); err != nil {
		log.Fatal("Failed to migrate schema:", err)
	}
}

func CreateOrder(c *gin.Context) {
	var order Order

	//bind the request body
	if err := c.ShouldBindJSON(&order); err != nil {
		ResponseJSON(c, http.StatusBadRequest, "Invalid input", nil)
		return
	}

	// Always catch and handle database execution errors
	if err := DB.Create(&order).Error; err != nil {
		ResponseJSON(c, http.StatusInternalServerError, "Failed to create order", nil)
		return
	}

	ResponseJSON(c, http.StatusCreated, "Order created successfully", order)
}

func CreateLineItem(c *gin.Context) {
	var line_item LineItem

	if err := c.ShouldBindJSON(&line_item); err != nil {
		ResponseJSON(c, http.StatusBadRequest, "Invalid input", nil)
		return
	}

	if err := DB.Create(&line_item).Error; err != nil {
		ResponseJSON(c, http.StatusInternalServerError, "Failed to create order", nil)
		return
	}

	ResponseJSON(c, http.StatusCreated, "Line Item created successfully", line_item)
}

func GetOrders(c *gin.Context) {
	var orders []Order

	if err := DB.Preload("LineItems").Find(&orders).Error; err != nil {
		ResponseJSON(c, http.StatusInternalServerError, "Failed to get orders", nil)
		return
	}

	ResponseJSON(c, http.StatusOK, "Orders retrieved successfully", orders)
}

func GetOrder(c *gin.Context) {
	var order Order

	// TODO: How to do complex conditions?

	if err := DB.Preload("LineItems").First(&order, c.Param("OrderId")).Error; err != nil {
		ResponseJSON(c, http.StatusNotFound, "Order not found", nil)
		return
	}

	ResponseJSON(c, http.StatusOK, "Order retrieved successfully", order)
}

func UpdateOrder(c *gin.Context) {
	var order Order

	if err := DB.First(&order, c.Param("OrderId")).Error; err != nil {
		ResponseJSON(c, http.StatusNotFound, "Order not found", nil)
		fmt.Println(err)
		return
	}

	if err := c.ShouldBindJSON(&order); err != nil {
		ResponseJSON(c, http.StatusBadRequest, "Invalid input", nil)
		fmt.Println(err)
		return
	}

	err := DB.Model(&order).Updates(&order).Error
	if err != nil {
		ResponseJSON(c, http.StatusInternalServerError, "Failed to update the order", nil)
		fmt.Println(err)
		return
	}

	ResponseJSON(c, http.StatusOK, "Order updated successfully", order)
}

func DeleteOrder(c *gin.Context) {
	var order Order

	if err := DB.Delete(&order, c.Param("OrderId")).Error; err != nil {
		ResponseJSON(c, http.StatusNotFound, "Order not found", nil)
		return
	}

	ResponseJSON(c, http.StatusOK, "Order deleted successfully", nil)
}
