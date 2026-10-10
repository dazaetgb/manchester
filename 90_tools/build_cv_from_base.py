"""Minimal, run-level edits to the master CV (00_fuentes/CV_base_...docx). Layout untouched."""
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "00_fuentes" / "CV_base_Dazaet_Galicia-Badillo.docx"

NMR_OLD = "Solid-state NMR: variable-temperature ²H and ¹³C, spectral simulation and relaxation analysis."
NMR_NEW = ("Solid-state NMR (Bruker 500 MHz, double-resonance ¹H/X MAS probe): ¹³C CP-MAS with variable "
           "contact time, ¹⁹F MAS, variable-temperature ²H and ¹⁵N CP-MAS; probe tuning and matching; ²H "
           "lineshape simulation; analysis of ¹³C T₁ and solid-state ¹H and ¹⁹F relaxometry data.")

# (paragraph text marker, old run text, new run text)
EDITS = [
    ("dynamics across multiple length scales", "-", ", "),
    ("dynamics across multiple length scales", "rom molecular-level", "from molecular-level"),
    ("I bring a strong experimental toolkit", "solid-state NMR (variable-temperature ²H and ¹³C)",
     "multinuclear solid-state NMR (¹³C, ¹⁹F, ²H, ¹⁵N)"),
    ("Experimental", NMR_OLD, NMR_NEW),
    ("Experimental", "NMR processing: MestreNova.", "NMR processing and simulation: TopSpin, MestreNova, NMR WebLab."),
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
