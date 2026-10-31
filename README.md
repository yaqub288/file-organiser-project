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

### Windows and macOS installation

On Windows, download `FileOrganiser-Windows.exe` and double-click it. On macOS,
download `FileOrganiser-macOS`, move it somewhere convenient, and open it. macOS
may require allowing it under **System Settings → Privacy & Security** the first
time.

## Safety features

- Only files directly inside the selected folder are considered.
- Existing files are never overwritten; duplicates receive a numbered name.
- The app shows a preview before anything is moved.
- The last sort can be undone.
- Symbolic links and subfolders are left untouched.

The category rules are defined near the top of `main.py`, so adding an extension
is as simple as adding it to the relevant set.
