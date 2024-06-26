from global_data import lienPerfRSE
from utils import sendMail, convert_month_to_french
from dbkeys import supabase
import datetime


# Notification de Validation de Données  14 du mois N
# Annonce de Début de Validation de Données le 15 du mois N
# Alerte Période de Validation des Données 18 , 20  25
# Alerte Fin de Collecte de Données  27 , 30

def sendAlerteAvantDebutValidation() :
    current_date = datetime.date.today()
    next_month = current_date.replace(day=28) + datetime.timedelta(days=4)
    mois_suivant = f"{next_month.strftime('%B')}"
    mois_suivant = convert_month_to_french(mois_suivant)

    response = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq("est_validateur", True).execute().data
    responseAdmin = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq('est_admin', True).execute().data

    if responseAdmin:
        for user in responseAdmin:
            response.append(user)

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['nom_entite']
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
        alerteAvantDebutValidation = f"""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Notification : Période de Validation des Données</title>
            <style>
                {style}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Notification : Période de Validation des Données</h1>
                </div>
                <div class="content">
                    <p>Bonjour M. {nom},</p>
                    <p>Nous vous informons que la période de validation de données débutera le <span class="red-text">1<sup>er</sup> {mois_suivant}</span>. Nous vous prions de bien vouloir vous préparer pour cette phase cruciale.</p>
                    <p>Veuillez consulter <a href="{lienPerfRSE}" class="link-text"> votre tableau de bord</a> pour les détails et les prochaines étapes de la validation.</p>

                    <!-- Validation de données section -->
                    <div class="saisie-section">
                        <h2>Validation de Données</h2>
                        <p>Assurez-vous d'être prêt pour la période de validation en suivant ces étapes :</p>
                        <ol>
                            <li>Consultez les données saisies par les contributeurs éditeurs pendant la période de collecte dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                            <li>Vérifiez l'exactitude des données saisies.</li>
                            <li>Validez vos données conformément en cliquant sur la case à cocher.</li>
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
        """
        return alerteAvantDebutValidation
    
    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Notification : Période de Validation des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)


def sendAlerteDebutValidation() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)

    response = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq("est_validateur", True).execute().data
    responseAdmin = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq('est_admin', True).execute().data

    if responseAdmin:
        for user in responseAdmin:
            response.append(user)

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['nom_entite']
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
        alerteDebutValidation = f"""<!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Annonce : Début de la Période de Validation des Données</title>
            <style>
                {style}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Annonce : Début de la Période de Validation des Données</h1>
                </div>
                <div class="content">
                    <p>Bonjour M. {nom},</p>
                    <p>Nous sommes ravis de vous informer que la période de validation de données a officiellement commencé. La validation se poursuivra jusqu'au <span class="red-text">15 {current_month}</span>.</p>
                    <p>Nous vous encourageons à participer activement en vérifiant et validant les informations fournies pendant la période de collecte. Veuillez vous connecter au cadre de validation de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> pour contribuer au processus de validation de données.</p>

                    <!-- Validation de données section -->
                    <div class="saisie-section">
                        <h2>Validation de Données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour la validation de vos données :</p>
                        <ol>
                            <li>Consultez les données saisies par les contributeurs éditeurs pendant la période de collecte dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                            <li>Vérifiez l'exactitude des données saisies.</li>
                            <li>Validez vos données en cliquant sur la case à cocher.</li>
                        </ol>
                        <p>Votre participation active est essentielle au succès de cette validation de données. Merci de contribuer à cet effort.</p>
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
        return alerteDebutValidation

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Annonce : Début de la Période de Validation des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)


def sendAlerteValidation() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)

    response = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq("est_validateur", True).execute().data
    responseAdmin = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq('est_admin', True).execute().data

    if responseAdmin:
        for user in responseAdmin:
            response.append(user)

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['nom_entite']
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
        alerteValidation = f"""<!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rappel : Période de Validation des Données</title>
            <style>
                {style}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Rappel : Période de Validation des Données</h1>
                </div>
                <div class="content">
                    <p>Bonjour M. {nom},</p>
                    <p>Nous vous rappelons que la période de validation de données a commencé. La validation se poursuivra jusqu'au <span class="red-text">15 {current_month}</span>.</p>
                    <p>Nous vous encourageons à participer activement en vérifiant et validant les informations fournies pendant la période de collecte. Veuillez vous connecter au cadre de validation de données dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> pour contribuer au processus de validation de données.</p>

                    <!-- Saisie de données section -->
                    <div class="saisie-section">
                        <h2>Validation des Données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour la saisie de vos données :</p>
                        <ol>
                            <li>Consultez les données saisies par les contributeurs éditeurs pendant la période de collecte dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                            <li>Vérifiez l'exactitude des données saisies.</li>
                            <li>Validez vos données en cliquant sur la case à cocher.</li>
                        </ol>
                        <p>Votre participation active est essentielle au succès de cette validation de données. Merci de contribuer à cet effort.</p>
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
        return alerteValidation

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Rappel : Période de Validation des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)


def sendAlerteFinValidation() :
    current_date = datetime.date.today()
    current_month = current_date.strftime('%B')
    current_month = convert_month_to_french(current_month)

    response = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq("est_validateur", True).execute().data
    responseAdmin = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq('est_admin', True).execute().data

    if responseAdmin:
        for user in responseAdmin:
            response.append(user)

    dictionnaire_utilisateurs = {}

    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['nom_entite']
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
        alerteFinDeValidation = f"""<!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Alerte : Période de Fin de la Validation des Données</title>
            <style>
                {style}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Alerte : Période de Fin de la Validation des Donnéess</h1>
                </div>
                <div class="content">
                    <p>Bonjour M. {nom},</p>
                    <p>Nous vous informons que la période de validation des données se termine le <span class="red-text">15 {current_month}</span>. Il reste seulement quelques jours pour la saisie des données. Votre contribution est essentielle pour le succès de cette collecte.</p>
                    <p>Veuillez vous connecter dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a> pour valider les données.</p>

                    <!-- Saisie de données section -->
                    <div class="saisie-section">
                        <h2>Saisie de données</h2>
                        <p>Connectez-vous à votre compte et suivez les étapes ci-dessous pour saisir vos données :</p>
                        <ol>
                            <li>Consultez les données saisies par les contributeurs éditeurs pendant la période de collecte dans <a href="{lienPerfRSE}" class="link-text">votre tableau de bord</a>.</li>
                            <li>Vérifiez l'exactitude des données saisies.</li>
                            <li>Validez vos données en cliquant sur la case à cocher.</li>
                        </ol>
                        <p>Votre participation active est grandement appréciée. Merci de contribuer à la réussite de la validation de données.</p>
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
        return alerteFinDeValidation

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Alerte : Période de Fin de la Validation des Données"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)





