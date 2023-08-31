package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func test(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "test success",
	})
}

func async(c *gin.Context) {
	copyContext := c.Copy()
	go func() {
		time.Sleep(5 * time.Second)

		log.Println("Done For " + copyContext.Request.URL.Path)
	}()
	c.JSON(http.StatusOK, gin.H{
		"messsage": "task send",
	})
}

func main() {
	defer fmt.Println("test defer")

	fmt.Println("add started")

	server := gin.Default()
	server.GET("/test", test)
	server.GET("/async", async)
	server.Run("0.0.0.0:7879")
}
