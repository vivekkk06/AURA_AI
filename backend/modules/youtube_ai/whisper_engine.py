from faster_whisper import WhisperModel
import subprocess
import os
import uuid
import shutil


# ============================================================
# Load Whisper Models (Loaded Once at Startup)
# ============================================================

# Fast lightweight model
fast_model = WhisperModel("tiny", compute_type="int8")

# Higher quality model
full_model = WhisperModel("small", compute_type="int8")


# ============================================================
# Audio Transcription Function
# ============================================================

def transcribe_audio(url: str, seconds: int = 120, mode: str = "fast") -> str:
    """
    Downloads audio from YouTube using yt-dlp
    and transcribes using Faster-Whisper.

    Parameters:
        url (str)      : YouTube URL
        seconds (int)  : Duration to download (optional limit)
        mode (str)     : "fast" → tiny model
                         "full" → small model
    """

    # --------------------------------------------------------
    # Check yt-dlp availability
    # --------------------------------------------------------
    if not shutil.which("yt-dlp"):
        raise Exception("yt-dlp not installed")

    filename = f"audio_{uuid.uuid4().hex}.mp3"

    # --------------------------------------------------------
    # yt-dlp Command
    # --------------------------------------------------------
    cmd = [
        "yt-dlp",
        "--no-playlist",
        "--ignore-errors",
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", filename,
    ]

    # Optional partial download (if seconds provided)
    if seconds:
        cmd.extend(["--download-sections", f"*0-{seconds}"])

    cmd.append(url)

    # --------------------------------------------------------
    # Download Audio
    # --------------------------------------------------------
    try:
        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
            timeout=120
        )
    except subprocess.TimeoutExpired:
        raise Exception("Audio download timeout")
    except subprocess.CalledProcessError:
        raise Exception("Audio download failed")

    if not os.path.exists(filename):
        raise Exception("Audio file not created")

    # --------------------------------------------------------
    # Select Model
    # --------------------------------------------------------
    model = fast_model if mode == "fast" else full_model

    # --------------------------------------------------------
    # Transcribe
    # --------------------------------------------------------
    try:
        segments, _ = model.transcribe(
            filename,
            vad_filter=True
        )

        text = " ".join(segment.text.strip() for segment in segments)

    except Exception:
        try:
            os.remove(filename)
        except Exception:
            pass
        raise Exception("Whisper transcription failed")

    # --------------------------------------------------------
    # Cleanup
    # --------------------------------------------------------
    try:
        os.remove(filename)
    except Exception:
        pass

    return text.strip()
