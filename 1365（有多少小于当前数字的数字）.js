/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    let list = [];
    for (let i = 0; i < 105; i++) {
        list[i] = 0;
    }
    for (let i = 0; i < nums.length; i++) {
        list[nums[i]]++;
    }
    let number = 0;
    let data = [];
    for (let i = 0; i < list.length; i++) {
        if (list[i]) {
            data[i] = number;
            number += list[i];
        }
    }
    let result = [];
    for (let i = 0; i < nums.length; i ++) {
        result[i] = data[nums[i]];
    }
    return result;
};

// alert(smallerNumbersThanCurrent([8, 1, 2, 2, 3]));
// alert(smallerNumbersThanCurrent([6,5,4,8]));
alert(smallerNumbersThanCurrent([7,7,7,7]));