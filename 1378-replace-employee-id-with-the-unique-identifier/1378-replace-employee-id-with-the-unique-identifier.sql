SELECT e.name, eu.unique_id
FROM EmployeeUNI eu
RIGHT JOIN Employees e  ON eu.id = e.id;