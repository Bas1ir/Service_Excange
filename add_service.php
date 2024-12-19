<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "registeruser";

// Создаем подключение
$conn = new mysqli($servername, $username, $password, $dbname);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    foreach ($_FILES['images']['tmp_name'] as $key => $tmp_name) {
        $file_name = $_FILES['images']['name'][$key];
        $file_path = 'uploads/' . basename($file_name);

        if (move_uploaded_file($tmp_name, $file_path)) {
            $conn->query("INSERT INTO services (img) VALUES ('$file_path')");
        }
    }
}


// Проверка подключения
if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}


// Получаем данные из формы
$title = $_POST['title'];
$exp = $_POST['exp'];
$address = $_POST['address'];
$compound = $_POST['compound'];
$guarantee = $_POST['guarantee'];
$day = $_POST['day'];
$time = $_POST['time'];
$description = $_POST['description'];
$price = $_POST['price'];
$number = $_POST['number'];



if(empty($title) || empty($exp) || empty($address) || empty($compound) || empty($guarantee) || 
empty($day) || empty($time) || empty($description) || empty($price) || empty($number)){
    echo "Заполните все поля";
} else{
// SQL-запрос для вставки новых данных
    $sql = "INSERT INTO services (title, exp, address, compound, guarantee, day, time, description, price, number, img)
    VALUES ('$title', '$exp', '$address' ,'$compound', '$guarantee', '$day', '$time', '$description', '$price', '$number', '$file_path')";

    if ($conn -> query($sql) === TRUE){
        header('Location: uslugi.php');
    }else{
        echo "Ошибка:" .$conn->error;
    }
}

$conn->close();
?>
