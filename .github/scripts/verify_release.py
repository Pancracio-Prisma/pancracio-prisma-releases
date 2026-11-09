"""Standalone verification for the public Prisma distribution repository."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import re
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


def verify(directory: Path, tag: str) -> None:
    match = re.fullmatch(r"prisma-(macos|windows)-v([0-9]+\.[0-9]+\.[0-9]+)", tag)
    if not match or directory.is_symlink() or not directory.is_dir():
        raise ValueError("invalid release tag or directory")
    if {path.name for path in directory.iterdir()} != {
            "release.json", "publisher-public-key.raw", "wheels"}:
        raise ValueError("unexpected release files")
    key_path = directory / "publisher-public-key.raw"
    manifest = directory / "release.json"
    wheels = directory / "wheels"
    if (key_path.is_symlink() or key_path.stat().st_size != 32
            or manifest.is_symlink() or manifest.stat().st_size > 64 * 1024
            or wheels.is_symlink() or not wheels.is_dir()):
        raise ValueError("unsafe release files")
    envelope = json.loads(manifest.read_text(encoding="utf-8"))
    payload = envelope["payload"]
    expected = payload["wheels"]
    if (payload["schema_version"] != 1 or payload["version"] != match.group(2)
            or not isinstance(expected, dict) or not expected
            or len(expected) > 100 or {path.name for path in wheels.iterdir()} != set(expected)):
        raise ValueError("release manifest differs from files or tag")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                           ensure_ascii=False).encode("utf-8")
    Ed25519PublicKey.from_public_bytes(key_path.read_bytes()).verify(
        base64.b64decode(envelope["signature"], validate=True), canonical)
    for name, digest in expected.items():
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]{5,199}\.whl", name):
            raise ValueError("invalid wheel name")
        path = wheels / name
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 100 * 1024 * 1024:
            raise ValueError("unsafe wheel")
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("wheel hash differs")
    if not any(name.startswith(f"pancracio_prisma_user-{match.group(2)}-") for name in expected):
        raise ValueError("matching user wheel is unavailable")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: public_release_verify.py RELEASE_DIR TAG")
    verify(Path(sys.argv[1]), sys.argv[2])
