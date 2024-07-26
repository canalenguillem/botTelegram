<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tap to Earn</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>
<body>
    <div id="score">Puntuación: 0</div>
    <div id="userpic"></div>
    <div id="tap-image"></div>
    <script>
        Telegram.WebApp.ready();

        let score = 0;
        const scoreDiv = document.getElementById('score');
        const userPic = document.getElementById('userpic');
        const userId = Telegram.WebApp.initDataUnsafe.user.id;
        const user_name=Telegram.WebApp.initDataUnsafe.user.first_name

        document.getElementById('tap-image').addEventListener('click', function() {
            score++;
            scoreDiv.textContent = 'Puntuación: ' + score+ ' user '+user_name;
            // fetch('http://localhost:5000/update_score', {  // Asegúrate de que esta URL es correcta
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify({ user_id: userId, score: score })
            // })
            // .then(response => response.json())
            // .then(data => console.log(data))
            // .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
