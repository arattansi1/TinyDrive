/* https://stackoverflow.com/a/50305285 */
/* https://stackoverflow.com/a/14779244 */
/* https://stackoverflow.com/a/25290107 */

CREATE USER 'project'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'project'@'%';
FLUSH PRIVILEGES;
CREATE DATABASE tinydrive;
