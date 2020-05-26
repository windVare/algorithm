/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var maximum = function(a, b) {
    let x = (a + b) / 2;
    return x + Math.abs(x - a);
};


alert(maximum(1, 2));
alert(maximum(2, 9));
