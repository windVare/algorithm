/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    var i = 0, j = parseInt(Math.sqrt(c));

    while (i <= j) {
        var sum = i * i + j * j;
        if (sum === c) {
            return true;
        } else if (sum < c) {
            i ++;
        } else {
            j --;
        }
    }
    return false;
};


alert(judgeSquareSum(3));