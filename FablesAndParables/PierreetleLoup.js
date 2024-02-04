function reponseDuVillage(foisLeLoupCrié) {
    let loupApparait = Math.random() < 0.5;
    if (foisLeLoupCrié > 2 && !loupApparait) {
        console.log("Les villageois ne croient plus le garçon.");
        return false; // Les villageois ne viennent pas.
    } else if (loupApparait) {
        console.log("Un loup apparaît réellement !");
        return foisLeLoupCrié <= 2;
        // Les villageois viennent seulement s'ils croient encore le garçon.
    } else {
        console.log("Le garçon a menti de nouveau.");
        return true; // Les villageois viennent encore.
    }
}

console.log(reponseDuVillage(3)); 
// Testez la fonction avec 3 fausses alertes.
