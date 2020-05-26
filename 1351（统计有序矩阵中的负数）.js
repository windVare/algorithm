/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let number = 0;
    for (let i = 0; i < grid.length; i ++) {
        for (let j = 0;j < grid[i].length; j ++) {
            if (grid[i][j] < 0) {
                number += 1;
            }
        }
    }
    return number;
};

alert(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]));
alert(countNegatives([[3,2],[1,0]]));
alert(countNegatives([[1,-1],[-1,-1]]));
alert(countNegatives([[-1]]));
