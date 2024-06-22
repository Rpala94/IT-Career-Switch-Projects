const finalGrade = (midterm, final, homework) => {
    if ((midterm < 0 || midterm > 100) || (final < 0 || final > 100) || (homework < 0 || homework > 100)) {
      return 'You have entered an invalid grade.'
    } 
    let average = (midterm + final + homework) / 3
    if (average < 60) {
      return 'F'
    }
    else if (average < 70) {
      return 'D'
    }
    else if (average < 80) {
      return 'C'
    }
    else if (average < 90) {
      return 'B'
    } else {
      return 'A'
    }
  }
  
    /* function finalGrade(midterm, final, homework) {
    if ((midterm < 0 || midterm > 100) || (final < 0 || final > 100) || (homework < 0 || homework > 100)) {
        return 'You have entered an invalid grade.'
    }
    let average = (midterm + final + homework) / 3
    if (average < 60) {
        return 'F'
    }
    else if (average < 70) {
        return 'D'
    }
    else if (average < 80) {
        return 'C'
    }
    else if (average < 90) {
        return 'B'
    } else {
        return 'A'
    }
}
*/
  
  
   console.log(finalGrade(99, 92, 95)) // Should print 'A'
   console.log(finalGrade(100, 70, 89))
   console.log(finalGrade(75, 65, 81))
   console.log(finalGrade(52, 7, 81))
   console.log(finalGrade(102, 65, 81))
   console.log(finalGrade(70, 65, 70))
  
   
 