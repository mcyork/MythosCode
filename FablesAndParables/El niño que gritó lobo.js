function respuestaDelPueblo(vecesQueGritoLobo) {
    let loboAparece = Math.random() < 0.5;
    if (vecesQueGritoLobo > 2 && !loboAparece) {
        console.log("Los aldeanos ya no creen al niño.");
        return false; // Los aldeanos no vienen.
    } else if (loboAparece) {
        console.log("¡Un lobo aparece de verdad!");
        return vecesQueGritoLobo <= 2;
        // Los aldeanos solo vienen si todavía creen al niño.
    } else {
        console.log("El niño mintió otra vez.");
        return true; // Los aldeanos siguen viniendo.
    }
}

console.log(respuestaDelPueblo(3)); 
// Prueba la función con 3 falsas alarmas.
