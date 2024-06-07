# Collecte
from global_data import lienPerfRSE
from utils import sendMail, convert_month_to_french
from dbkeys import supabase
import datetime

# Alerte avant le début du mois N : 28 du mois N-1
# Alerte au début de mois N
# Alerte Normale le 3, 6 , 10
# Alerte avant la fin de la collecte : 12 , 14 et 15

def sendAlerteAvantCollecte() :
    current_date = datetime.date.today()
    next_month = current_date.replace(day=28) + datetime.timedelta(days=4)
    mois_suivant = f"{next_month.strftime('%B')}"
    mois_suivant = convert_month_to_french(mois_suivant)

    response = supabase.table('AccesPilotage').select('email, entite, Users(nom, prenom)').eq("est_editeur", True).execute().data

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['entite']
        utilisateurs = utilisateur['Users']
        noms_complets = [f"{user['prenom']} {user['nom']}" for user in utilisateurs]
        dictionnaire_utilisateurs[email] = (noms_complets, entite)

    listEmail = list(dictionnaire_utilisateurs.keys())


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
    def mailBody(nom, entite):
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
                    <p>Bonjour M. {nom},</p>
                    <p>Nous vous informons que la période de collecte des données débutera le <span class="red-text">1<sup>er</sup> {mois_suivant}</span>. Nous vous prions de bien vouloir participer en fournissant les informations nécessaires.</p>
                    <p>Veuillez vous connecter <a href="{lienPerfRSE}" class="link-text"> au cadre de saisie des données sur votre tableau de bord</a> pour contribuer au processus de collecte de données de vos filiales.</p>

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
        return alerteAvantLeDebutDeLaCollecte
    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Notification : Période de Collecte de Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)


def sendAlerteDebutCollecte() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)

    response = supabase.table('AccesPilotage').select('email, entite, Users(nom, prenom)').eq("est_editeur", True).execute().data

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['entite']
        utilisateurs = utilisateur['Users']
        noms_complets = [f"{user['prenom']} {user['nom']}" for user in utilisateurs]
        dictionnaire_utilisateurs[email] = (noms_complets, entite)
    

    listEmail = list(dictionnaire_utilisateurs.keys())

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

    def mailBody(nom, entite):
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
                    <p>Bonjour M. {nom},</p>
                    <p>Nous sommes ravis de vous informer que la période de collecte de données a officiellement commencé pour ce mois-ci. La collecte se poursuivra jusqu'au <span class="red-text">15 {current_month}</span>.</p>
                    <p>Nous vous encourageons à participer activement en fournissant les informations nécessaires. Veuillez vous connecter au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> pour contribuer au processus de collecte de données.</p>

                    <!-- Saisie de données section -->
                    <div class="saisie-section">
                        <h2>Saisie de données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                        <ol>
                            <li>Accédez à la section de saisie de données sur <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                            <li>Suivez les instructions pour saisir les données requises.</li>
                            <li>Assurez-vous de soumettre vos données avant la date limite (15 {current_month}).</li>
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
        return alerteCollecte
    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Annonce : Début de la Période de Collecte des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)

def sendAlerteCollecte() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)
    response = supabase.table('AccesPilotage').select('email, entite, Users(nom, prenom)').eq("est_editeur", True).execute().data

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['entite']
        utilisateurs = utilisateur['Users']
        noms_complets = [f"{user['prenom']} {user['nom']}" for user in utilisateurs]
        dictionnaire_utilisateurs[email] = (noms_complets, entite)
    

    listEmail = list(dictionnaire_utilisateurs.keys())

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

    def mailBody(nom, entite):
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
                    <p>Bonjour M. {nom},</p>
                    <p>Nous sommes ravis de vous informer que la période de collecte de données a commencé pour ce mois-ci. La collecte se poursuivra jusqu'au <span class="red-text">15 {current_month}</span>.</p>
                    <p>Nous vous encourageons à participer activement en fournissant les informations nécessaires. Veuillez vous connecter au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord </a> pour contribuer au processus de collecte de données.</p>

                    <!-- Saisie de données section -->
                    <div class="saisie-section">
                        <h2>Saisie de données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                        <ol>
                            <li>Accédez à la section de saisie de données sur  <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> .</li>
                            <li>Suivez les instructions pour renseigner les données requises.</li>
                            <li>Assurez-vous de soumettre vos données avant la date limite (15 {current_month}).</li>
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
        return alerteCollecte

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Rappel : Période de Collecte des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)

def sendAlerteFinCollecte() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)
    response = supabase.table('AccesPilotage').select('email, entite, Users(nom, prenom)').eq("est_editeur", True).execute().data

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['entite']
        utilisateurs = utilisateur['Users']
        noms_complets = [f"{user['prenom']} {user['nom']}" for user in utilisateurs]
        dictionnaire_utilisateurs[email] = (noms_complets, entite)
    

    listEmail = list(dictionnaire_utilisateurs.keys())

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

    def mailBody (nom, entite):
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
                    <p>Bonjour M. {nom},</p>
                    <p>Nous vous informons que la période de collecte de données se termine le <span class="red-text">15 {current_month}</span>. Il reste seulement quelques jours pour la sasie des données. Votre contribution est essentielle pour le succès de cette collecte.</p>
                    <p>Veuillez vous connecter  au cadre de saisie de données dans <a href="{lienPerfRSE}" class="link-text"> votre tableau de bord</a>  pour contribuer au processus de collecte de données.</p>

                    <!-- Saisie de données section -->
                    <div class="saisie-section">
                        <h2>Saisie de données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                        <ol>
                            <li>Accédez à la section de saisie de données sur <a href="{lienPerfRSE}" class="link-text"> votre tableau de bord</a> .</li>
                            <li>Suivez les instructions pour saisir les données requises.</li>
                            <li>Assurez-vous de soumettre vos données avant la date limite (15 {current_month}) .</li>
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
        return alerteAvantLaFinDeLaCollecte

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Alerte : Fin de la Période de Collecte des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)