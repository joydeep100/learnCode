.. To obtain the 2nd highest salary from a table, you can use the following SQL query:
SELECT MAX(salary) AS SecondHighestSalary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
.. This is one way but the more efficient way is to use like below

.. To obtain 2nd and thrid highest marks
SELECT name, marks
FROM student_marks
ORDER BY marks DESC
LIMIT 1, 2;  
.. LIMIT [skip n items], [display n items]