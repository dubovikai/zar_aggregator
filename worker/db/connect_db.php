<?php

$serv_name =$_ENV['DB_SERVER'];
$user_name =$_ENV['DB_USER'];
$pass = $_ENV['DB_PASSWORD'];
$bd_name = $_ENV['DB_DB'];
$conn_db = mysqli_connect($serv_name, $user_name, $pass, $bd_name);

?>