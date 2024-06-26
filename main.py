#from datetime import datetime
import datetime
import schedule
import time
import calendar

from collecte_data import sendAlerteAvantCollecte, sendAlerteDebutCollecte ,sendAlerteCollecte, sendAlerteFinCollecte
from statistiques import sendStatsMensuelles, sendStatsMiParcours
from validation_data import sendAlerteAvantDebutValidation, sendAlerteDebutValidation, sendAlerteValidation, \
    sendAlerteFinValidation

current_date = datetime.date.today()
days_in_current_month = calendar.monthrange(current_date.year, current_date.month)[1]

#schedule.every().day.at("00:00").do(lambda: sendStatsMensuelles() if datetime.now().day == 2 else None)
schedule.every().minute.do(lambda: sendStatsMensuelles())
schedule.every().day.at("00:00").do(lambda: sendStatsMiParcours() if datetime.now().day in [10, 15, 20, 25] else None)

# Planification des tâches d'alerte sur la collecte des données

schedule.every().day.at("00:00").do(lambda: sendAlerteAvantCollecte() if datetime.now().day == days_in_current_month else None)
#schedule.every().minute.do(lambda: sendAlerteAvantCollecte())
schedule.every().day.at("00:00").do(lambda: sendAlerteDebutCollecte() if datetime.now().day == 1 else None)
schedule.every().day.at("00:00").do(lambda: sendAlerteCollecte()() if datetime.now().day in [3, 6, 10] else None)
schedule.every().day.at("00:00").do(lambda: sendAlerteFinCollecte() if datetime.now().day in [12, 14, 15] else None)

# Planification des tâches d'alerte sur la validation des données

schedule.every().day.at("00:00").do(lambda: sendAlerteAvantDebutValidation() if datetime.now().day == 28 else None)
schedule.every().day.at("00:00").do(lambda: sendAlerteDebutValidation() if datetime.now().day == 1 else None)
schedule.every().day.at("00:00").do(lambda: sendAlerteValidation() if datetime.now().day in [3, 6, 10] else None)
schedule.every().day.at("00:00").do(lambda: sendAlerteFinValidation() if datetime.now().day in [27, 30] else None)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScript termi++nated by user.")


