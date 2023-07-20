import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS horas (id INTEGER PRIMARY KEY, produccion, fecha, entradaOrden,\
         salidaOrden, pausa, entrada, salida, horas, desplazamiento, retraso)")
        self.conn.commit()

    def listar(self):
        self.cur.execute("SELECT * FROM horas")
        rows = self.cur.fetchall()
        return rows

    def insert(self, produccion, fecha, entradaOrden, salidaOrden, pausa, entrada, salida, horas, desplazamiento, retraso):
        self.cur.execute("INSERT INTO horas VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (produccion, fecha, entradaOrden, salidaOrden, pausa,
             entrada, salida, horas, desplazamiento, retraso))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM horas WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, produccion, fecha, entradaOrden, salidaOrden, pausa, entrada, salida, horas, desplazamiento, retraso):
        self.cur.execute("UPDATE horas SET produccion = ?, fecha = ?, entradaOrden = ?, salidaOrden = ?, pausa = ?,\
            entrada = ?, salida = ?, horas = ?, desplazamiento = ?, retraso = ? WHERE id = ?", (produccion, fecha, entradaOrden, salidaOrden, pausa,
            entrada, salida, horas, desplazamiento, retraso, id))
        self.conn.commit()

    def suma_de_horas(self, dia):
        self.cur.execute("SELECT horas FROM horas WHERE fecha = ?", (dia,))
        horaE = self.cur.fetchall()
        return horaE

    def imprimir_dias_semana(self, dia):
        self.cur.execute("SELECT * FROM horas WHERE fecha = ?", (dia,))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()
