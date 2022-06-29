package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"
)

var reader *bufio.Reader

type User struct {
	id       int
	username string
	email    string
	age      int
}

var id int
var users map[int]User

func crearUsuario() {
	clearConsole()
	fmt.Print("Ingresa un username:")
	username := readline()
	fmt.Print("Ingresa un email:")
	email := readline()
	fmt.Print("Ingresa una edad:")
	age, err := strconv.Atoi(readline())
	if err != nil {
		panic("No es posible convertir un string a un int")
	}

	id++
	user := User{id, username, email, age}
	users[id] = user

	fmt.Println("\nUsuario Creado")
}
func listarUsuario() {
	clearConsole()

	fmt.Println("id - Username")
	for id, user := range users {
		fmt.Println(id, "-", user.username)
	}

	fmt.Println("\nLista de Usuarios")
}
func actualizarUsuario() {
	clearConsole()
	fmt.Println("Ingresa el ID de usuario para actualizar:")
	id, err := strconv.Atoi(readline())
	if err != nil {
		panic("Imposible la conversión de la edad, número incorrecto")
	}
	if _, ok := users[id]; ok {
		clearConsole()
		fmt.Println("Ingresa un valor para el nombre usuario:")
		username := readline()
		fmt.Println("Ingresa un valor para el correo:")
		email := readline()
		fmt.Println("Ingresa un valor para la edad:")
		age, err := strconv.Atoi(readline())
		if err != nil {
			panic("Imposible la conversión de la edad, número incorrecto")
		}
		user := User{id, username, email, age}
		users[id] = user
		fmt.Println("Usuario actualizado exitosamente")
	}
}
func eliminarUsuario() {
	clearConsole()

	fmt.Println("Ingresa el id del usuario para eliminar")
	id, err := strconv.Atoi(readline())

	if err != nil {
		panic("No es posible convertir un string a un int")
	}

	if _, ok := users[id]; ok {
		delete(users, id)
	}

	fmt.Println("\nUsuario Eliminado")
}

func clearConsole() {
	cmd := exec.Command("clear")
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func readline() string {
	//Método para obtener lo que se teclee
	if option, err := reader.ReadString('\n'); err != nil {
		panic("No es posible obtener el valor")
	} else {
		//Eliminar el caracter de \n
		return strings.TrimSuffix(option, "\n")
	}
}

func main() {
	var option string
	users = make(map[int]User)
	//stdin = Estandar init
	reader = bufio.NewReader(os.Stdin)
	clearConsole()

	for {

		fmt.Println("A) Crear")
		fmt.Println("B) Listar")
		fmt.Println("C) Actualizar")
		fmt.Println("D) Eliminar")

		fmt.Println("Ingresa una opción")

		option = readline()

		if option == "quit" || option == "q" {
			break
		}

		switch option {
		case "a", "crear":
			crearUsuario()
		case "b", "listar":
			listarUsuario()
		case "c", "actualizar":
			actualizarUsuario()
		case "d", "eliminar":
			eliminarUsuario()
		default:
			fmt.Println("\nNo existe esa opción:")
		}

	}
	fmt.Println("\nAdios!!\n")
}
