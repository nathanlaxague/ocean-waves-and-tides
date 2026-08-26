# Ocean Waves and Tides

Jupyter notebooks for an upper-level undergraduate / introductory graduate course
on ocean waves and tides (OE 754/854).

Notebooks are released as the semester progresses, so this repository grows over
time. Everything already here is ready to run.

```
weekly_notebooks/     one notebook per week, released weekly
homework_solutions/   worked solutions, released after each deadline
figure_style.py       shared plot style used by every notebook
requirements.txt      Python packages needed to run the notebooks
```

All notebooks ship with their outputs baked in, so they can be read on GitHub or
in nbviewer without running anything. To run them yourself, set up an environment
as below.

## Setup

### 1. Install `uv`

[`uv`](https://docs.astral.sh/uv/) handles the Python version, the virtual
environment, and the packages.

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your shell, then confirm with `uv --version`.

### 2. Create the virtual environment

From the root of your clone:

```bash
uv venv --python 3.12
```

This creates `.venv/` in the repository (already gitignored). If your clone lives
inside a cloud-synced folder (Dropbox, OneDrive, Google Drive), put the
environment outside that tree instead so the sync client does not churn on it:

```bash
uv venv ~/Documents/.virtual_reality/ocean-waves-and-tides --python 3.12
```

### 3. Install the packages

```bash
uv pip install -r requirements.txt
```

If you created the environment outside the repository, point `uv` at it:

```bash
uv pip install --python ~/Documents/.virtual_reality/ocean-waves-and-tides/bin/python \
    -r requirements.txt
```

The packages are NumPy, SciPy, Matplotlib, Seaborn, and Jupyter. No data files
are downloaded — every notebook generates what it needs.

### 4. Launch Jupyter

```bash
source .venv/bin/activate      # Windows: .venv\Scripts\activate
jupyter lab
```

Open any notebook and run it top to bottom. Execution order is linear within a
notebook, and nothing carries over between notebooks.

### Fonts

`figure_style.py` asks for **Fira Sans**. If it is not installed system-wide,
Matplotlib falls back to its default sans font and prints a `findfont` warning
for each text element — the figures still render correctly. To silence the
warnings, install Fira Sans (free from Google Fonts; packaged as `fonts-firacode`
or similar on most Linux distributions).

## Plot style

`figure_style.py` at the repository root is the single source of truth for the
plot style. The `figure_style.py` inside `weekly_notebooks/` and
`homework_solutions/` is a small loader that executes the root module and
re-exports it, so notebooks can use a plain `import figure_style as fs` from
either folder. Edit the root file only; leave the loaders alone.

Importing the module applies the style and exposes `fs.color_list` (hex colors in
plot-cycle order), `fs.fullwidth` and `fs.fullheight` (full-page figure size in
inches for letter paper with 0.5 in margins), and `fs.fsize` (base font size).
