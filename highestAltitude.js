function largestAltitude(gain) {
    let max = 0;
    let curr = 0;
    for (let i in gain) {
        curr += gain[i]; 
        if (curr > max) {
            max = curr;
        }
    }
    return max;
}
console.log(largestAltitude([-5, 1, 5, 0, -7]))