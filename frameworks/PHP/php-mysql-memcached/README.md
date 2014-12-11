#PHP MySQL-memcached Benchmarking Test

This is the PHP portion of a [benchmarking test suite](../) comparing a variety of web development platforms.

This benchmark is the same as the raw PHP benchmark, except that it makes use of the [MySQL memcached interface](http://dev.mysql.com/doc/refman/5.6/en/innodb-memcached.html) introduced in MySQL 5.6 instead of the standard SQL interface. Only the database tests are implemented. On the PHP side, it makes use of the mysqlnd-memcached plugin and the Pecl memcached extension. Note that this is NOT the same as using conventional memcached as a cache in front of MySQL - it's a memcached-compatible interface directly into InnoDB - there is no separate memcached server involved.

### Data-Store/Database Mapping Test

* [Database test source Raw](dbraw.php)

## Infrastructure Software Versions
The tests were run with:

* [PHP Version 5.6.1](http://www.php.net/) with FPM and OpCache
* [nginx 1.6.2](http://nginx.org/)
* [MySQL 5.6.20](https://dev.mysql.com/)

## Test URLs

### Data-Store Test

MySQL: http://localhost/dbraw.php

### Variable Query Test

MySQL: http://localhost/queries.php?queries=2

### Update Test

MySQL: http://localhost/updateraw.php

### Fortunes Test

MySQL: http://localhost/fortune.php
