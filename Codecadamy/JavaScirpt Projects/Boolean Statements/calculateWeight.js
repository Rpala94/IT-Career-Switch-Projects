const calculateWeight = (earthWeight, planet) => {
    switch(planet) {
      case 'Mercury':
      return earthWeight * 0.378;
      case 'Venus':
      return earthWeight * 0.907;
      case 'Mars' :
      return earthWeight * 0.377;
      case 'Jupiter' :
      return earthWeight * 2.36;
      case 'Saturn' :
      return earthWeight * 0.916;
    default:
      return 'Invalid Planet Entry. Try: Mercury, Venus, Mars, Jupiter, or Saturn.'
  
    }
  }
  
  /* As a function declaration: 
  function calculateWeight(earthWeight, planet) {
      switch (planet) {
          case 'Mercury':
              return earthWeight * .378;
          case 'Venus':
              return earthWeight * .907;
          case 'Mars':
              return earthWeight * .377;
          case 'Jupiter':
              return earthWeight * 2.36;
          case 'Saturn':
              return earthWeight * .916;
       default:
          return 'Invalid Planet Entry. Try: Mercury, Venus, Mars, Jupiter, or Saturn.'
      }
  } */
  
  
  console.log(calculateWeight(100, 'Jupiter')) 
  console.log(calculateWeight(10, 'Mars')) 
  console.log(calculateWeight(89, 'Venus')) 
  console.log(calculateWeight(170, 'Mercury')) 
  console.log(calculateWeight(1000, 'Saturn')) 
  console.log(calculateWeight(100, 'Earth')) 