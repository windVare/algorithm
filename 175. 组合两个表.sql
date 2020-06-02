# 题目链接： https://leetcode-cn.com/problems/combine-two-tables/

# Write your MySQL query statement below
select a.FirstName, a.LastName, b.City, b.State
FROM Person as a LEFT JOIN Address as b
ON a.PersonId=b.PersonId
