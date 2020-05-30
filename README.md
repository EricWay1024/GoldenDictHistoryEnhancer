# GoldenDict History Enhancer

Add a list of new words to your GoldenDict history panel each time (so that you can remember them by reading explanations and example sentences in your dictionaries).

This Python program is developed on Arch Linux and is compatible with Unix machines.

## Usage

### Initialization

*You may want to delete the `json` files before first usage.*

1. Add your word list to `voclist.txt`. One word (or phrase) per line. The example `voclist.txt` is a GRE vocabulary list.

2. Run `python3 gdhe` and follow the instructions.

NB: Your word list will be shuffled, cut into equal-length parts and stored in `daily_words.json`.

### Update or Undo Last Update

Run `python3 gdhe` and follow the instructions.

NB: `goldendict` process will be automatically killed during the update or undo. Restart it manually.

Your progress will be saved in `index.json`.

You can undo only one step.