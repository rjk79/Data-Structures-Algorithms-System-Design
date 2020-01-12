function flip(arr, k) {  
  for (let i = 0; i < Math.floor((k/2)+1); i++) {
    const j = k - i - 1;
    
    let tmp = arr[j];
    arr[j] = arr[i]
    arr[i] = tmp;
  }
  
  return arr;
}

console.log(flip([1, 5, 4, 3, 2], 2));

