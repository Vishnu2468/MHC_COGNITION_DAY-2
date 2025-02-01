# MHC_COGNITION_DAY-2
This repository is a **Student Management System** that facilitates the retrieval of student data from a MySQL database using Django. It provides a foundational framework for managing and displaying student records efficiently.


![image](https://github.com/user-attachments/assets/560a3182-357c-4028-ba01-538222aa4037)



## Setting Up the Database in Django

To configure the **Student Management System** with MySQL, follow these steps:

### 1. **Create a MySQL Database**  
Before proceeding, ensure that MySQL is installed and running. You can create a database with any name, but in this project, we use **`students_db`**.

```sql
CREATE DATABASE students_db;
```

### 2. **Update Django `settings.py`**  
Modify the database settings in the `settings.py` file, located in the **sms** project directory. Replace the placeholder values (`USER`, `PASSWORD`) with your MySQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'students_db',  # Database name
        'USER': 'your_mysql_username',  # Replace with your MySQL username
        'PASSWORD': 'your_mysql_password',  # Replace with your MySQL password
        'HOST': 'localhost',  # Default host
        'PORT': '3306',  # Default MySQL port
    }
}
```

### 3. **Install MySQL Client for Django**  
Ensure you have the MySQL client installed:

```sh
pip install mysqlclient
```
or  
```sh
pip install pymysql
```
(If using `pymysql`, add `import pymysql; pymysql.install_as_MySQLdb()` in `__init__.py` of your Django project.)

### 4. **Apply Migrations**  
After updating `settings.py`, run the following commands to apply migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

Now, your Django project is successfully connected to the MySQL database.
