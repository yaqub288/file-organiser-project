# File Organiser

A small desktop app that sorts the files in a folder into category folders such as
`Documents`, `Pictures`, `Audio`, `Video`, `Archives`, `Code`, and `Other`.

## Download

**[Download the latest version](https://github.com/yaqub288/file-organiser-project/releases/latest)**

On the releases page, open the newest release and download:

- **Windows:** `FileOrganiser-Windows.exe`
- **macOS:** `FileOrganiser-macOS`
- **Linux:** `FileOrganiser-Linux`

No Python installation is needed. Download the file for your operating system,
then open it. On Linux, run `chmod +x FileOrganiser-Linux` once before opening it.

### Linux installation

1. Download `FileOrganiser-Linux` from the **Assets** section of the latest
   release.
2. Open Terminal and go to your Downloads folder:

   ```bash
   cd ~/Downloads
   ```

3. Allow the app to run:

   ```bash
   chmod +x FileOrganiser-Linux
   ```

4. Start it:

   ```bash
   ./FileOrganiser-Linux
   ```

The downloaded Linux file is portable, so Python and Tkinter are not required.
If you instead run the source code, use `python3 main.py` (not `python main.py`
on Ubuntu installations where the `python` command is not configured).

To keep the app in a personal applications folder:

```bash
mkdir -p ~/.local/bin
mv ~/Downloads/FileOrganiser-Linux ~/.local/bin/file-organiser
chmod +x ~/.local/bin/file-organiser
~/.local/bin/file-organiser
```

### Windows and macOS installation

On Windows, download `FileOrganiser-Windows.exe` and double-click it. On macOS,
download `FileOrganiser-macOS`, move it somewhere convenient, and open it. macOS
may require allowing it under **System Settings → Privacy & Security** the first
time.

## Run from source

Python 3.12+ and Tkinter are required. Tkinter is included with most Python
installations. On Ubuntu/Debian, install it with:

```bash
sudo apt install python3-tk
```

From the project directory:

```bash
python3 main.py
```

Or, if you use `uv`:

```bash
uv run file-organiser-project
```

## Share it with other people

The easiest way to share the app is as a standalone executable. The recipient
does not need Python, `uv`, or Tkinter installed.

Build it locally on the operating system you want to share:

```bash
python -m pip install pyinstaller
python build.py
```

The finished app is placed in `dist/`:

- Windows: `FileOrganiser.exe`
- macOS/Linux: `FileOrganiser`

PyInstaller builds are operating-system specific. Build on Windows for Windows
users, on macOS for Mac users, and on Linux for Linux users. Do not send the
Windows executable to a Mac or Linux user.

This repository also includes a GitHub Actions workflow. Run **Actions →
Build desktop apps → Run workflow** on GitHub, then download the Windows,
macOS, or Linux artifact from the completed workflow. Creating a tag such as
`v1.0.0` runs the same build automatically.

For the simplest public download experience, use the **Releases** section on
GitHub. Each version release contains ready-to-run files for all three
operating systems. Users download the file for their computer and do not need
Python or access to the source code.

## Safety features

- Only files directly inside the selected folder are considered.
- Existing files are never overwritten; duplicates receive a numbered name.
- The app shows a preview before anything is moved.
- The last sort can be undone.
- Symbolic links and subfolders are left untouched.

The category rules are defined near the top of `main.py`, so adding an extension
is as simple as adding it to the relevant set.
