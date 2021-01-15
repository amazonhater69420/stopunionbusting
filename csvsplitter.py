# Helper script to split @marx_hxc's csv file into separate files
import os
import csv
import argparse
import nltk.data

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

parser = argparse.ArgumentParser(description="Split @marx_hxc's csv file containing GPT3 generated messages into separate files")
parser.add_argument("--output_dir",
                    metavar="output_dir",
                    nargs=1,
                    default="messages/gpt3generated",
                    required=False,
                    help="directory to output to")
parser.add_argument("--start_count",
                    metavar="start_count",
                    nargs=1,
                    type=int,
                    default=1,
                    required=False,
                    help="number of first output file")
parser.add_argument("path",
                    metavar="path",
                    nargs=1,
                    type=str,
                    help="split specified file")
options = parser.parse_args()

with open(options.path[0]) as csvfile:
    csvreader = csv.reader(csvfile)
    count = options.start_count
    for row in csvreader:
        with open(os.path.join(options.output_dir, str(count) + ".txt"), mode="w") as output_file:
            tokenized = tokenizer.tokenize(row[4])
            output_file.write(tokenized[0] + "\n") # Write subject line 
            output_file.write(" ".join(tokenized[1:])) # Write the rest of the message

        count = count + 1
