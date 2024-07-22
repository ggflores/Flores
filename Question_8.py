## Question 8: File Processing
# Write a Python program that does the following:
# 1. Reads a text file with its name passed as an argument to the program. The file contains a list of words separated by spaces.
# 2. Counts the occurrence of each word in the file
# 3. Writes the counts to a new text file, with name also passed as an argument, in the format word: count, one word per line.
# 4. The words should be sorted in descending order.
import sys
from collections import Counter

def question_8(input_file_str, output_file_str):
    try:
        with open(input_file_str, 'r') as file:
            text = file.read()
        
        words = text.split()
        word_counts = Counter(words)
        sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
       
        with open(output_file_str, 'w') as file:
            for word, count in sorted_word_counts:
                file.write(f"{word}: {count}\n")

        print(f"Word counts written to {output_file_str}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python question_8.py <input_file_str> <output_file_str>")
    else:
        input_file_str = sys.argv[1]
        output_file_str = sys.argv[2]
        question_8(input_file_str,output_file_str)