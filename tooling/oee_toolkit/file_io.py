"""Shared atomic JSON output for publisher tooling and offline consumers.

This module performs only an explicit local write requested by the caller.
It contains no Git, network, release acquisition, course parsing or
publication logic. Failed validation must occur before invoking this writer.
"""
from __future__ import annotations

import os
from pathlib import Path
import sys
import tempfile

from .source import SourceError


def atomic_write(target: str, data: bytes) -> None:
    if target == "-":
        sys.stdout.buffer.write(data)
        return
    file = Path(target).expanduser()
    if not file.parent.is_dir():
        raise SourceError("missing_input", "output parent directory does not exist")
    if file.is_symlink():
        raise SourceError("unsafe_reference", "refusing to replace a symlink output")
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=file.parent, prefix=f".{file.name}.", suffix=".tmp", delete=False
        ) as temp:
            temp_path = Path(temp.name)
            temp.write(data)
            temp.flush()
            os.fsync(temp.fileno())
        os.replace(temp_path, file)
    except OSError as exc:
        raise SourceError("tool_error", f"atomic export write failed: {type(exc).__name__}") from exc
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
