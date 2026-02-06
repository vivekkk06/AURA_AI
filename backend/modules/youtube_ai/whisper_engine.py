from faster_whisper import WhisperModel
import subprocess, os, uuid, shutil

fast_model = WhisperModel("tiny", compute_type="int8")
full_model = WhisperModel("small", compute_type="int8")


def transcribe_audio(url: str, seconds=120, mode="fast"):

    if not shutil.which("yt-dlp"):
        raise Exception("yt-dlp is not installed")

    filename = f"audio_{uuid.uuid4().hex}.mp3"

    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--download-sections", f"*0-{seconds}",
        "-o", filename,
        url
    ]

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        raise Exception("Audio download failed (yt-dlp error)")

    model = fast_model if mode == "fast" else full_model
    segments, _ = model.transcribe(filename, vad_filter=True)

    text = " ".join(seg.text for seg in segments)

    try:
        os.remove(filename)
    except:
        pass

    return text.strip()
