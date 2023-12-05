# Collecte
from global_data import lienPerfRSE, testMail
from utils import sendMail

# Alerte avant le début du mois N : 28 du mois N-1
# Alerte au début de mois N
# Alerte Normale le 3, 6 , 10
# Alerte avant la fin de la collecte : 12 , 14 et 15

def sendAlerteAvantCollecte() :

    style = """body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f2f2f2;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                background-color: #ffc107;
                color: white;
                padding: 10px;
                text-align: center;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background-color: #757575;
                color: white;
                padding: 10px;
                text-align: center;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            .saisie-section {
                background-color: #ffecb3;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
            }
            .saisie-section h2 {
                color: #ff9800;
            }
            .small-text {
                font-size: 80%;
                color: white;
            }
            .link-text {
                color: #039be5; /* Couleur bleu pour le lien */
            }
            .red-text {
                color: red;
                font-weight: bold;
            }
    """

    alerteAvantLeDebutDeLaCollecte = f'''<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notification : Période de Collecte de Données</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Notification de Collecte de Données</h1>
            </div>
            <div class="content">
                <p>Bonjour M. Fabrice HOUESSOU,</p>
                <p>Nous vous informons que la période de collecte des données de <strong>Sucrivoire-Siège</strong> débutera le <span class="red-text">1<sup>er</sup> décembre</span>. Nous vous prions de bien vouloir participer en fournissant les informations nécessaires.</p>
                <p>Veuillez vous connecter <a href="{lienPerfRSE}" class="link-text"> au cadre de saisie des données sur votre tableau de bord</a> pour contribuer au processus de collecte de données.</p>

                <!-- Saisie de données section -->
                <div class="saisie-section">
                    <h2>Saisie de données</h2>
                    <p>Connectez-vous à <a href="{lienPerfRSE}" class="link-text">votre compte</a> et suivez les étapes ci-dessous pour saisir vos données :</p>
                    <ol>
                        <li>Accédez à la section de saisie de données sur votre tableau de bord.</li>
                        <li>Suivez les instructions pour saisir les données requises.</li>
                        <li>Assurez-vous de soumettre vos données avant la date limite.</li>
                    </ol>
                </div>
                <p>Nous vous remercions de votre coopération !</p>
                <p>Cordialement</p>
            </div>
            <div class="footer">
                <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
            </div>
        </div>
    </body>
    </html>
    '''
    subject = "Notification : Période de Collecte de Données - Sucrivoire-Siège"
    recipient_emails = ["fabdev6@gmail.com","ing@visionstrategie.com"]
    for email in recipient_emails :
        sendMail(subject, alerteAvantLeDebutDeLaCollecte, email)

def sendAlerteDebutCollecte() :

    style = """body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f2f2f2;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                background-color: #ffc107;
                color: white;
                padding: 10px;
                text-align: center;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background-color: #757575;
                color: white;
                padding: 10px;
                text-align: center;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            .saisie-section {
                background-color: #ffecb3;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
            }
            .saisie-section h2 {
                color: #ff9800;
            }
            .small-text {
                font-size: 80%;
                color: white;
            }
            .link-text {
                color: #039be5; /* Couleur bleu pour le lien */
            }
            .red-text {
                color: red;
                font-weight: bold;
            }
    """

    alerteCollecte = f"""<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Annonce : Début de la Période de Collecte des Données</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Annonce : Début de la Période de Collecte des Données</h1>
            </div>
            <div class="content">
                <p>Bonjour M. Fabrice HOUESSOU,</p>
                <p>Nous sommes ravis de vous informer que la période de collecte de données de <strong>Sucrivoire-Siège</strong> a officiellement commencé pour ce mois-ci. La collecte se poursuivra jusqu'au <span class="red-text">15 décembre</span>.</p>
                <p>Nous vous encourageons à participer activement en fournissant les informations nécessaires. Veuillez vous connecter au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord (Sucrivoire-Siège)</a> pour contribuer au processus de collecte de données.</p>

                <!-- Saisie de données section -->
                <div class="saisie-section">
                    <h2>Saisie de données</h2>
                    <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                    <ol>
                        <li>Accédez à la section de saisie de données sur <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                        <li>Suivez les instructions pour saisir les données requises.</li>
                        <li>Assurez-vous de soumettre vos données avant la date limite (15 décembre).</li>
                    </ol>
                    <p>Votre participation active est essentielle au succès de cette collecte de données. Merci de contribuer à cet effort.</p>
                </div>
                <p>Nous vous remercions de votre coopération !</p>
                <p>Cordialement</p>
            </div>
            <div class="footer">
                <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
            </div>
        </div>
    </body>
    </html>
    """

    subject = "Annonce : Début de la Période de Collecte des Données - Sucrivoire-Siège"
    recipient_email = "fabdev6@gmail.com"
    sendMail(subject, alerteCollecte, recipient_email)

