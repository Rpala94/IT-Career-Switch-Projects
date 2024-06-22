// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G'];
    return dnaBases[Math.floor(Math.random() * 4)];
  }
  
  // Returns a random single strand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = [];
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase());
    }
    return newStrand;
  }
  
  // Factory function to create pAequor objects
  const pAequorFactory = (specimenNum, dna) => {
    return {
      specimenNum,
      dna,
      // Method to simulate mutation
      mutate() {
        const randomIndex = Math.floor(Math.random() * this.dna.length);
        let newBase = returnRandBase();
        while (newBase === this.dna[randomIndex]) {
          newBase = returnRandBase();
        }
        this.dna[randomIndex] = newBase;
        return this.dna;
      },
      // Method to compare DNA with another pAequor object
      compareDNA(otherPaequor) {
        let commonBases = 0;
        for (let i = 0; i < this.dna.length; i++) {
          if (this.dna[i] === otherPaequor.dna[i]) {
            commonBases++;
          }
        }
        const percentage = (commonBases / this.dna.length) * 100;
        console.log(`Specimen #${this.specimenNum} and Specimen #${otherPaequor.specimenNum} have ${percentage.toFixed(2)}% DNA in common.`);
      },
      // Method to check if the object is likely to survive
      willLikelySurvive() {
        const countCG = this.dna.filter(base => base === 'C' || base === 'G').length;
        return (countCG / this.dna.length) >= 0.6;
      }
    };
  }
  
  // Create 30 instances of pAequor that can survive
  const survivingInstances = [];
  let specimenCount = 1;
  
  while (survivingInstances.length < 30) {
    const newStrand = mockUpStrand();
    const newPaequor = pAequorFactory(specimenCount, newStrand);
    if (newPaequor.willLikelySurvive()) {
      survivingInstances.push(newPaequor);
      specimenCount++;
    }
  }
  
  // Example usage and testing
  const pAequor1 = pAequorFactory(1, mockUpStrand());
  const pAequor2 = pAequorFactory(2, mockUpStrand());
  
  pAequor1.compareDNA(pAequor2);
  pAequor1.mutate();
  console.log(pAequor1.dna);
  console.log(pAequor1.willLikelySurvive());
  
  
  
  
  
  
  
  