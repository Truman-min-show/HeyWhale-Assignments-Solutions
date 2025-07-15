# File: submit.py (最终完美版)
import subprocess
import argparse
import os
import sys


def win_to_wsl_path(win_path):
    """Converts a Windows path (e.g., C:\\Users) to a WSL path (e.g., /mnt/c/Users)."""
    path = win_path.replace('\\', '/')
    drive, path_no_drive = os.path.splitdrive(path)
    drive_letter = drive.replace(':', '').lower()
    return f"/mnt/{drive_letter}{path_no_drive}"


def main():
    """Main function to handle argument parsing and command execution."""
    parser = argparse.ArgumentParser(
        description="Automate HeyWhale submission using WSL from Windows.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-t", "--token",
        required=True,
        help="Your submission token from the HeyWhale website."
    )
    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Relative path to your answer file (e.g., p1/answer_2.csv)."
    )
    args = parser.parse_args()

    # --- 1. Verify Paths and Files ---
    script_dir_win = os.getcwd()
    heywhale_tool_path = os.path.join(script_dir_win, 'heywhale_submit')
    answer_file_path = os.path.join(script_dir_win, args.file)

    if not os.path.exists(heywhale_tool_path):
        print(f"Error: The submission tool 'heywhale_submit' was not found in this directory:", file=sys.stderr)
        print(f"Searched in: {script_dir_win}", file=sys.stderr)
        print("Please make sure it's present before running.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(answer_file_path):
        print(f"Error: The answer file '{args.file}' was not found.", file=sys.stderr)
        print(f"Full path checked: {answer_file_path}", file=sys.stderr)
        sys.exit(1)

    # --- 2. Construct the WSL Command ---
    project_root_wsl = win_to_wsl_path(script_dir_win)

    command_inside_wsl = (
        f"cd {project_root_wsl} && "
        f"./heywhale_submit -token {args.token} -file {args.file}"
    )

    final_windows_command = ['wsl', 'bash', '-c', command_inside_wsl]

    # --- 3. Execute and Display Results ---
    print("🚀 Starting submission process via WSL...")
    try:
        process = subprocess.Popen(
            final_windows_command,
            stdout=subprocess.PIPE,
            # [美化] 忽略WSL启动时的底层信息，让输出更干净
            stderr=subprocess.DEVNULL,
            text=True,
            encoding='utf-8',
            errors='replace'
        )

        for line in iter(process.stdout.readline, ''):
            print(line, end='')

        process.wait()
        print("\n✅ Submission process finished.")

    except FileNotFoundError:
        print("Error: 'wsl.exe' not found. Is WSL installed correctly and in your system's PATH?", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()