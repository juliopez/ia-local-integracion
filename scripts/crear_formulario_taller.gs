/**
 * SESIÓN 3 — ejecutar UNA vez la función crearFormularioTaller().
 * Crea Google Forms -> vincula Google Sheets -> añade estado de procesamiento.
 *
 * Estructura compatible con scripts/Code.gs:
 * A Marca temporal | B Nombre | C Tipo de consulta | D Consulta |
 * E Correo electrónico | F Estado | G Respuesta IA | H Fecha de procesamiento
 *
 * IMPORTANTE: cree un proyecto NUEVO en https://script.google.com.
 * No pegue este bootstrap en el Code.gs de producción y no despliegue aquí doGet/doPost.
 */
function crearFormularioTaller() {
  const propiedades = PropertiesService.getUserProperties();
  const idAnterior = propiedades.getProperty('FORMULARIO_TALLER_ID');
  const hojaAnterior = propiedades.getProperty('SHEET_TALLER_ID');

  if (idAnterior && hojaAnterior) {
    Logger.log('Ya existe una instalación asociada a este proyecto.');
    Logger.log('Formulario: https://docs.google.com/forms/d/' + idAnterior + '/edit');
    Logger.log('Hoja de cálculo: https://docs.google.com/spreadsheets/d/' + hojaAnterior + '/edit');
    return;
  }

  const formulario = FormApp.create('Solicitudes al Asistente Académico');
  formulario.setDescription('Formulario de prueba del taller de IA local. No ingrese información real ni sensible.');
  formulario.setCollectEmail(false); // Se usa una pregunta explícita de correo.
  formulario.setLimitOneResponsePerUser(false);

  formulario.addTextItem()
    .setTitle('Nombre')
    .setRequired(true);

  formulario.addListItem()
    .setTitle('Tipo de consulta')
    .setChoiceValues(['Evaluaciones', 'Asignaturas', 'Matrícula', 'Otro'])
    .setRequired(true);

  formulario.addParagraphTextItem()
    .setTitle('Consulta')
    .setRequired(true);

  const correo = formulario.addTextItem()
    .setTitle('Correo electrónico')
    .setRequired(true);
  const validacionCorreo = FormApp.createTextValidation()
    .requireTextIsEmail()
    .setHelpText('Ingrese un correo electrónico válido para recibir la respuesta.')
    .build();
  correo.setValidation(validacionCorreo);

  const libro = SpreadsheetApp.create('IA Local — Respuestas del Asistente Académico');
  formulario.setDestination(FormApp.DestinationType.SPREADSHEET, libro.getId());

  propiedades.setProperty('FORMULARIO_TALLER_ID', formulario.getId());
  propiedades.setProperty('SHEET_TALLER_ID', libro.getId());

  // Trigger instalado en el LIBRO, no en Forms: e.range incluye la fila nueva.
  ScriptApp.newTrigger('registrarSolicitudTaller')
    .forSpreadsheet(libro)
    .onFormSubmit()
    .create();

  Logger.log('Formulario (edición): ' + formulario.getEditUrl());
  Logger.log('Formulario (para responder): ' + formulario.getPublishedUrl());
  Logger.log('Hoja de cálculo: ' + libro.getUrl());
  Logger.log('SIGUIENTE: envíe una respuesta ficticia. El trigger escribirá PENDIENTE.');
  Logger.log('Compruebe que las columnas A:E sean exactamente las previstas.');
}

/**
 * Se ejecuta cuando Sheets recibe una nueva respuesta.
 * Nunca modifica las cinco columnas originales de Forms.
 */
function registrarSolicitudTaller(e) {
  if (!e || !e.range) {
    throw new Error('Esta función requiere un envío real de Forms; no la ejecute a mano.');
  }
  const hoja = e.range.getSheet();
  const fila = e.range.getRow();
  if (fila <= 1) return;
  const encabezados = ['Estado', 'Respuesta IA', 'Fecha de procesamiento'];
  // Preservar los títulos escritos en F:H; no alterar las respuestas.
  const valores = hoja.getRange(1, 6, 1, 3).getValues()[0];
  for (let i = 0; i < encabezados.length; i++) {
    if (!valores[i]) hoja.getRange(1, 6 + i).setValue(encabezados[i]);
  }
  hoja.getRange(fila, 6).setValue('PENDIENTE');
}

/**
 * Comprobación opcional, después del primer envío real.
 * Muestra los encabezados y estado; no modifica respuestas.
 */
function verificarFormularioTaller() {
  const id = PropertiesService.getUserProperties().getProperty('SHEET_TALLER_ID');
  if (!id) throw new Error('Ejecute primero crearFormularioTaller().');
  const libro = SpreadsheetApp.openById(id);
  const hoja = libro.getSheets().find(h =>
    h.getLastRow() > 1 && h.getRange(1, 1).getValue() === 'Marca temporal'
  );
  if (!hoja) {
    Logger.log('Todavía no aparece una respuesta real de Forms; envíe una solicitud ficticia.');
    return;
  }
  Logger.log('Hoja de respuestas: ' + hoja.getName());
  Logger.log('Columnas A:H: ' + hoja.getRange(1, 1, 1, 8).getDisplayValues()[0].join(' | '));
  Logger.log('Último estado: ' + hoja.getRange(hoja.getLastRow(), 6).getDisplayValue());
}
