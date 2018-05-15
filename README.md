## Simple API to allow users to view posts and users. Users can edit only their posts and their personal info in the system

# Helper
`virtualenv -p python3 env`

`sudo -u postgres psql`

postgres=# `CREATE DATABASE tangiers;`

postgres=# `CREATE USER tangiers WITH password 'tangiers';`

postgres=# `GRANT ALL ON DATABASE tangiers TO tangiers;`

postgres=# `ALTER USER tangiers CREATEDB;`
