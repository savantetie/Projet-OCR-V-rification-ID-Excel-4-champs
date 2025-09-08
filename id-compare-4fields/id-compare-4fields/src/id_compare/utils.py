import re
import unicodedata
from datetime import datetime

def normalize_name(s: str | None) -> str | None:
    if s is None:
        return None
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", s).strip().upper()

def normalize_dob(s: str | None) -> str | None:
    if not s:
        return None
    # Try several common formats, return ISO YYYY-MM-DD
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.strptime(s.strip(), fmt).date().isoformat()
        except ValueError:
            pass
    return None

ID_RE = re.compile(r"(N[°o]?[:\s-]*)?(?P<ID>[A-Z0-9]{6,})", re.I)

def parse_id(text: str) -> str | None:
    m = ID_RE.search(text or "")
    return m.group("ID").upper() if m else None
