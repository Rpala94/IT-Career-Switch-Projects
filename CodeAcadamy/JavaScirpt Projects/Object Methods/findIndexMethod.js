// Write your code here:
function findMyKeys(arr) {
    let index = -1;
    for(let i= 0; i<arr.length; i++) {
      if (arr[i] === 'keys'){
        index = i
        break
      }
    }
    return index
  
   }
   // Alternate solution:
   //const findMyKeys = arr => arr.findIndex(item => item === 'keys')
  
  
  // Alternate solution:
  
  
  // Feel free to comment out the code below to test your function
  
  const randomStuff = ['credit card', 'screwdriver', 'receipt', 'gum', 'keys', 'used gum', 'plastic spoon'];
  
  console.log(findMyKeys(randomStuff))
  
  // Should print 4
  