def sendAlerteCollecte() :

    style = """body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f2f2f2;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                background-color: #ffc107;
                color: white;
                padding: 10px;
                text-align: center;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background-color: #757575;
                color: white;
                padding: 10px;
                text-align: center;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            .saisie-section {
                background-color: #ffecb3;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
            }
            .saisie-section h2 {
                color: #ff9800;
            }
            .small-text {
                font-size: 80%;
                color: white;
            }
            .link-text {
                color: #039be5; /* Couleur bleu pour le lien */
            }
            .red-text {
                color: red;
                font-weight: bold;
            }
    """

    alerteCollecte = f"""<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rappel : Période de Collecte des Données</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Rappel : Période de Collecte des Données</h1>
            </div>
            <div class="content">
                <p>Bonjour M. Fabrice HOUESSOU,</p>
                <p>Nous sommes ravis de vous informer que la période de collecte de données de <strong>Sucrivoire-Siège</strong> a commencé pour ce mois-ci. La collecte se poursuivra jusqu'au <span class="red-text">15 décembre</span>.</p>
                <p>Nous vous encourageons à participer activement en fournissant les informations nécessaires. Veuillez vous connecter au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord (Sucrivoire-Siège)</a> pour contribuer au processus de collecte de données.</p>

                <!-- Saisie de données section -->
                <div class="saisie-section">
                    <h2>Saisie de données</h2>
                    <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                    <ol>
                        <li>Accédez à la section de saisie de données sur  <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> .</li>
                        <li>Suivez les instructions pour renseigner les données requises.</li>
                        <li>Assurez-vous de soumettre vos données avant la date limite (15 décembre).</li>
                    </ol>
                    <p>Votre participation active est essentielle au succès de cette collecte de données. Merci de contribuer à cet effort.</p>
                </div>
                <p>Nous vous remercions de votre coopération !</p>
                <p>Cordialement</p>
            </div>
            <div class="footer">
                <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
            </div>
        </div>
    </body>
    </html>
    """

    subject = "Rappel : Période de Collecte des Données - Sucrivoire-Siège"
    recipient_email = testMail
    sendMail(subject, alerteCollecte, recipient_email)

def sendAlerteFinCollecte() :

    style = """body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f2f2f2;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                background-color: #ffc107;
                color: white;
                padding: 10px;
                text-align: center;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background-color: #757575;
                color: white;
                padding: 10px;
                text-align: center;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            .saisie-section {
                background-color: #ffecb3;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
            }
            .saisie-section h2 {
                color: #ff9800;
            }
            .small-text {
                font-size: 80%;
                color: white;
            }
            .link-text {
                color: #039be5; /* Couleur bleu pour le lien */
            }
            .red-text {
                color: red;
                font-weight: bold;
            }
    """

    alerteAvantLaFinDeLaCollecte = f"""<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alerte : Fin de la Période de Collecte des Données</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Alerte : Fin de la Période de Collecte des Données</h1>
            </div>
            <div class="content">
                <p>Bonjour M. Fabrice HOUESSOU,</p>
                <p>Nous vous informons que la période de collecte de données de <strong>Sucrivoire-Siège</strong> se termine le <span class="red-text">15 décembre</span>. Il reste seulement quelques jours pour la sasie des données. Votre contribution est essentielle pour le succès de cette collecte.</p>
                <p>Veuillez vous connecter  au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text"> votre tableau de bord Sucrivoire-Siège</a>  pour contribuer au processus de collecte de données.</p>

                <!-- Saisie de données section -->
                <div class="saisie-section">
                    <h2>Saisie de données</h2>
                    <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                    <ol>
                        <li>Accédez à la section de saisie de données sur <a href="{lienPerfRSE}" class="link-text"> votre tableau de bord</a> .</li>
                        <li>Suivez les instructions pour saisir les données requises.</li>
                        <li>Assurez-vous de soumettre vos données avant la date limite (15 décembre) .</li>
                    </ol>
                    <p>Votre participation active est grandement appréciée. Merci de contribuer à la réussite de cette collecte de données.</p>
                </div>
                <p>Nous vous remercions de votre coopération !</p>
                <p>Cordialement</p>
            </div>
            <div class="footer">
                <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
            </div>
        </div>
    </body>
    </html>
    """

    subject = "Alerte : Fin de la Période de Collecte des Données - Sucrivoire-Siège"
    recipient_email = "fabdev6@gmail.com"
    sendMail(subject, alerteAvantLaFinDeLaCollecte, recipient_email)