/* https://stackoverflow.com/q/3278379 */

CREATE USER project WITH PASSWORD 'password';
ALTER ROLE project SET client_encoding TO 'utf8';
ALTER ROLE project SET default_transaction_isolation TO 'read committed';
ALTER ROLE project SET timezone TO 'UTC';

CREATE DATABASE tinydrive;
GRANT ALL PRIVILEGES ON DATABASE tinydrive TO project;
