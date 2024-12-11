<?php

require_once('db.php'); /*Подключение к бд*/

$login = $_POST['login'];
$email = $_POST['email'];
$pass = $_POST['pass'];

if (empty($login) || empty($email) || empty($pass)){
    echo "Заполните все поля";
} else
{

    $sql = "INSERT INTO `users` (login,email,pass) VALUES('$login', '$email', '$pass')";
    if ($conn -> query($sql) === TRUE){
        header('Location: log.html');
    }else{
        echo "Ошибка:" .$conn->error;
    }

}