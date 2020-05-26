/**
 * @param {string} astr
 * @return {boolean}
 */
var isUnique = function(astr) {
    let arr = [];
    for (let i = 0; i < astr.length; i ++) {
        if (arr[astr[i]] > 0){
            return false;
        }
        arr[astr[i]] = 1;
    }
    return true;
};


alert(isUnique("leetcode"));
alert(isUnique("abc"));
