/**
 * @param {number} N
 * @return {number}
 */
var fib = function(N) {
    if (N === 1){
        return 1;
    } else if (N === 0) {
        return 0;
    }

    return fib(N - 1) + fib(N - 2);
};

alert(fib(2));
alert(fib(4));
alert(fib(3));
alert(fib(30));

