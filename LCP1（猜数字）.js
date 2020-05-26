/**
 * @param {number[]} guess
 * @param {number[]} answer
 * @return {number}
 */
var game = function(guess, answer) {
    var len = guess.length, number = 0;
    for (var i = 0; i < len; i ++)  {
        if (guess[i] === answer[i]) {
            number += 1;
        }
    }
    return number;
};
