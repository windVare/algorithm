/**
 * @param {number[]} coins
 * @return {number}
 */

var func = function (num) {
    let res = Math.floor(num / 2);
    if (num % 2) {
        res ++;
    }
    return res;
};

var minCount = function (coins) {
    let number = 0;
    for (let i = 0; i < coins.length; i ++) {
        number += func(coins[i]);
    }
    return number;
};


document.writeln(minCount([4, 2, 1]));
document.writeln(minCount([2, 3, 10]));
