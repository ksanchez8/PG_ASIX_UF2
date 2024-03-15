// Classe per representar un llibre
class Llibre(val titol: String, val autor: String, var exemplarsDisponibles: Int) {
    fun obtenirInformacio(): String {
        return "Títol: $titol, Autor: $autor, Exemplars disponibles: $exemplarsDisponibles"
    }
}

// Classe per representar un soci
class Soci(val nom: String, val cognom: String, val numSoci: Int) {
    fun obtenirInformacio(): String {
        return "Nom: $nom, Cognom: $cognom, Número de soci: $numSoci"
    }
}

// Classe per representar un préstec
class Prestec(val llibre: Llibre, val soci: Soci, val dataPrestec: String) {
    fun obtenirInformacio(): String {
        return "Llibre: ${llibre.titol}, Soci: ${soci.nom} ${soci.cognom}, Data de préstec: $dataPrestec"
    }
}

// Función principal
fun main() {
    // Creación de libros
    val libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 3)
    val libro2 = Libro("Crimen y castigo", "Fyodor Dostoevsky", 5)

      // Creación de socios
    val socio1 = Socio("Juan", "García", 1001)
    val socio2 = Socio("María", "López", 1002)

     // Mostrar información de los libros y socios
    println("Información de los libros:")
    println(libro1.obtenerInformacion())
    println(libro2.obtenerInformacion())

    println("\nInformación de los socios:")
    println(socio1.obtenerInformacion())
    println(socio2.obtenerInformacion())

    