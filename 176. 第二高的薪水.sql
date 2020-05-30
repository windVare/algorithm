-- 题目链接： https://leetcode-cn.com/problems/second-highest-salary/
-- 解题思路： 若不存在第二大的数，返回null，若只存在多个第一大的薪水，返回null。
select (
    select
        distinct Salary
    FROM Employee
    order by Salary DESC
    limit 1, 1
) AS SecondHighestSalary;