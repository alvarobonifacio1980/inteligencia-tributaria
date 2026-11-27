"""Valida o snapshot editorial canônico sem reverter ampliações já revisadas."""
from pathlib import Path
import json
from coletar import validar
p=Path(__file__).resolve().parents[1]/'data/base_revisada.json'
validar(json.loads(p.read_text()))
print('Snapshot preservado e validado. Para coletar, execute coletar.py e ampliar_fontes.py.')
