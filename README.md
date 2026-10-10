# Manchester: Research Associate in Solid-State NMR Spectroscopy

**Ref. SAE-032399** · Department of Chemical Engineering · Programa EPSRC *Molecular Solid Solutions (MoSS)* entre Durham, Leeds y Manchester
**Cierre: 31/10/2026 a medianoche, hora de Reino Unido (alrededor de las 18:00 h del 31/10 en Ciudad de México; el Reino Unido ya estará en horario de invierno, GMT).** Envíalo antes del **24/10**.
Entrevistas: finales de noviembre o principios de diciembre.

## Contenido

| Carpeta | Qué contiene |
|---|---|
| `00_vacante/` | La vacante completa, el análisis criterio por criterio y el ángulo de venta |
| `00_fuentes/` | Tu CV base y la carta de UCLA (solo como referencia) |
| `01_documentos/` | **`Galicia-Badillo_Dazaet_SAE-032399_CoverLetter_CV.pdf`**, el archivo que se sube (71 KB). También van la carta y el CV por separado, en .docx y .pdf |
| `02_formularios/` | Respuestas sugeridas para cada formulario de Jobtrain |
| `90_tools/` | Script que regenera todo (`python3 90_tools/build_manchester_ssnmr.py`) |

## Paso 0: estado de las confirmaciones

Ya resuelto (10/10/2026): RMN en Bruker 500 MHz con sonda ¹H/X; ¹³C CP-MAS con tiempo de contacto variable; ¹⁹F; ²H a temperatura variable; ¹⁵N limitado; NMR WebLab; análisis de ¹³C T₁ y de relaxometría de ¹H/¹⁹F; Aaron en la UAM; Further Particulars leídos (se agregaron síntesis, seguridad, supervisión y DNP Facility).

Resuelto el 10/10: ¹⁹F MAS; ¹³C T₁ y relaxometría de ¹H/¹⁹F en estado sólido (analizados, no adquiridos); IMPI como Industrial Property Expert con contrato hasta enero de 2027; inicio inmediato, de preferencia en enero de 2027.

**CV:** es tu CV original con 5 cambios mínimos (ver `90_tools/build_cv_from_base.py`). Usa la fuente Aptos, que no existe en este entorno, así que **el PDF debes exportarlo tú desde Word** (Archivo > Guardar como > PDF). El PDF generado aquí solo sirve de vista previa.

Pendiente:
1. **Tesis doctoral**, para reescribir la carta con lo que hiciste exactamente.
2. Mes de inicio en el IMPI y periodo de aviso.
3. Angew. Chem. 2026: confirma el número de artículo ("e26010").

## Paso 1: antes de abrir el portal

- [x] Further Particulars leídos (copia en `00_vacante/`).
- [ ] (Opcional, pero recomendable en Reino Unido) Escribe un correo breve a **Dr Daniel Lee** (daniel.lee@manchester.ac.uk) con una pregunta concreta sobre el puesto. Hay un borrador en `02_formularios/correo_daniel_lee.md`.
- [ ] Avisa a tus dos referencias que Manchester podría contactarlas en noviembre.
- [ ] Ten a mano: pasaporte, fechas exactas de grados, títulos y la fecha de examen doctoral.

## Paso 2: el portal (Jobtrain)

Botón **Apply for job**, crea una cuenta y luego llena las secciones en orden. En `02_formularios/respuestas_formularios.md` está el texto sugerido para cada una.

1. Personal details
2. Right to work in the UK: vas a necesitar **patrocinio de visa Skilled Worker**. La universidad sí patrocina puestos de investigación; contéstalo con honestidad, no te descalifica.
3. Education / qualifications
4. Employment history
5. Referees: 2 o 3
6. Supporting documents: sube **solo** `Galicia-Badillo_Dazaet_SAE-032399_CoverLetter_CV.pdf` (carta + CV en un archivo, menor de 1 MB, como pide la vacante)
7. Equality & diversity monitoring: es opcional y anónimo, y no se usa en la preselección
8. Declaration y Submit, y guarda el correo de confirmación

Jobtrain guarda borradores, así que puedes llenarlo en varias sesiones.

## Paso 3: después de enviar

- Prepara la entrevista: una plática de 10 a 15 minutos sobre tu trabajo con ²H NMR y difracción, y una diapositiva sobre cómo aplicarías la RMN a soluciones sólidas moleculares (desorden local, distribución de componentes, ¹⁹F/¹H como sondas, DNP para abundancia natural de ¹⁵N/¹⁷O).
- Lee 2 o 3 artículos recientes de Daniel Lee sobre DNP y RMN de sólidos orgánicos.

## Ángulo de venta (resumen)

Tu argumento más fuerte es el criterio deseable D3: correlacionas la dinámica medida por RMN de ²H/¹³C con estructuras de difracción a temperatura variable, en colaboración con el grupo de NMR del IOCB Praga. Le sigue el cómputo (DFT, DFT periódico, MD en HPC). La brecha honesta está en la cobertura multinuclear y en DNP. La carta la reconoce en una frase y la presenta como lo que vienes a aprender, para que el comité no la descubra por su cuenta.

## Chequeos

```
Voz:
[OK] Cero construcciones tesis/antítesis
[OK] Cero guiones largos en el texto
[OK] Sin frases de cierre grandilocuentes ni autoelogio abstracto
[OK] Cada afirmación sale de tu CV base o de la carta de UCLA

ATS:
[OK] Encabezados estándar (Research Experience, Education, Technical Skills, Publications)
[OK] Texto seleccionable, sin iconos; contacto en el cuerpo del documento
[OK] Palabras clave: solid-state NMR, multinuclear, variable-temperature, lineshape simulation,
     relaxation, DFT, molecular dynamics, SCXRD/PXRD, DSC/TGA, molecular crystals, collaboration
[OK] Sin pie de página "adaptado para…"
[OK] Archivo combinado de 71 KB (límite: 1 MB)
```

Cambios respecto a tu CV base: ortografía británica; reordenado para poner la RMN al frente; "Material Chemistry Frontiers" corregido a *Materials*; corregido "rom" por "from"; referencias en formato abreviado de ACS con tu nombre en negritas; sección de experiencia de investigación con bullets que responden a los criterios.
