# File Organiser

A small desktop app that sorts the files in a folder into category folders such as
`Documents`, `Pictures`, `Audio`, `Video`, `Archives`, `Code`, and `Other`.

## Run it

Python 3.12+ and Tkinter are required. Tkinter is included with most Python
installations. On Ubuntu/Debian, install it with:

```bash
sudo apt install python3-tk
```

From the project directory:

```bash
python main.py
```

Or, if you use `uv`:

```bash
uv run file-organiser-project
```

## Safety features

- Only files directly inside the selected folder are considered.
- Existing files are never overwritten; duplicates receive a numbered name.
- The app shows a preview before anything is moved.
- The last sort can be undone.
- Symbolic links and subfolders are left untouched.

The category rules are defined near the top of `main.py`, so adding an extension
is as simple as adding it to the relevant set.
