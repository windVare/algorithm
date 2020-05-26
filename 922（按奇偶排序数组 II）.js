/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParityII = function(A) {
    var evenNumber = [], unevenNumber = [];
    for(var i = 0; i < A.length; i ++) {
        if(A[i] % 2 === 0) {
            evenNumber.push(A[i]);
        } else {
            unevenNumber.push(A[i]);
        }
    }
    // 排序
    evenNumber.sort((a, b) => a - b);
    unevenNumber.sort((a, b) => a - b);
    var nums = [], k = 0, t = 0;
    for(var i = 0; i < A.length; i ++) {
        if (i % 2 === 0) {
            nums.push(evenNumber[k]);
            k ++;
        } else {
            nums.push(unevenNumber[t]);
            t ++;
        }
    }
    return nums;
};

alert(sortArrayByParityII([4,2,5,7]));
