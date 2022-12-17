
function getMaxCals (calorieList) {
  let sumNum = 0; // a variable to keep track of the sum of each group
  let sumList = []; // an array to keep track of top 3 sums

  for (let i = 0; i < calorieList.length; i++){
    if (calorieList[i]){ // check if item is truthy, ie contains a string
      sumNum = sumNum + (+calorieList[i]); // then add to running sum
    } else if (!calorieList[i]){ // if item is a falsy, ie no string
        if (sumList.length < 3){ // check if length of array is less then 3
          sumList.push(sumNum); // add to array
        } else if (sumNum > Math.min(...sumList)){ // else, array has 3 elements
            let minNum = Math.min(...sumList); // find min of array
            sumList = sumList.filter(number => number !== minNum); // replace array with new array that does not include min element
            sumList.push(sumNum); // add running sum to array instead of min element
        }
      
        sumNum = 0; // reset running sum
    }
  }

  if (sumNum > Math.min(...sumList)){ // in the case that the original array does not end with empty string do another check
    let minNum = Math.min(...sumList);
    sumList = sumList.filter(number => number !== minNum);
    sumList.push(sumNum);
  }

  return sumList.reduce((a, b) => { // return the sum of the top 3 sum array
    return a + b;
  })
}

let lines;
const fs = require('fs');

fs.readFile('day_01_input.txt', 'utf8', (err, data) => {
if (err) {
    console.log('error');
} else {
    // Use the data variable to access the file contents
    lines = data.split('\n');
    maxCals = getMaxCals(lines);
    console.log(maxCals);
    }
})

// test
// const arr2 = ['1', '4', '', '4', '5', '', '2', '4', '', '8', '9'];
// maxCalsTest = getMaxCals(arr2);
// console.log(maxCalsTest);