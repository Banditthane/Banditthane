
from datetime import datetime, timezone
from pathlib import Path

readme = Path("README.md")

start = "<!-- PROFILE_LAST_UPDATED_START -->"
end = "<!-- PROFILE_LAST_UPDATED_END -->"

content = readme.read_text(encoding="utf-8")

if start not in content or end not in content:
    raise SystemExit("README timestamp markers are missing.")

before, remainder = content.split(start, 1)
_, after = remainder.split(end, 1)

timestamp = datetime.now(timezone.utc).strftime(
    "%Y-%m-%d %H:%M UTC"
)

updated = f"{before}{start}{timestamp}{end}{after}"

readme.write_text(updated, encoding="utf-8")

print(f"README updated: {timestamp}")
