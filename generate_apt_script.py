#!/usr/bin/env python3
"""
Script to generate a bash executable from apt_history.txt
Adds apt update and apt upgrade before each command (unless already present)
"""

import os


def generate_apt_script(input_file='apt_history.txt', output_file='install_packages.sh'):
    """
    Generate a bash script from apt history file.
    
    Args:
        input_file: Path to the apt history text file
        output_file: Path to the output bash script
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return
    
    # Read all commands from the input file
    with open(input_file, 'r') as f:
        commands = [line.strip() for line in f if line.strip()]
    
    # Generate the bash script
    with open(output_file, 'w') as f:
        # Write shebang and header
        f.write("#!/bin/bash\n")
        f.write("#\n")
        f.write("# Auto-generated apt installation script\n")
        f.write(f"# Generated from: {input_file}\n")
        f.write("#\n")
        f.write("# This script will install all packages from the apt history\n")
        f.write("#\n\n")
        
        f.write("# Exit on error\n")
        f.write("set -e\n\n")
        
        f.write("# Check if running as root\n")
        f.write("if [ \"$EUID\" -ne 0 ]; then\n")
        f.write("    echo \"Please run this script with sudo\"\n")
        f.write("    exit 1\n")
        f.write("fi\n\n")
        
        f.write("echo \"Starting package installation...\"\n")
        f.write("echo \"=====================================\"\n\n")
        
        # Process each command
        for i, cmd in enumerate(commands, 1):
            # Check if the current command is apt update or apt upgrade
            is_update_or_upgrade = cmd in ['apt update', 'apt upgrade']
            
            # Add update and upgrade before each command (unless it's already update/upgrade)
            if not is_update_or_upgrade:
                # Check if previous command was apt update or apt upgrade
                needs_update = True
                needs_upgrade = True
                
                if i > 1:
                    prev_cmd = commands[i - 2]
                    if prev_cmd == 'apt update':
                        needs_update = False
                    if prev_cmd == 'apt upgrade':
                        needs_upgrade = False
                
                if needs_update:
                    f.write(f"echo \"Running apt update before command {i}...\"\n")
                    f.write("apt update\n\n")
                
                if needs_upgrade:
                    f.write(f"echo \"Running apt upgrade before command {i}...\"\n")
                    f.write("apt upgrade -y\n\n")
            
            # Write the actual command
            f.write(f"echo \"Executing command {i}: {cmd}\"\n")
            
            # Add -y flag for non-interactive installation (except for update/upgrade that don't install)
            if cmd.startswith('apt install'):
                cmd = cmd.replace('apt install', 'apt install -y', 1)
            elif cmd == 'apt upgrade':
                cmd = 'apt upgrade -y'
            
            f.write(f"{cmd}\n\n")
        
        f.write("echo \"=====================================\"\n")
        f.write("echo \"All packages installed successfully!\"\n")
    
    # Make the script executable
    os.chmod(output_file, 0o755)
    
    print(f"Successfully generated {output_file}")
    print(f"Processed {len(commands)} commands")
    print(f"\nTo execute the script, run:")
    print(f"  sudo ./{output_file}")


if __name__ == '__main__':
    generate_apt_script()
