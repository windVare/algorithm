/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var mid, left = 0, right = nums.length - 1;
    while (left <= right) {
        mid = parseInt((left + right) / 2);
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
};


alert(search([-1,0,3,5,9,12], 9));
alert(search([-1,0,3,5,9,12], 2));
