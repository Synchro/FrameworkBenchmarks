
import subprocess
import sys
import setup_util
import os
from os.path import expanduser

home = expanduser("~")

def start(args, logfile, errfile):
  setup_util.replace_text("php-mysql-memcached/dbraw.php", "host=.*;", "host=" + args.database_host + ";")
  setup_util.replace_text("php-mysql-memcached/updateraw.php", "host=.*;", "host=" + args.database_host + ";")
  setup_util.replace_text("php-mysql-memcached/fortune.php", "host=.*;dbname", "host=" + args.database_host + ";dbname")
  setup_util.replace_text("php-mysql-memcached/deploy/nginx.conf", "root .*\/FrameworkBenchmarks", "root " + home + "/FrameworkBenchmarks")
  
  try:
    if os.name == 'nt':
      subprocess.check_call('appcmd add site /name:PHP /bindings:http/*:8080: /physicalPath:"C:\\FrameworkBenchmarks\\php-mysql-memcached"', shell=True, stderr=errfile, stdout=logfile)
      return 0
    
    subprocess.check_call("sudo php-fpm --fpm-config config/php-fpm.conf -g " + home + "/FrameworkBenchmarks/php-mysql-memcached/deploy/php-fpm.pid", shell=True, stderr=errfile, stdout=logfile)
    subprocess.check_call("sudo /usr/local/nginx/sbin/nginx -c " + home + "/FrameworkBenchmarks/php-mysql-memcached/deploy/nginx.conf", shell=True, stderr=errfile, stdout=logfile)
    
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop(logfile, errfile):
  try:
    if os.name == 'nt':
      subprocess.check_call('appcmd delete site PHP', shell=True, stderr=errfile, stdout=logfile)
      return 0
    
    subprocess.call("sudo /usr/local/nginx/sbin/nginx -s stop", shell=True, stderr=errfile, stdout=logfile)
    subprocess.call("sudo kill -QUIT $( cat php/deploy/php-fpm.pid )", shell=True, stderr=errfile, stdout=logfile)
    
    return 0
  except subprocess.CalledProcessError:
    return 1
