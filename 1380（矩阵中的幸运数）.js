/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function (matrix) {
    var h = matrix.length, res = [];
    for (var i = 0; i < h; i++) {
        for (var j = 0; j < matrix[i].length; j++) {
            // 判断是否为同行最小
            var number = matrix[i][j];
            if (number !== Math.min.apply(null, matrix[i])) {
                continue
            }
            // 判断是否为同列最大
            var flag = true;
            for (var k = 0; k < h; k++) {
                if (number < matrix[k][j]) {
                    flag = false;
                    break
                }
            }

            // 同时满足上述两种条件时，数据记录
            if (flag === true) {
                res.push(number);
            }
        }
    }
    return res;
};

alert(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]));
alert(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]));
alert(luckyNumbers([[7, 8], [1, 2]]));
