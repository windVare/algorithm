/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    var number = 0;
    for (var i = 0; i < S.length; i ++) {
        if (J.indexOf(S[i]) !== -1) {
            number ++;
        }
    }
    return number;
};

alert(numJewelsInStones("z", "ZZ"));