function villageResponse(timesWolfCried) {
    let wolfAppears = Math.random() < 0.5;
    if (timesWolfCried > 2 && !wolfAppears) {
        console.log("The villagers no longer believe the boy.");
        return false; // The villagers don't come.
    } else if (wolfAppears) {
        console.log("A wolf actually appears!");
        return timesWolfCried <= 2;
        // The villagers only come if they still believe the boy.
    } else {
        console.log("The boy lied again.");
        return true; // The villagers still come.
    }
}

console.log(villageResponse(3)); 
// Test the function with 3 false alarms.
