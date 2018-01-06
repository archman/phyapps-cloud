1. Create database: *phyapps_cloud*

```
CREATE DATABASE phyapps_cloud`;
```

2. Create development user: *dev*

```
CREATE USER 'dev'@'localhost' IDENTIFIED BY 'dev';
GRANT ALL PRIVILEGES ON phyapps_cloud.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;
```

3. Edit `config.py`:

```
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://{username}:{password}@{host}/phyapps_cloud'.format(
            username='dev',
            password='dev',
            host='localhost')
```

4. Initialize database:
   
```
make init_db
```

5. [Optional] Import data from SQLite:
    
