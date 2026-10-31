from __future__ import annotations

import shutil
import tkinter as tk
from dataclasses import dataclass
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


CATEGORIES: dict[str, set[str]] = {
    "Documents": {".doc", ".docx", ".odt", ".pdf", ".rtf", ".txt", ".xls", ".xlsx", ".csv"},
    "Pictures": {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"},
    "Audio": {".aac", ".flac", ".m4a", ".mp3", ".ogg", ".wav", ".wma"},
    "Video": {".avi", ".m4v", ".mkv", ".mov", ".mp4", ".webm", ".wmv"},
    "Archives": {".7z", ".bz2", ".gz", ".rar", ".tar", ".zip"},
    "Code": {".c", ".cpp", ".css", ".go", ".html", ".java", ".js", ".json", ".py", ".rb", ".rs", ".sh", ".sql", ".ts", ".tsx", ".xml", ".yaml", ".yml"},
}


@dataclass(frozen=True)
class PlannedFile:
    source: Path
    category: str


def category_for(path: Path) -> str:
    extension = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def plan_files(folder: Path) -> list[PlannedFile]:
    """Return direct child files only; never recursively reorganise a folder."""
    return [
        PlannedFile(path, category_for(path))
        for path in sorted(folder.iterdir(), key=lambda item: item.name.lower())
        if path.is_file() and not path.is_symlink()
    ]


def available_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem} ({counter}){destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


class FileOrganiserApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("File Organiser")
        self.geometry("780x540")
        self.minsize(650, 420)
        self.option_add("*Font", "Segoe UI 10")

        self.folder = tk.StringVar()
        self.status = tk.StringVar(value="Choose a folder to get started.")
        self.files: list[PlannedFile] = []
        self.moved_files: list[tuple[Path, Path]] = []

        self._build_ui()

    def _build_ui(self) -> None:
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel", foreground="#5f6368")
        style.configure("Action.TButton", padding=(14, 8))

        outer = ttk.Frame(self, padding=24)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="File Organiser", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            outer,
            text="Sort files into clear categories without touching folders or overwriting anything.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(4, 18))

        folder_row = ttk.Frame(outer)
        folder_row.pack(fill="x")
        ttk.Label(folder_row, text="Folder", width=9).pack(side="left")
        ttk.Entry(folder_row, textvariable=self.folder).pack(side="left", fill="x", expand=True)
        ttk.Button(folder_row, text="Browse…", command=self.choose_folder).pack(side="left", padx=(8, 0))
        ttk.Button(folder_row, text="Scan", command=self.scan_folder).pack(side="left", padx=(8, 0))

        table_frame = ttk.Frame(outer)
        table_frame.pack(fill="both", expand=True, pady=(18, 8))
        columns = ("file", "category", "destination")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="none")
        self.table.heading("file", text="File")
        self.table.heading("category", text="Category")
        self.table.heading("destination", text="Destination")
        self.table.column("file", width=280, anchor="w")
        self.table.column("category", width=130, anchor="w")
        self.table.column("destination", width=280, anchor="w")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        bottom = ttk.Frame(outer)
        bottom.pack(fill="x", pady=(8, 0))
        ttk.Label(bottom, textvariable=self.status).pack(side="left")
        ttk.Button(bottom, text="Undo last sort", command=self.undo, state="disabled").pack(
            side="right", padx=(8, 0)
        )
        self.undo_button = bottom.winfo_children()[-1]
        self.organise_button = ttk.Button(
            bottom, text="Organise files", style="Action.TButton", command=self.organise, state="disabled"
        )
        self.organise_button.pack(side="right")

    def choose_folder(self) -> None:
        selected = filedialog.askdirectory(title="Choose a folder to organise")
        if selected:
            self.folder.set(selected)
            self.scan_folder()

    def scan_folder(self) -> None:
        selected = Path(self.folder.get()).expanduser()
        if not selected.is_dir():
            messagebox.showerror("Folder not found", "Please choose an existing folder.")
            return
        self.folder.set(str(selected.resolve()))
        self.files = plan_files(selected)
        for item in self.table.get_children():
            self.table.delete(item)
        for planned in self.files:
            destination = planned.source.parent / planned.category / planned.source.name
            self.table.insert("", "end", values=(planned.source.name, planned.category, str(destination)))
        count = len(self.files)
        self.status.set(f"{count} file{'s' if count != 1 else ''} ready to organise.")
        self.organise_button.configure(state="normal" if self.files else "disabled")

    def organise(self) -> None:
        if not self.files:
            return
        if not messagebox.askyesno(
            "Organise files?",
            f"Move {len(self.files)} file{'s' if len(self.files) != 1 else ''} into category folders?",
        ):
            return
        self.moved_files = []
        try:
            for planned in self.files:
                target_folder = planned.source.parent / planned.category
                target_folder.mkdir(exist_ok=True)
                destination = available_destination(target_folder / planned.source.name)
                shutil.move(str(planned.source), str(destination))
                self.moved_files.append((planned.source, destination))
        except OSError as error:
            messagebox.showerror("Could not organise files", str(error))
            self.status.set("Sort stopped because a file could not be moved.")
        else:
            self.files = []
            self.scan_folder()
            self.undo_button.configure(state="normal")
            self.status.set(f"Organised {len(self.moved_files)} files. You can undo this sort.")

    def undo(self) -> None:
        if not self.moved_files:
            return
        restored = 0
        try:
            for original, moved in reversed(self.moved_files):
                if moved.exists() and not original.exists():
                    shutil.move(str(moved), str(original))
                    restored += 1
        except OSError as error:
            messagebox.showerror("Could not undo sort", str(error))
            return
        self.moved_files = []
        self.undo_button.configure(state="disabled")
        self.scan_folder()
        self.status.set(f"Restored {restored} files.")


def main() -> None:
    app = FileOrganiserApp()
    app.mainloop()


if __name__ == "__main__":
    main()
