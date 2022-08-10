<?php
$sleep_time = 60;
$token = '1581335512:AAGUsPp8Dxep9jvmNfUtKYjNQaTXHIiDhzM';
    $chat_id = array('475630757');
    $message = 'Сервер '.$host.' недоступен! '. date('l jS \of F Y h:i:s A');

while(1) {
    exec("ping -c 4 " . $_ENV['DOMAIN'], $output, $result);

    if ($result != 0) 
        foreach ($chat_id as $id) 
            file_get_contents('https://api.telegram.org/bot'.$token.'/sendMessage?chat_id='.$id.'&text='.$message);

        // Время сна Демона между итерациями
    sleep($sleep_time); 
}
?>
