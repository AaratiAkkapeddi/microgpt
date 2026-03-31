import argparse

def split_words(input_file, output_file, words_per_line):
    with open(input_file, 'r') as f:
        words = f.read().split()
    
    lines = [' '.join(words[i:i+words_per_line]) for i in range(0, len(words), words_per_line)]
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Done! {len(words)} words written to {output_file} ({words_per_line} per line)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split text file into N words per line")
    parser.add_argument("--input", help="Input .txt file")
    parser.add_argument("--output", help="Output .txt file")
    parser.add_argument("-n", "--words", type=int, default=1, help="Words per line (default: 1)")
    args = parser.parse_args()
    
    split_words(args.input, args.output, args.words)