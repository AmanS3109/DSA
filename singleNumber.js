let singleNum = (nums) => {
    let res = 0;
    for (let n of nums){
        res ^= n;
    }
    return res;
}
console.log(singleNum([4, 1, 2, 1, 2]))
console.log(singleNum([1, 2, 2, 3, 3]))