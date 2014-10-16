<?php
//
// Database Test
//

// MySQL database connection
$mysqli = new mysqli('localhost', 'benchmarkdbuser', 'benchmarkdbpass', 'hello_world');

//MySQL memcached connection
$memcached = new Memcached;
$memcached->addServer('localhost', 11212);

//Associate mysqli and memcached connections
mysqlnd_memcache_set($mysqli, $memcached);

// Read number of queries to run from URL parameter
$query_count = 1;
if (isset($_GET['queries'])) {
  $query_count = $_GET['queries'];
}

// Create an array with the response string.
$arr = array();

// For each query, store the result set values in the response array
while (0 < $query_count--) {
  $id = mt_rand(1, 10000);
  $r = $mysqli->query('SELECT randomNumber FROM World WHERE id = '.(integer)$id);
  // Store result in array.
  $arr[] = array('id' => $id, 'randomNumber' => $r->fetch_row()[0]);
}

// Use the PHP standard JSON encoder.
// http://www.php.net/manual/en/function.json-encode.php
if (count($arr) == 1) {
  $arr = $arr[0];
}

echo json_encode($arr);
