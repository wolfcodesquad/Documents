from word import generate_doc

data = {
    'NUMERODEOFICIO': '11020',
    'EXPEDIENTE': 'ETG4-1',
    'NOMBREALUMNO': 'RAÚL ESQUIVEL ROSADO',
    'MATRICULA': 'E17080338',
    'CARRERA': 'ING. ELECTRÓNICA',
    'INGRESOENSEMESTRE': '8VO SEMESTRE',
    'DIA': '23',
    'MES': 'NOVIEMBRE',
    'DIA2': '24',
    'MES2': 'DICIEMBRE',
    'AÑO': '2020',
    'DIA3': '12',
    'MES3': 'ENERO',
    'DIA4': '30',
    'MES4': 'OCTUBRE',
    'DIAS': "20 DIAS",
    'MESEXPEDICION': 'OCTUBRE',
    'TITULO': 'MSC.',
    'NOMBREJEFEDEPTO': 'NORA LETICIA CUEVAS CUEVAS'}

generate_doc("templates/CONSTANCIA.docx", data, 'outputs/CONST-salida3.docx')
