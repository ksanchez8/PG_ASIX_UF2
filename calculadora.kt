// 1. Funció per Sumar
fun sumar(a: Int, b: Int): Int {
    return a + b
}

// 2. Funció per Restar
fun restar(a: Int, b: Int): Int {
    return a - b
}

// 3. Funció per Multiplicar
fun multiplicar(a: Int, b: Int): Int {
    return a * b
}

// 4. Funció per Dividir
fun dividir(a: Int, b: Int): Double {
    if (b != 0) {
        return a.toDouble() / b.toDouble()
    } else {
        println("Error: Divisió per zero")
        return Double.NaN
    }
}

// 5. Funció Principal
fun main() {
    // Exemples d'ús
    val num1 = 10
    val num2 = 5

    val suma = sumar(num1, num2)
    println("Suma: $suma")

    val resta = restar(num1, num2)
    println("Resta: $resta")

    val producte = multiplicar(num1, num2)
    println("Producte: $producte")

    val quocient = dividir(num1, num2)
    println("Quocient: $quocient")
}
