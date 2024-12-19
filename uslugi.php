<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mitr:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
    

    <title>Услуги</title>
    <link rel="stylesheet" href="/Service_Excange/css/uslugi.css">
    <style>
        .body{
            margin: 0;
            font-family: "Montserrat", sans-serif;
        }
        .wrapper{
            max-width: 1004px;/*для выравнивания текста*/
            margin: 0 auto;
            display: flex;
        }
        .square{
            position: absolute;
            background-color: rgba(114, 125, 249, 1);
            width: 100%;
            height: 173px;
        }
        .filtr{
            position: relative;
            top: 53px;
            right: 11px;
            width: 67px;
            height: 67px;
            border: none;
            outline: none;
            background: transparent;
            cursor: pointer;
        }
        .search{
            display: flex;
        }
        .search input {
            background:white;
            font-size: 26px;
            font-weight: 400;
            line-height: 31.5px;
            text-align: left;

            outline: none;
            border: none;
            position: relative;
            left: 14px;
            top: 53px;
            width: 888px;
            height: 65px;
            padding-left: 10px;
            border-radius: 15px;
        }
        .search button {
            position: relative; 
            top: 70px;
            right: 40px;
            width: 33px;
            height: 33px;
            border: none;
            outline: none;
            background: white;
            cursor: pointer;
        }
        .wrapper input::placeholder{
            color: black;
        }
        .profile{
            position: relative;
            top: 53px;
            width: 67px;
            height: 67px;
            border: none;
            outline: none;
            background: transparent;
            cursor: pointer;    
        }
        .uslugi{
            max-width: 1300px;
            margin: 0 auto;
        }
        .service {
            position: relative;
            top: 110px;
            border: 3px solid rgba(109, 121, 247, 1);
            border-radius: 20px;
            padding: 15px;
            margin: 30px;
            width: 350px;
            float: left;
            box-sizing: border-box;
        }
        .service h2{
            font-size: 30px ;
        }
        .service p{
            font-size: 20px;
        }
        .clearfix {
            clear: both;
        }
        .service img{
            border-radius: 20px;
            position: relative;
            left: 25px;
            width: 270px;
            height: 270px;
        }
        
    </style>    
</head>
<body class="body">

<header class="header">
        <div class="square"></div>
        <div class="wrapper">
            <form action="creation.php">
                <button class="filtr"><img src="/Service_Excange/img1/+.svg" alt=""></button>
            </form>
                <div class="search">
                <input type="text" placeholder="Поиск">
                <button><img src="/Service_Excange/img1/поиск.svg" alt=""></button>
            </div>
            </div>  
    </header>

    <div class = "uslugi">
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

        // SQL-запрос для получения услуг
        $sql = "SELECT id, title, price, img FROM services";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<div class='service'>";
                echo '<img src="' . $row['img'] . '" alt="">';
                echo "<h2>" . $row["title"]. "</h2>";
                echo "<p>" . $row["price"]. "</p>";
                echo "<a href='service_detail.php?id=" . $row["id"] . "'>Подробнее</a>";
                echo "</div>";
            }
        } else {
            echo "Услуги не найдены.";
        }

        $conn->close();
        ?>
    </div>
</body>
</html> 
