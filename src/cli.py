import argparse
import sys
from typing import List

from src.core import midi_to_wav
from src.logging import get_logger

logger = get_logger()

def parse_args(args: List[str]) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args (List[str]): List of command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Convert MIDI files to WAV using a specified soundfont.")
    parser.add_argument("midi_file", help="Path to the input MIDI file")
    parser.add_argument("--soundfont", required=True, help="Path to the soundfont file")
    parser.add_argument("-o", "--output", help="Directory to save the output WAV file")
    parser.add_argument("--sample-rate", type=int, default=44100, help="Sample rate for the output WAV file")
    return parser.parse_args(args)

def main() -> None:
    """
    Main entry point for the CLI application.
    """
    args = parse_args(sys.argv[1:])

    try:
        output_file = midi_to_wav(args.midi_file, args.soundfont, args.output, args.sample_rate)
        logger.info(f"Conversion completed successfully. Output file: {output_file}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()