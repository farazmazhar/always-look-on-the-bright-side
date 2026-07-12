package api

import (
	"time"

	"github.com/gin-gonic/gin"
)

type Order struct {
	OrderId      uint      `json:"OrderId" gorm:"primaryKey"`
	CustomerName string    `json:"CustomerName"`
	IsPaid       bool      `json:"IsPaid"`
	OrderDate    time.Time `json:"OrderDate"`
	OongsBoongs  string    `json:"-" gorm:"column:oongabonga"`

	// Has Many: An Order has many LineItems
	LineItems []LineItem `json:"LineItems" gorm:"foreignKey:VeryCoolOrderId"`
}

// Unnamed reciever function.
func (Order) TableName() string {
	return "Order"
}

type LineItem struct {
	LineItemId       uint    `json:"LineItemId" gorm:"primaryKey"`
	LineItemName     string  `json:"Name"`
	LineItemPrice    float64 `json:"Price"`
	LineItemQuantity uint    `json:"Quantity"`

	// Foreign Key field in the database
	VeryCoolOrderId uint `json:"OrderId"`
	// Belongs To: A LineItem belongs to an Order
	Order Order `json:"Order" gorm:"foreignKey:VeryCoolOrderId;references:OrderId"`
}

func (LineItem) TableName() string {
	return "LineItem"
}

type JsonResponse struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    any    `json:"data"`
}

func ResponseJSON(c *gin.Context, status int, message string, data any) {
	response := JsonResponse{
		Status:  status,
		Message: message,
		Data:    data,
	}

	c.JSON(status, response)
}
