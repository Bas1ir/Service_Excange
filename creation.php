<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mitr:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">


    <title>Document</title>
    <link rel="stylesheet" href="/Service_Excange/css/creation.css">
</head>
<body>
    <div class="wrapper">   
        <div class="logo">
            <a href="uslugi.php"><img src="/Service_Excange/img1/logo.png" alt=""></a>
            <h1>Создание услуги</h1>
        </div>

        <!--======Подробности=======-->

        <h2>Подробности</h2>


        <form action="add_service.php" method="post" enctype="multipart/form-data">

            <!----- Название услуги ----->

            <div class="name">
                <p>Название услуги</p>
                <input type="text" id="title" name="title" required>
            </div>

            <!----- Опыт работы ----->

            <div class="exp">
                <p>Опыт работы</p>
                <input type="text" name="exp" required>
            </div>

            <!----- Адрес ----->

            <div class="address">
                <p>Адрес</p>
                <input type="text" name="address" required>
            </div>

            <!----- Состав рабочих ----->

            <div class="compound">
                <p>Состав рабочих</p>
                <input type="text" name="compound" required>
            </div>

            <!----- Гарантия ----->

            <div class="guarantee">
                <p>Гарантия</p>
                <input type="text" name="guarantee" required>
            </div>

            <!--=====График работы=====-->

            <h2>График работы</h2>
            <div class="day">
                <p>Рабочие дни</p>
                <input type="text" name="day" required>
            </div>

            <div class="time">
                <p>Время работы с .. до ..</p>
                <input type="text" name="time" required>
            </div>

            <!--=====Описание=====-->

            <h2>Описание</h2>
            <div class="description">
                <textarea name="description" required></textarea>
                <p>Не указывайте здесь телефон — для него есть отдельное поле</p>
            </div>

            <!--=====Стоимость=====-->

            <h2>Стоимость одной услуги</h2>
            <div class="price">
                <input  type="text" placeholder="&#8381;" name="price" required>
            </div>

            <!--=====Фотографии=====-->

            <h2>Фотография</h2>
            <div class="photo">
                <input type="file" name="images[]" multiple>
            </div>
            
            <!--=====Контакты=====-->

            <h2>Контакты</h2>
            <div class="phone">
                <p>телефон</p>
                <input type="tel" placeholder="89001234567" name="number" required>
            </div>

            <!--=====Сохранение=====-->
            <button type="submit" class="save">Разместить</button>
        </form>


        <br><br><br><br><br>
</body>
</html>