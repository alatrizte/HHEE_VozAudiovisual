from datetime import datetime, timedelta
from databaseHoras import Database
data = Database('horasVoz.db')

class dias_semana:

    def __init__(self, dia):
        
        nombre_produccion = data.imprimir_dias_semana(dia)[0][1]
        
        dia=dia + " 00:00:00"
        dia = datetime.strptime(dia, '%d/%m/%Y %H:%M:%S')
        # Empieza sabiendo el día en número de la semana
        week_day=dia.isocalendar()[2]
        # Calcula el dia de inicio de la semana restando con timedelta los días menos 1
        start_date=dia - timedelta(days=week_day-1)
        # imprime en una lista los días de esa semana
        dias = [str((start_date + timedelta(days=i)).date().strftime("%d/%m/%Y")) for i in range(5)]
        
        dates = []
        for day in dias:
            enLabase=data.imprimir_dias_semana(day)
            if enLabase != [] and enLabase[0][1] == nombre_produccion:
                dates.append(day)
        print(dates)
        
        self.returncode = dates
