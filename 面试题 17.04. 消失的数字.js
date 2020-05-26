/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    var sum = nums.reduce((pre, next) => {return pre + next});
    var len = nums.length;
    return (len + 1) * len / 2 - sum;
};


alert(missingNumber([9,6,4,2,3,5,7,0,1]));
