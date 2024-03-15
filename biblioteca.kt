// Classe per representar un llibre
class Llibre(val titol: String, val autor: String, var exemplarsDisponibles: Int) {
    fun obtenirInformacio(): String {
        return "Títol: $titol, Autor: $autor, Exemplars disponibles: $exemplarsDisponibles"
    }
}
