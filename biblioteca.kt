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