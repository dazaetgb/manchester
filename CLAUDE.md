# Reglas para esta postulación (Manchester ssNMR, SAE-032399)

Responde en español. Los documentos de la postulación van en inglés británico.

## Contenido
- La carta y el CV hablan **solo de lo que Dazaet hizo**. Si algo lo hizo un colaborador, va en voz pasiva o se omite; lo que Dazaet *sabe hacer* pero no hizo en ese trabajo no se le atribuye en ese trabajo.
- Las referencias externas (por ejemplo `ejemplos solucionessolidas/` en Drive, Ye et al., Nat. Commun. 2025) son **solo contexto**. No se citan ni se usan en la solicitud salvo que Dazaet pida extraer algo concreto.
- No afirmar que el ¹³C CP-MAS mide composición: el CP no es cuantitativo, la integral no da el contenido. Lo que la RMN de sólidos aporta en soluciones sólidas es el **ambiente local alrededor del núcleo de interés**.
- Cada dato debe salir de la tesis (Drive: `TesisDoctoral-DGB-v3.1.pdf`), de los papers (Drive: `manchester/papers/`) o de algo que Dazaet confirmó. Si la tesis y Dazaet difieren, manda lo que dice Dazaet.

## Papel de Dazaet por trabajo (confirmado el 10/10/2026)
- General: Dazaet hizo el análisis de RMN (disolución y estado sólido) de los 14 papers, y sabe hacer todo, desde la adquisición hasta la interpretación y el modelado. Conviene decirlo explícitamente.
- DFT periódico: Dazaet usa **CP2K** (y Gaussian 16 para cálculos moleculares). **No ha usado CASTEP**; los cálculos en CASTEP de sus papers los hicieron colaboradores, así que van en pasiva o se omiten. Puede calcular tensores EFG (CP2K tiene el módulo `qs_electric_field_gradient`).
- ACS Mater. Lett. 2026 (MOF rotor + fotointerruptor): síntesis, PXRD, construcción de los modelos periódicos, ¹³C CP-MAS, ²H, ¹⁹F MAS y ¹⁹F cuantitativo. El ajuste de ²H con Spinach y tensores EFG de CASTEP lo hizo Jan Blahut (Dazaet sabe usar Spinach).
- Mater. Chem. Front. 2026 (solvato de tolueno): Dazaet preparó el tolueno-d₈ y simuló el ²H en NMR WebLab. Rango de ²H según el artículo: 178 (−95 °C) a 338 K; la parte de baja temperatura y los cálculos GIPAW los hizo Martin Dračínský.
- Angew. Chem. Int. Ed. 2026, 65 (18), e26010: no adquirió los espectros; interpretó y modeló el ²H.
- Chem. Sci. 2020 (Torres-Huerta et al.): modelo de ²H.
- Chem. Mater. 2025 (Belmonte-Vázquez et al.): interpretación del ¹³C.
- Equipo: Bruker 500 MHz (TopSpin), sonda ¹H/X. Adquirió ¹³C CP-MAS, ¹⁹F MAS, ³¹P, ²H a temperatura variable y algo de ¹⁵N CP-MAS. Analizó (no adquirió) ¹³C T₁ y relaxometría de ¹H y ¹⁹F. Sin DNP. No mencionar tiempos de contacto variables ni sintonización de sonda.

## Voz de la carta
Sin construcciones "no es X, es Y", sin guiones largos, sin tricolons ni cierres grandilocuentes, sin autoelogio abstracto, cada afirmación verificable.

## Formato
- CV: CV maestro (`00_fuentes/`) con cambios mínimos (`90_tools/build_cv_from_base.py`). No cambiar su estructura.
- Fuente Aptos; el PDF final lo exporta Dazaet desde Word. Carta + CV en un solo PDF < 1 MB.
- **La versión de trabajo vive en Google Drive**, carpeta `manchester` (id 15-ZzMwOYVq1SrVSsqGFMX2CJkCCK_aBd). Dazaet edita ahí; los cambios que pida se aplican en el documento de Drive (y se reflejan en el repo).
- Commit y push a `main`.
