<?php
require "connect_db.php";
if($conn_db)
echo 'Соединение установлено.';
else
die('Ошибка подключения к серверу баз данных.');
?>