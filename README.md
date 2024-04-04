### Requirements
```
pipenv install uvicorn sqlalchemy fastapi pymysql

```
### Database
```
MariaDb

sudo pacman -S mariadb sqlite
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
sudo systemctl enable --now mariadb
sudo mysql_secure_installation
...
...

sudo mysql -uroot -p
MariaDB [(none)]> CREATE USER 'homestead'@'localhost' IDENTIFIED BY 'secret';

MariaDB [(none)]> GRANT ALL PRIVILEGES ON * . * TO 'homestead'@'localhost';

MariaDB [(none)]> FLUSH PRIVILEGES;

MariaDB [(none)]> exit

...

 mysqladmin -u homestead -p create BlogApplication

```

### How to install
```
pipenv install -r requirements.txt
```
### Sql
```
uvicorn main:app --reload --port 5000 --host 0.0.0.0

```
