function leerSolicitud() {
  const hoja = SpreadsheetApp
    .getActiveSpreadsheet()
    .getActiveSheet();

  if (!hoja) {
    throw new Error("No se encontró la hoja de respuestas.");
  }

  const datos = hoja.getDataRange().getValues();

  if (datos.length <= 1) {
    return {
      disponible: false,
      mensaje: "No existen solicitudes registradas."
    };
  }

  // Índices de la estructura definida:
  // 0: Marca temporal
  // 1: Nombre
  // 2: Tipo de consulta
  // 3: Consulta
  // 4: Correo electrónico
  // 5: Estado
  // 6: Respuesta IA
  // 7: Fecha de procesamiento

  for (let indice = 1; indice < datos.length; indice++) {
    const fila = datos[indice];
    const estado = String(fila[5] || "").trim().toUpperCase();

    if (estado === "PENDIENTE") {
      const numeroFila = indice + 1;

      // Marcar inmediatamente la solicitud como en procesamiento
      hoja.getRange(numeroFila, 6).setValue("PROCESANDO");

      return {
        disponible: true,
        fila: numeroFila,
        nombre: String(fila[1] || "").trim(),
        tipo: String(fila[2] || "").trim(),
        consulta: String(fila[3] || "").trim(),
        correo: String(fila[4] || "").trim()
      };
    }
  }

  return {
    disponible: false,
    mensaje: "No existen solicitudes pendientes."
  };
}


function doGet() {
  try {
    const solicitud = leerSolicitud();

    return ContentService
      .createTextOutput(JSON.stringify(solicitud))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(
        JSON.stringify({
          disponible: false,
          mensaje: error.message
        })
      )
      .setMimeType(ContentService.MimeType.JSON);
  }
}


function doPost(e) {
  let hoja = null;
  let fila = null;

  try {
    const contenido = JSON.parse(
      e.postData.contents || "{}"
    );

    fila = Number(contenido.fila);

    const respuesta = String(
      contenido.respuesta || ""
    ).trim();

    if (!Number.isInteger(fila) || fila < 2) {
      throw new Error(
        "El número de fila no es válido."
      );
    }

    if (!respuesta) {
      throw new Error(
        "La respuesta recibida está vacía."
      );
    }

    hoja = SpreadsheetApp
      .getActiveSpreadsheet()
      .getActiveSheet();

    if (!hoja) {
      throw new Error(
        "No se encontró la hoja de respuestas."
      );
    }

    const nombre = String(
      hoja.getRange(fila, 2).getValue() || ""
    ).trim();

    const tipo = String(
      hoja.getRange(fila, 3).getValue() || ""
    ).trim();

    const correo = String(
      hoja.getRange(fila, 5).getValue() || ""
    ).trim();

    // Registrar la respuesta generada
    hoja.getRange(fila, 7).setValue(respuesta);
    hoja.getRange(fila, 8).setValue(new Date());

    // Enviar la respuesta al estudiante
    enviarCorreo(
      correo,
      nombre,
      tipo,
      respuesta
    );

    // Finalizar la solicitud
    hoja.getRange(fila, 6).setValue("ENVIADA");

    return respuestaJson_({
      correcto: true,
      mensaje: "Respuesta registrada y enviada correctamente."
    });

  } catch (error) {

    if (
      hoja &&
      fila &&
      Number.isInteger(fila) &&
      fila >= 2
    ) {
      hoja.getRange(fila, 6).setValue("ERROR");
    }

    return respuestaJson_({
      correcto: false,
      error: error.message
    });
  }
}


function respuestaJson_(contenido) {
  return ContentService
    .createTextOutput(JSON.stringify(contenido))
    .setMimeType(ContentService.MimeType.JSON);
}


function enviarCorreo(correo, nombre, tipo, respuesta) {
  if (!correo) {
    throw new Error(
      "La solicitud no contiene un correo electrónico."
    );
  }

  if (!respuesta) {
    throw new Error(
      "No existe una respuesta para enviar."
    );
  }

  const nombreUsuario = nombre || "estudiante";
  const categoria = tipo || "Consulta académica";

  const asunto =
    "Respuesta a tu consulta académica: " + categoria;

  const cuerpo =
    "Hola " + nombreUsuario + ":\n\n" +
    "Hemos procesado tu consulta mediante el " +
    "Servicio Inteligente Académico.\n\n" +
    "Respuesta:\n\n" +
    respuesta + "\n\n" +
    "Esta respuesta fue generada automáticamente. " +
    "Si necesitas una revisión adicional, comunícate " +
    "con el responsable académico correspondiente.\n\n" +
    "Saludos.";

  GmailApp.sendEmail(
    correo,
    asunto,
    cuerpo,
    {
      name: "Servicio Inteligente Académico"
    }
  );
}
