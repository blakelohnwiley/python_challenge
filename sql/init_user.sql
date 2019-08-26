/*
This script when executed by MySQL will create a new user called swimlane on localhost and identified by the password swimlane. This user will be used by the application to connect from the python scripts to the database.
*/
flush privileges;
--use mysql;
create user "swimlane"@"localhost" identified by "swimlane";
create database if not exists swimlane;
use swimlane;
grant all on swimlane.* to "swimlane"@"localhost";
