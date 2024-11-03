
class Pacient(Document):
    # Campos básicos
    nodulo = StringField(choices=['No', 'Si'], required=True) 
    morfologia = StringField(choices=['Ovalado', 'Redondo', 'Irregular'], required=True)
    margenes = StringField(choices=[
        'Circunscritos',
        'Microlobulados',
        'Indistintos o mal definidos',
        'Obscurecidos',
        'Espiculados'
    ], required=True)

    # Densidad del nódulo
    densidad = StringField(choices=['Densidad Grasa', 'Baja Densidad (Hipodenso)', 'Igual Densidad (Isodenso)', 'Alta Densidad (Hiperdenso)'], required=True)

    # Presencia de microcalcificaciones
    microcalcificaciones = StringField(choices=['No', 'Si'], required=True) 

    # Calcificaciones típicamente benignas
    calcificaciones_benignas = StringField(choices=[
        'Cutaneas',
        'Vasculares',
        'Gruesas o Pop Corn',
        'Leño o Vara',
        'Redondas o puntiformes',
        'Anulares',
        'Distroficas',
        'Leche de Calcio',
        'Suturas'
    ], required=False)

    # Calcificaciones morfología sospechosa
    calcificaciones_sospechosas = StringField(choices=[
        'Gruesas heterogeneas',
        'Amorfas',
        'Finas pleomorficas',
        'Lineas fianas o lineales ramificadas'
    ], required=False)

    # Distribución de las calcificaciones
    distribucion_calcificaciones = StringField(choices=[
        'Difusas',
        'Regionales',
        'Agrupadas (cumulo)',
        'Segmentaria',
        'Lineal'
    ], required=False)

    # Presencia de asimetrias
    asimetrias = StringField(choices=['No', 'Si'], required=True)  

    # Tipo de asimetría
    tipo_asimetria = StringField(choices=[
        'Asimetria',
        'Asimetria global',
        'Asimetria focal',
        'Asimetria focal evolutiva'
    ], required=False)

    # Hallazgos asociados
    hallazgos_asociados = StringField(choices=[
        'Retracción de la piel',
        'Retracción del pezón',
        'Engrosamiento de la piel',
        'Engrosamiento trabecular',
        'Adenopatias axilares'
    ], required=False)

    # Lateralidad del hallazgo
    lateralidad = StringField(choices=['Derecho', 'Izquierdo', 'Bilateral'], required=True)

    # BIRADS
    birads = StringField(choices=["0", "1", "2", "3", "4A", "4B", "4C", "5", "6"], required=True)

