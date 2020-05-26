/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    var array = new Array();
    for (var i = left; i <= right; i ++) {
        // 判断是否存在0
        if (String(i).indexOf(0) !== -1) {
            continue;
        }

        var j = i, flag = false;
        while(j !== 0) {
            var mod = j % 10;
            j = parseInt(j / 10);
            if (i % mod !== 0) {
                flag = true;
                break
            }
        }
        if (flag === false) {
            array.push(i);
        }
    }
    return array;
};


alert(selfDividingNumbers(1, 22));
