from typing import Dict, List, Optional, Any

class Paciente:
    CAMPOS = {
        'nodulo': {
            'choices': ['No', 'Si'],
            'required': True
        },
        'morfologia': {
            'choices': ['Ovalado', 'Redondo', 'Irregular', 'N.A'],
            'required': True
        },
        'margenes': {
            'choices': [
                'Circunscritos',
                'Microlobulados',
                'Indistintos o mal definidos',
                'Obscurecidos',
                'Espiculados', 'N.A'
            ],
            'required': True
        },
        'densidad': {
            'choices': ['Densidad Grasa', 'Baja Densidad (Hipodenso)', 'Igual Densidad (Isodenso)', 'Alta Densidad (Hiperdenso)', 'N.A'],
            'required': True
        },
        'microcalcificaciones': {
            'choices': ['No', 'Si'],
            'required': True
        },
        'calcificaciones benignas': {
            'choices': [
                'Cutaneas',
                'Vasculares',
                'Gruesas o Pop Corn',
                'Leño o Vara',
                'Redondas o puntiformes',
                'Anulares',
                'Distroficas',
                'Leche de Calcio',
                'Suturas', 'N.A'
            ],
            'required': True
        },
        'calcificaciones sospechosas': {
            'choices': [
                'Gruesas heterogeneas',
                'Amorfas',
                'Finas pleomorficas',
                'Lineas fianas o lineales ramificadas', 'N.A'
            ],
            'required': True
        },
        'distribucion calcificaciones': {
            'choices': [
                'Difusas',
                'Regionales',
                'Agrupadas (cumulo)',
                'Segmentaria',
                'Lineal', 'N.A'
            ],
            'required': True
        },
        'asimetrias': {
            'choices': ['Si', 'No'],
            'required': True
        },
        'tipo asimetria': {
            'choices': [
                'Asimetria',
                'Asimetria global',
                'Asimetria focal',
                'Asimetria focal evolutiva', 'N.A'
            ],
            'required': True
        },
        'hallazgos asociados': {
            'choices': [
                'Retracción de la piel',
                'Retracción del pezón',
                'Engrosamiento de la piel',
                'Engrosamiento trabecular',
                'Adenopatias axilares', 'N.A'
            ],
            'required': True
        },
        'lateralidad': {
            'choices': ['Derecho', 'Izquierdo', 'Bilateral', 'N.A'],
            'required': True
        },
        'birads': {
            'choices': ["0", "1", "2", "3", "4A", "4B", "4C", "5", "6", "N.A"],
            'required': True
        }
    }

    def __init__(self):
        self.datos: Dict[str, Any] = {}

    def set_campo(self, campo: str, valor: str) -> None:
        if campo not in self.CAMPOS:
            raise ValueError(f"Campo '{campo}' no válido")
        
        if valor not in self.CAMPOS[campo]['choices']:
            raise ValueError(f"Valor '{valor}' no válido para el campo '{campo}'")
        
        self.datos[campo] = valor

    def get_campo(self, campo: str) -> Optional[str]:
        return self.datos.get(campo)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el objeto Paciente en un diccionario serializable.
        """
        return {
            campo: valor for campo, valor in self.datos.items()
        }
