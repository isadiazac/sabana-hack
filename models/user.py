from mongoengine import Document, StringField, ListField, IntField, BooleanField, connect

# Conectar a tu base de datos MongoDB
connect('nombre_de_tu_base_de_datos')  # Reemplaza con el nombre de tu base de datos

class Pacient(Document):
    # Campos básicos
    nodulo = BooleanField(required=True)  # 0.No, 1.Si
    morfologia = StringField(choices=['Ovalado', 'Redondo', 'Irregular'], required=True)
    margenes = ListField(StringField(choices=[
        'Circunscritos',
        'Microlobulados',
        'Indistintos o mal definidos',
        'Obscurecidos',
        'Espiculados'
    ]), required=True)

    # Densidad del nódulo
    densidad = StringField(choices=['Densidad Grasa', 'Baja Densidad', 'Igual Densidad', 'Alta Densidad'], required=True)

    # Presencia de microcalcificaciones
    microcalcificaciones = BooleanField(required=True)  # 0.No, 1.Si

    # Calcificaciones típicamente benignas
    calcificaciones_benignas = ListField(StringField(choices=[
        'Cutaneas',
        'Vasculares',
        'Gruesas o Pop Corn',
        'Leño o Vara',
        'Redondas o puntiformes',
        'Anulares',
        'Distroficas',
        'Leche de Calcio',
        'Suturas'
    ]), required=False)

    # Calcificaciones morfología sospechosa
    calcificaciones_sospechosas = ListField(StringField(choices=[
        'Gruesas heterogeneas',
        'Amorfas',
        'Finas pleomorficas',
        'Lineas fianas o lineales ramificadas'
    ]), required=False)

    # Distribución de las calcificaciones
    distribucion_calcificaciones = ListField(StringField(choices=[
        'Difusas',
        'Regionales',
        'Agrupadas (cumulo)',
        'Segmentaria',
        'Lineal'
    ]), required=False)

    # Presencia de asimetrias
    asimetrias = BooleanField(required=True)  # 0.No, 1.Si

    # Tipo de asimetría
    tipo_asimetria = StringField(choices=[
        'Asimetria',
        'Asimetria global',
        'Asimetria focal',
        'Asimetria focal evolutiva'
    ], required=False)

    # Hallazgos asociados
    hallazgos_asociados = ListField(StringField(choices=[
        'Retracción de la piel',
        'Retracción del pezón',
        'Engrosamiento de la piel',
        'Engrosamiento trabecular',
        'Adenopatias axilares'
    ]), required=False)

    # Lateralidad del hallazgo
    lateralidad = StringField(choices=['Derecho', 'Izquierdo', 'Bilateral'], required=True)

    # BIRADS
    birads = IntField(choices=[0, 1, 2, 3, 4, 5, 6], required=True)
