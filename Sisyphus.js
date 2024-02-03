function sisyphusEffort() {
    console.log("Sisyphus starts to push the boulder...");
  
    setTimeout(() => {
      console.log("Sisyphus nearly reaches the top...");
      
      setTimeout(() => {
        console.log("The boulder rolls back down.");
        // Recursive call to simulate the eternal effort
        sisyphusEffort();
      }, 1000); // Represents the boulder rolling back down
  
    }, 1000); // Represents the effort to push the boulder up
  }
  
  sisyphusEffort();
  