const lifePhase = age => {
    if (age < 0 || age > 140) {
        return 'This is not a valid age'
    } else if (age < 4) {
        return 'baby'
    } else if (age < 13) {
        return 'child'
    } else if (age < 20) {
        return 'teen'
    } else if (age < 65) {
        return 'adult'
    } else {
        return 'senior citizen'
    }
}
/*
function lifePhase (age) {
    if (age < 0 || age > 140) {
       return 'This is not a valid age'
   } else if (age < 4) {
        return 'baby'
    } else if (age < 13) {
        return 'child'
    } else if (age < 20) {
       return 'teen'
    } else if (age < 65) {
       return 'adult'
    } else {
        return 'senior citizen'
    }  
}
*/
console.log(lifePhase(5)) //should print 'child'
console.log(lifePhase(29))
console.log(lifePhase(102))
console.log(lifePhase(59))
console.log(lifePhase(17))
console.log(lifePhase(149))