"""Build the public skill ZIP using only explicitly selected package files."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "ai-video-director"
ARCHIVE = ROOT / "ai-video-director-download.zip"
PREFIX = "ai-video-director-download"


def build():
    files = [ROOT / name for name in ("README.md", "START-HERE.md", "video-project-brief.md")]
    files.extend(sorted(path for path in SKILL.rglob("*") if path.is_file()))
    if not (SKILL / "SKILL.md").is_file():
        raise FileNotFoundError("The complete ai-video-director source folder is required.")
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError(f"Unexpected external file: {path.name}")
        if path.suffix not in {".md", ".yaml"}:
            raise ValueError(f"Unexpected skill-package file: {path.relative_to(ROOT)}")
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            entry = zipfile.ZipInfo(f"{PREFIX}/{relative}", date_time=(2020, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    with zipfile.ZipFile(ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise ValueError("Archive integrity check failed.")
        for path in files:
            name = f"{PREFIX}/{path.relative_to(ROOT).as_posix()}"
            if archive.read(name) != path.read_bytes():
                raise ValueError(f"Archive content mismatch: {name}")
    checksum = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    (ROOT / "SHA256SUMS.txt").write_bytes(f"{checksum}  {ARCHIVE.name}\n".encode("utf-8"))
    print(f"Built and verified {ARCHIVE.name}: {len(files)} files, {ARCHIVE.stat().st_size} bytes")
    print(f"SHA256 {checksum}")


if __name__ == "__main__":
    build()
