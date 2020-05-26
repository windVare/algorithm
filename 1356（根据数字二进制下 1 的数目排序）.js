/**
 * @param {number[]} arr
 * @return {number[]}
 */

var zeroNumber = function (data) {
    let number = 0;
    while (data) {
        number += data % 2;
        data = Math.floor(data / 2);
    }
    return number;
};

var sortByBits = function(arr) {
    let list = [];
    for (let i = 0; i < arr.length; i ++) {
        list[i] = [arr[i], zeroNumber(arr[i])];
    }
    list.sort(function (a, b) {
        if (a[1] === b[1]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    });
    var nums = [];
    for (let i = 0; i < list.length; i ++) {
        nums[i] = list[i][0];
    }
    return nums;
};


// alert(sortByBits([0,1,2,3,4,5,6,7,8]));
// alert(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]));
alert(sortByBits([2,3,5,7,11,13,17,19]));