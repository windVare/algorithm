/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {

    function compare(a, b) {
        if (a < b) {
            return -1;
        } else if (a >= b) {
            return 1;
        }
    }

    nums = nums.sort(compare);
    var arrayLength = nums.length;

    var sum1 = nums[arrayLength - 1] * nums[arrayLength - 2] * nums[arrayLength - 3];
    var sum2 = nums[arrayLength - 1] * nums[0] * nums[1];
    return Math.max(sum1, sum2);
};

alert(maximumProduct([1000,1000,2,1,2,5,3,1]));