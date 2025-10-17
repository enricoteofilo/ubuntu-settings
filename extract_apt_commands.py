#!/usr/bin/env python3
"""
Extract apt commands from history.log file.

This script reads an apt history.log file and extracts only the command lines,
writing them to a text file with one command per line.
"""

import sys
import os


def extract_apt_commands(input_file, output_file):
    """
    Extract apt commands from history.log and write to output file.
    
    Args:
        input_file: Path to the history.log file
        output_file: Path to the output .txt file
    """
    commands = []
    
    try:
        with open(input_file, 'r') as f:
            for line in f:
                # Look for lines starting with "Commandline:"
                if line.startswith('Commandline:'):
                    # Extract the command part (everything after "Commandline: ")
                    command = line.split('Commandline:', 1)[1].strip()
                    if command:
                        commands.append(command)
        
        # Write commands to output file
        with open(output_file, 'w') as f:
            for command in commands:
                f.write(command + '\n')
        
        print(f"Successfully extracted {len(commands)} commands from {input_file}")
        print(f"Output written to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python3 extract_apt_commands.py <history.log> [output.txt]")
        print("\nExtracts apt commands from history.log file")
        print("\nArguments:")
        print("  history.log   Path to the apt history.log file")
        print("  output.txt    Path to output file (default: apt_commands.txt)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'apt_commands.txt'
    
    extract_apt_commands(input_file, output_file)


if __name__ == '__main__':
    main()
    
