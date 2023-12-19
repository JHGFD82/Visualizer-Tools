# main.py

import os
import argparse
from . import (import_midi, clean_data, add_sections, calculate_note_lengths, BPMtoFPS)


def main(file_list, sections=None, action_safe=False):
    """
    This method performs a series of operations on CSV files generated by the MIDICSV program and supplied in the
    file_list parameter. After verification, this method imports them into a DataFrame, cleans the data, adds sections,
    calculates note lengths, generates fake notes, creates a keyboard, adjusts the keyboard side,
    converts BPM to FPS, and saves the DataFrame to a CSV file.

    Parameters:
        file_list (list): A list of file paths containing MIDI files.
        sections (list): A list of sections which may indicate visual separation in video projects.
        action_safe (bool): If true, the script will accommodate for the action safe zone in the video (usually 5% of
            the video's pixel resolution)

    Raises:
        FileNotFoundError: If a file is not found at the specified location.

    Returns:
        None
    """
    for file in file_list:
        if not os.path.isfile(file):
            raise FileNotFoundError(
                f'Failed to open file "{file}". Please ensure that the file exists and that you have entered the '
                f'correct file name.')
    df = import_midi(file_list)
    df, division, notes_per_bar = clean_data(df)
    if sections is None:
        print("No sections provided via command-line arguments.")
        sections = (input("If the music has sections you want to designate, enter their bar numbers here separated by "
                          "spaces, or simply hit enter to continue: ").split())
    df = add_sections(df, sections, division, notes_per_bar)
    df = calculate_note_lengths(df)
    # insert function for adding visual layout columns
    df = BPMtoFPS(df)
    df.to_csv('output.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument("-i", "--input_files", nargs="+", help="List of files to process.")
    parser.add_argument("-s", "--sections", nargs="+", default=None, help="List of sections (if any).")
    parser.add_argument("-a", "--action_safe", action="store_true", help="Boolean to indicate preference for "
                                                                         "accommodating action safe zones in "
                                                                         "video pixel resolution")
    args = parser.parse_args()

    main(args.input_files, args.sections, args.action_safe)
