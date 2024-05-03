function good_pair(nums){
    let count = 0;
    for (let i=0; i<nums.length; i++){
        for (let j=i+1; j<nums.length; j++){
            if(nums[i] == nums[j]){
                count++;
            }
        }
    }
    return count;
}
console.log(good_pair([1, 2, 1, 1, 3, 4, 3, 5, 4]))