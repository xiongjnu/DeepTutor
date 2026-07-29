"""FFmpeg availability check utility."""

import shutil


def check_ffmpeg_available() -> bool:
    """Return True if ffmpeg is installed and accessible."""
    return shutil.which("ffmpeg") is not None
