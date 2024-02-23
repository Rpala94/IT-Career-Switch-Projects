// Write your function here:

const reportingForDuty = (rank, lastName) => `${rank} ${lastName} reporting for duty!`



 console.log(reportingForDuty('Private', 'Fido')) // Should return 'Private Fido reporting for duty!'
 
 /*
// Using string concatenation:
const reportingForDuty = (rank, lastName) => rank + " " + lastName + " " + "reporting for duty!"

// As a function declaration:
function reportingForDuty(rank, lastName) {
    return `${rank} ${lastName} reporting for duty!`
}
*/

console.log(reportingForDuty('Captain', 'Lee'))
console.log(reportingForDuty('Colonel', 'James'))
console.log(reportingForDuty('Major', 'Woo'))
console.log(reportingForDuty('Lieutenant', 'Pablo'))