# ubuntu-settings

## APT Command Extractor

A Python script that extracts apt commands from the `history.log` file.

### Usage

```bash
python3 extract_apt_commands.py <history.log> [output.txt]
```

### Arguments

- `history.log` - Path to the apt history.log file (usually located at `/var/log/apt/history.log`)
- `output.txt` - (Optional) Path to the output file. Default: `apt_commands.txt`

### Example

```bash
# Extract commands from history.log to apt_commands.txt (default)
python3 extract_apt_commands.py history.log

# Extract commands to a custom output file
python3 extract_apt_commands.py history.log my_commands.txt

# Use with system apt history
python3 extract_apt_commands.py /var/log/apt/history.log
```

### What it does

The script reads the apt history.log file, which contains detailed information about all apt/apt-get commands executed on the system, and extracts only the command lines. The output is a simple text file with one command per line, without the additional metadata (dates, requested-by, install/remove details, etc.).

### Input Format

The script expects an apt history.log file with entries in the following format:

```
Start-Date: 2023-10-01  10:30:00
Commandline: apt install vim
Requested-By: user (1000)
Install: vim:amd64 (2:8.2.3995-1ubuntu2.1)
End-Date: 2023-10-01  10:30:15
```

### Output Format

The output file contains only the commands, one per line:

```
apt install vim
apt-get update
apt upgrade
apt remove --purge firefox
```