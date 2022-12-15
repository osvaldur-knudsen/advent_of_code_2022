
function getMaxCals (calorieList) {
  let sum = 0;
  let maxSum = 0;

  for (let i = 0; i < calorieList.length; i++){
    if (calorieList[i]){
      sum = sum + (+calorieList[i]);
    } else if (!calorieList[i]){
      if (sum > maxSum){
        maxSum = sum;
      }
      sum = 0;
    }
  }

  if (sum > maxSum){
    maxSum = sum;
  }

  return maxSum;
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
// const arr2 = ['1', '4', '', '4', '5', '', '3', '4', '1'];
// maxCalsTest = getMaxCals(arr2);
// console.log(maxCalsTest);