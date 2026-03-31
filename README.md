# Running MicroGPT on your computer — Step by Step
[MicroGPT](https://karpathy.github.io/2026/02/12/microgpt/) is a script written by Andrej Karpathy. This is a slight modification to get you up and running on your own machine.

## Before you start
You need **Python 3** installed. To check, open your Terminal (Mac) or Command Prompt (Windows) and type:

**Mac:**
```bash
python3 --version
```
**Windows:**
```bash
python --version
```
If you see a version number like `Python 3.10.x` you're good to go. If not, download Python from [python.org](https://python.org).

---

## Step 1 — Open your Terminal
**Mac:** Press `Cmd + Space`, type `Terminal`, hit Enter.

**Windows:** Press the Windows key, type `cmd`, hit Enter.

---

## Step 2 — Navigate to your folder
Type `cd` followed by the path to where you saved the files.

**Mac:**
```bash
cd ~/Desktop
```
**Windows:**
```bash
cd C:\Users\YourName\Desktop
```
> 💡 Tip: Instead of typing the path, you can drag your folder into the terminal window after typing `cd ` (with a space) and it will fill in the path automatically.

---
## Step 3 - Add your data

Place your `.txt` file in the same folder as `microgpt.py`.
> If you'd like to just test with sample data, there's a file containing the 21,000 class names used to train imagenet in this folder that you may use (`imagenet21k_classes.txt`).

**Format**
Your file should be plain text (`.txt`) with **one item per line**. Each line is treated as a single training example — the model learns the patterns within each line, not across the whole file.

example:
```
Black-throated Warbler
Common Sandpiper
White-bellied Sea Eagle
Rufous Hummingbird
...
```

**Guidelines**
- names, species, places, titles, ingredients. Anything where each line follows a similar pattern.
- 5,000–20,000 lines is ideal for this script.
- the model handles up to 16 characters per line by default. Longer lines get cut off.
- Avoid long paragraphs or sentences — this script is designed for short items, not prose
- Avoid lots of rare characters like emoji, accents, or symbols — they bloat the vocabulary and confuse the model

---

## Step 4 — Run the script

**Mac:**
```bash
python3 microgpt.py --input names.txt
```
**Windows:**
```bash
python microgpt.py --input names.txt
```
You should see something like:
```
num docs: 20000
vocab size: 30
num params: 7040
step  100 / 1000 | loss 2.8421
```
Training will take a few minutes. When it's done it will print 20 generated names.

---

## Step 5 — Experiment with settings (optional)
You can adjust three settings to change how the model trains:

| Argument | What it does | Default | Safe range |
|---|---|---|---|
| `--n_embd` | Controls how many features the model tracks per character. Low = can only learn simple patterns like "this name starts with a capital". High = can learn complex patterns like "bird names often have a color followed by a body part". Must be a multiple of 4. | 16 | 8 – 256 |
| `--n_layer` | Controls how many times the model re-processes its own thinking. 1 layer = one pass at the pattern. 4 layers = the model can build on its own earlier conclusions, like first learning word structure, then learning how words combine. | 1 | 1 – 8 |
| `--num_steps` | How many training examples the model sees. More steps = more practice, up to a point. Too few and the model hasn't learned enough. Too many and you're just waiting with no benefit. | 1000 | 1 – 20000 |
| `--num_samples` | How many examples the model generates after training. | 20 | Any positive number |
| `--seed` | A word or phrase the model uses as a starting point when generating output. For example, `--seed "Ru"` will begin every generated name with those characters and continue from there. Only characters that appear in your training data will work — others are silently skipped. | none | Any short word or phrase |

Example — a bigger, longer-trained model:

**Mac:**
```bash
python3 microgpt.py --input names.txt --n_embd 32 --n_layer 2 --num_steps 5000
```
**Windows:**
```bash
python microgpt.py --input names.txt --n_embd 32 --n_layer 2 --num_steps 5000
```

> ⚠️ Higher values = slower training. Stick within the safe ranges above or the script will warn you.

---

## Common errors

**`python3: command not found` (Mac) / `python is not recognized` (Windows)** — Python isn't installed. Download it from [python.org](https://python.org). Windows users: make sure to check **"Add Python to PATH"** during installation.

**`No such file or directory`** — The terminal isn't in the right folder. Repeat Step 2, or try the drag-and-drop tip above.

**`AssertionError`** — One of your settings is outside the safe range. Read the error message — it will tell you exactly which one.


------
Using text_splitter.py

You can use this python file to split up a .txt file into single words per line. 
You can also set options so that its 2 or 3 or however many words per line instead of just 1. Put your original .txt file in this folder then run...

```python
python3 text_splitter.py --input name_of_your_original_file.txt --output name_of_file_you_want_to_output.txt
```

to get more than one word per line just change the number after --n in this code below
```python
python3 text_splitter.py --input name_of_your_original_file.txt --output name_of_file_you_want_to_output.txt --n 2
```