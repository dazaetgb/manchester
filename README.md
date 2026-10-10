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

## Paso 0: confirma estos datos antes de enviar (importante)

La carta y el CV dicen solo lo que aparece en tu CV base. Revisa estos puntos, porque son los que decidirán la preselección:

1. **¿Qué experimentos de RMN de estado sólido corriste tú mismo, en el espectrómetro?** Los criterios esenciales piden "una amplia gama de experimentos avanzados" y "RMN multinuclear". Si hiciste ¹³C CP-MAS, eco cuadrupolar de ²H, mediciones de T₁, ¹H MAS rápido, ¹⁹F (por ejemplo en el MOF con huéspedes fluorados), ¹⁵N o 2D (HETCOR), **dímelo y lo agrego por nombre**. Es la mejora más importante que se puede hacer.
2. **¿Qué software usaste para simular espectros de ²H?** (EXPRESS, SIMPSON, MXQET, código propio…). Nombrarlo responde al criterio E4.
3. **¿Usaste cálculos de desplazamiento químico (GIPAW/CASTEP o Gaussian NMR) con el grupo de Dračínský?** Si sí, responde a "NMR crystallography" y al criterio D3.
4. **Artículo de Angew. Chem. 2026:** el número de artículo "e26010" se ve incompleto. Revísalo.
5. **Dr Aaron Torres-Huerta:** en tu CV aparece como Universidad Autónoma de Madrid, pero su correo es de la ULB (Bruselas). Confirma su institución actual. En el CV dejé solo el correo.
6. **IMPI:** ¿cuál es tu puesto y desde cuándo? El formulario de historial laboral lo pedirá.
7. **Fecha de inicio posible** y si tienes título y cédula de doctorado en mano (te pueden pedir copias).

## Paso 1: antes de abrir el portal

- [ ] Descarga el PDF *Further Particulars* (`SAE-032399 Research Associate in ssNMR of MoSS FPs`) desde la página de la vacante. Puede traer la *person specification* con criterios que se evalúan "en la solicitud" o "en la entrevista". Pásamelo y ajusto la carta.
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
