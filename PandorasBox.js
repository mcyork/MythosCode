function openPandorasBox() {
    return new Promise((resolve, reject) => {
      resolve("Evils of the world are released, but Hope remains.");
    });
  }
  
  openPandorasBox().then(message => console.log(message));
  