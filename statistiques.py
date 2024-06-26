# Statistiques mensuelles Collecte et Validation chaque du 02 du mois N-1
from datetime import datetime

from global_data import testMail
from utils import sendMail
from dbkeys import supabase

# Statistiques mi-parcours Collecte et Validation chaque 10 15 20 25

statsMiParcours = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistiques de Collecte et de Validation Mensuelles</title>
    <style>
        body {
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
            background-color: #FFC107; /* Amber */
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
            background-color: #BDBDBD; /* Grey */
            padding: 10px;
            text-align: center;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
            text-align: left;
        }
        th, td {
            padding: 10px;
        }
        th {
            background-color: #FFC107; /* Amber */
            color: white;
        }
        .blue-bold {
            color: #039be5; /* Bold Blue */
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Statistiques de Collecte et de Validation Mensuelles</h1>
        </div>
        <div class="content">
            <p>Bonjour M. Fabrice HOUESSOU,</p>
            <p>Voici les statistiques de collecte et de validation pour le mois de Janvier 2022 pour <span class="blue-bold">Sucrivoire-Siège</span> :</p>

            <table>
                <tr>
                    <th>Métrique</th>
                    <th>Collecte</th>
                    <th>Validation</th>
                </tr>
                <tr>
                    <td>Nombre de données éditées</td>
                    <td>200</td>
                    <td>150</td>
                </tr>
                <tr>
                    <td>Total des données attendues</td>
                    <td>300</td>
                    <td>300</td>
                </tr>
            </table>

            <p>Vous êtes encouragé à continuer la saisie ou la validation des données !</p>

            <p>Merci pour votre contribution !</p>
        </div>
        <div class="footer">
            <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
            <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
        </div>
    </div>
</body>
</html>"""


def sendStatsMensuelles():
    response = supabase.table('AccesPilotage').select('email, nom_entite, Users(nom, prenom)').eq("est_validateur", True).eq('Users.fonction', 'Responsable').execute().data

    print(response)
    dictionnaire_utilisateurs = {}
    for utilisateur in response:
        email = utilisateur['email']
        entite = utilisateur['nom_entite']
        utilisateurs = utilisateur['Users']
        noms_complets = [f"{user['prenom']} {user['nom']}" for user in utilisateurs]
        dictionnaire_utilisateurs[email] = (noms_complets, entite)

    listEmail = list(dictionnaire_utilisateurs.keys())
    def mailBody(nom, entite):
        statsMensuelles = """<!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Statistiques de Collecte et de Validation Mensuelles</title>
            <style>
                body {
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
                    background-color: #FFC107; /* Amber */
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
                    background-color: #BDBDBD; /* Grey */
                    padding: 10px;
                    text-align: center;
                    border-bottom-left-radius: 10px;
                    border-bottom-right-radius: 10px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                table, th, td {
                    border: 1px solid #ddd;
                    text-align: left;
                }
                th, td {
                    padding: 10px;
                }
                th {
                    background-color: #FFC107; /* Amber */
                    color: white;
                }
                .blue-bold {
                    color: #039be5; /* Bold Blue */
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Statistiques de Collecte et de Validation Mensuelles</h1>
                </div>
                <div class="content">
                    <p>Bonjour M. Fabrice HOUESSOU,</p>
                    <p>Voici les statistiques de collecte et de validation pour le mois de Janvier 2022 pour <span class="blue-bold">Sucrivoire-Siège</span> :</p>

                    <table>
                        <tr>
                            <th>Métrique</th>
                            <th>Collecte</th>
                            <th>Validation</th>
                        </tr>
                        <tr>
                            <td>Nombre de données éditées</td>
                            <td>200</td>
                            <td>150</td>
                        </tr>
                        <tr>
                            <td>Total des données attendues</td>
                            <td>300</td>
                            <td>300</td>
                        </tr>
                    </table>

                    <p>Merci pour votre participation active !</p>
                </div>
                <div class="footer">
                    <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                    <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
                </div>
            </div>
        </body>
        </html>
        """
        return statsMensuelles

    for mail in listEmail :
        name = dictionnaire_utilisateurs[mail][0][0]
        entity = dictionnaire_utilisateurs[mail][1]
        subject = f"Statistiques Mensuelles - {entity}"
        sendMail(subject, mailBody(nom=name, entite=entity), mail)


def sendStatsMiParcours():
    statsMiParcours = """<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Statistiques de Collecte et de Validation Mensuelles</title>
        <style>
            body {
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
                background-color: #FFC107; /* Amber */
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
                background-color: #BDBDBD; /* Grey */
                padding: 10px;
                text-align: center;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            table, th, td {
                border: 1px solid #ddd;
                text-align: left;
            }
            th, td {
                padding: 10px;
            }
            th {
                background-color: #FFC107; /* Amber */
                color: white;
            }
            .blue-bold {
                color: #039be5; /* Bold Blue */
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Statistiques de Collecte et de Validation Mensuelles</h1>
            </div>
            <div class="content">
                <p>Bonjour M. Fabrice HOUESSOU,</p>
                <p>Voici les statistiques de collecte et de validation pour le mois de Janvier 2022 pour <span class="blue-bold">Sucrivoire-Siège</span> :</p>

                <table>
                    <tr>
                        <th>Métrique</th>
                        <th>Collecte</th>
                        <th>Validation</th>
                    </tr>
                    <tr>
                        <td>Nombre de données éditées</td>
                        <td>200</td>
                        <td>150</td>
                    </tr>
                    <tr>
                        <td>Total des données attendues</td>
                        <td>300</td>
                        <td>300</td>
                    </tr>
                </table>

                <p>Vous êtes encouragé à continuer la saisie ou la validation des données !</p>

                <p>Merci pour votre contribution !</p>
            </div>
            <div class="footer">
                <p>Si vous avez des questions, veuillez nous contacter à l'adresse projet.dd@vsionstrategie.com</p>
                <p class="small-text">Veuillez ne pas répondre à ce mail.</p>
            </div>
        </div>
    </body>
    </html>"""
    subject = "Statistiques Mensuelles - Sucrivoire-Siège"
    recipient_email = testMail
    sendMail(subject, statsMiParcours, recipient_email)
