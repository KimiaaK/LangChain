SELECT email
FROM employee_email
GROUP BY email
    HAVING COUNT(email) > 1
/*Groups the rows by the email column, creating a separate group for each unique email address.
Allows aggregate functions (like COUNT) to operate on each group.*/
