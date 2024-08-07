import os
from typing import Optional
from midi2audio import FluidSynth
from src.logging import get_logger

logger = get_logger()

def midi_to_wav(
    midi_file: str,
    soundfont_file: str,
    output_dir: Optional[str] = None,
    sample_rate: int = 44100
) -> str:
    """
    Convert a MIDI file to WAV using the specified soundfont.

    Args:
        midi_file (str): Path to the input MIDI file.
        soundfont_file (str): Path to the soundfont file.
        output_dir (Optional[str]): Directory to save the output WAV file. If None, use the current directory.
        sample_rate (int): Sample rate for the output WAV file.

    Returns:
        str: Path to the generated WAV file.
    """
    logger.info(f"Converting MIDI file: {midi_file}")
    logger.info(f"Using soundfont: {soundfont_file}")

    # Validate input files
    if not os.path.exists(midi_file):
        raise FileNotFoundError(f"MIDI file not found: {midi_file}")
    if not os.path.exists(soundfont_file):
        raise FileNotFoundError(f"Soundfont file not found: {soundfont_file}")

    # Create output directory if it doesn't exist
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = os.getcwd()

    # Generate output file name
    midi_basename = os.path.splitext(os.path.basename(midi_file))[0]
    output_file = os.path.join(output_dir, f"{midi_basename}.wav")

    # Convert MIDI to WAV
    logger.debug("Converting MIDI to WAV")
    fs = FluidSynth(sound_font=soundfont_file, sample_rate=sample_rate)
    fs.midi_to_audio(midi_file, output_file)

    logger.info(f"WAV file generated: {output_file}")
    return output_file