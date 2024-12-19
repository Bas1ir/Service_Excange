<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Mitr:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">

    <title>Детали Услуги</title>
    <style>
        body{
            font-family:"Montserrat", sans-serif;
            position: relative;
            top: 50px;
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
        }
        .img img{
            width:600px;
            position: relative;
            top: 40px;
        }

        .additional{
            width: 600px;
        }
        .additional p{
            position: relative;
            top: 50px;
        }
        
        .main{
            width: 400px;
            position: relative;
            top: 110px;
            left: 50px;
        }
        h1{
            font-size: 50px;
            color: rgba(114, 125, 249, 1);
        }
        h2{
            font-size:25px;
        }
        .logo img{
            width: 300px;
            height: 100px;
        }
        .number{
            width:155px;
            height: 30px;
            color:white;
            border: 5px solid rgba(114, 125, 249, 1);
            border-radius:5px;
            background-color: rgba(114, 125, 249, 1);
        }
        h3{
            font-size: 28px;
            position: relative;
            top: 50px;
        }
        p{
            font-size:24px;
        }
    </style>
</head>
<body>
    <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "registeruser";

    // Создаем подключение
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Проверка подключения
    if ($conn->connect_error) {
        die("Ошибка подключения: " . $conn->connect_error);
    }

    // Получение ID услуги из GET-запроса
    $id = $_GET['id'];

    // SQL-запрос для получения полной информации об услуге
    $sql = "SELECT title, exp, address, compound, guarantee, day, time, description, price, number, img FROM services WHERE id = $id";
    $result = $conn->query($sql);
    

    $sql1 = "SELECT login, email FROM users WHERE id = $id";
    $result1 = $conn->query($sql1);


    if ($result->num_rows > 0){
        $row = $result->fetch_assoc();
        $row1 = $result1->fetch_assoc();

        echo "<div class='additional'>";
        echo "<div class='logo'>";
            echo '<a href="uslugi.php"><img src="/Service_Excange/img1/logo.png" alt=""></a>';
        echo "</div>";
        echo "<div class='img'>";
            echo '<img src="' . $row['img'] . '" alt="">';
        echo "</div>";
        echo "<h3> Опыт работы: </h3>";
        echo "<p>" . $row["exp"] . "</p>";
        echo "<h3> Ваш адрес: </h3>";
        echo "<p>" . $row["address"] . "</p>";
        echo "<h3> Состав рабочих: </h3>";
        echo "<p>" . $row["compound"] . "</p>";
        echo "<h3> Гарантия: </h3>";
        echo "<p>" . $row["guarantee"] . "</p>";
        echo "<h3> Подробное описание: </h3>";
        echo "<p>" . $row["description"] . "</p>";
        echo "<h3> Рабочие дни: </h3>";
        echo "<p>" . $row["day"] . "</p>";
        echo "<h3> Время работы с .. до ..: </h3>";
        echo "<p>" . $row["time"] . "</p>";
        echo "</div>";

        echo "<div class='main'>";

        echo "<h1>" . $row["title"] . "</h1>";
        echo "<h2>" . $row["price"] . "</h2>";
        echo "<h2 class='number'>" . $row["number"] . "</h2>";
        echo "<h2>" . $row1['login'] . "</h1>";
        echo "</div>";
    } else {
        echo "Услуга не найдена.";
    }

    $conn->close();
    ?>
</body>
</html>

