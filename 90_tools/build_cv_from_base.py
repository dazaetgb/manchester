"""Minimal, run-level edits to the master CV (00_fuentes/CV_base_...docx). Layout untouched."""
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "00_fuentes" / "CV_base_Dazaet_Galicia-Badillo.docx"

NMR_OLD = "Solid-state NMR: variable-temperature ²H and ¹³C, spectral simulation and relaxation analysis."
NMR_NEW = ("Solid-state NMR (Bruker 500 MHz, double-resonance ¹H/X MAS probe): ¹³C CP-MAS, ¹⁹F MAS, ³¹P, "
           "variable-temperature ²H and ¹⁵N CP-MAS; ²H lineshape simulation; DFT calculation of NMR parameters "
           "(CASTEP); analysis of ¹³C T₁ and solid-state ¹H and ¹⁹F relaxometry data.")

ABOUT_RUN2 = (" on the design and synthesis of organic crystals and metal-organic frameworks exhibiting dynamics "
              "from the molecular level to the macroscopic level")
ABOUT_RUN4 = ("including rotational motion, photoisomerization, crystal flexibility, salient mechanical responses, "
              "and single-crystal-to-single-crystal phase transitions.")

# (paragraph text marker, old run text, new run text)
EDITS = [
    ("dynamics across multiple length scales",
     " on the design and synthesis of organic and metal-organic framework materials exhibiting dynamics "
     "across multiple length scales", ABOUT_RUN2),
    ("from the molecular level to the macroscopic level", "-", ", "),
    ("from the molecular level to the macroscopic level", "rom molecular-level rotational motion and "
     "photoisomerization to macroscopic phenomena such as crystal flexibility, salient mechanical responses, "
     "and single-crystal-to-single-crystal phase transitions.", ABOUT_RUN4),
    ("I bring a strong experimental toolkit", "solid-state NMR (variable-temperature ²H and ¹³C)",
     "multinuclear solid-state NMR (¹³C, ¹⁹F, ³¹P, ²H, ¹⁵N)"),
    ("Experimental", NMR_OLD, NMR_NEW),
    ("Experimental", "NMR processing: MestreNova.", "NMR processing and simulation: TopSpin, MestreNova, NMR WebLab, CASTEP."),
    ("Dissecting Molecular and Macroscopic", "Material Chemistry Frontiers", "Materials Chemistry Frontiers"),
]


def build_cv(out_path):
    doc = Document(BASE)
    for marker, old, new in EDITS:
        p = next(p for p in doc.paragraphs if marker in p.text)
        run = next((r for r in p.runs if r.text == old), None) or next((r for r in p.runs if old in r.text), None)
        if run is None:
            raise ValueError(f"not found: {old!r}")
        run.text = run.text.replace(old, new, 1)
    doc.save(out_path)
    return out_path
