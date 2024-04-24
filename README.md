<head>
<style>
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #222;
}
.stream-deck {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
    width: 300px;
    background-color: #333;
    padding: 10px;
    border-radius: 10px;
}
.deck-button {
    display: block;
    background-color: #444;
    color: #fff;
    text-decoration: none;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    font-size: 14px;
    overflow: hidden; /* Ensures images do not overflow the button */
}
.deck-button img {
    width: 100%; /* Adjusts the image width to fit the button */
    height: auto; /* Maintains the aspect ratio of the image */
}
.deck-button:hover {
    background-color: #555;
}
</style>
<body>
    <div class="stream-deck">
        <a href="https://www.instagram.com/the.lv.boys" class="deck-button">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png" alt="Instagram">
        </a>
        <a href="https://discord.gg/7dBDFYxUKV" class="deck-button">
            <img src="https://static.vecteezy.com/system/resources/previews/023/986/880/original/discord-logo-discord-logo-transparent-discord-icon-transparent-free-free-png.png" alt="Discord">
        </a>
        <a href="https://www.youtube.com/@TheLavegaBoys-tlvb" class="deck-button">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png" alt="Youtube">
        </a>
        <a href="https://thelavegaboys1.odoo.com/web?reload=true#action=114&cids=1&menu_id=74&active_id=discuss.channel_1'" class="deck-button">
            <img src="https://play-lh.googleusercontent.com/Zv2I5VIii0ZK9sJ2FgPFZxynVqtcenDZkO9BUYMO-35sTExs21OsGXEj2kQQFkk2ww=w240-h480-rw" alt="Odoo">
        </a>
        <a href="https://classroom.google.com/c/NTk1NDMzNzcxNDk0?cjc=fukwqtc" class="deck-button">
            <img src="https://seeklogo.com/images/G/google-classroom-logo-AD2BE4B278-seeklogo.com.png" alt="Google Classroom">
        </a>
        <a href="https://docs.google.com/document/d/1Sl_gFnhUH7o2Mloflf6DfXHYOAnpCrjt06LZfpKbw5M/edit?usp=sharing" class="deck-button">
            <img src="https://mailmeteor.com/logos/assets/PNG/Google_Docs_Logo_512px.png" alt="Google Docs">
        </a>
    </div>
</body>
</head>