import re
import argparse
from bs4 import BeautifulSoup

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Extract transcript text from an HTML file.')
parser.add_argument('input_file', help='The input HTML file containing the transcript.')
parser.add_argument('output_file', help='The output text file to save the transcript.')

args = parser.parse_args()

# Open and read the input HTML file
with open(args.input_file, 'r', encoding='utf-8') as file:
    html = file.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'lxml')  # or 'html.parser'

# Extract the transcript lines
transcript_lines = soup.find_all('div', class_='transcript-text')

# Create a list to store the processed transcript text
transcript_text = []

# Process each line
for line in transcript_lines:
    # Get the text content of the line
    text = line.get_text()

    # Use a regular expression to split the text by punctuation (periods, question marks, exclamation marks)
    sentences = re.split(r'([.!?])', text)

    # Join the sentences with the punctuation and add a newline after each sentence
    processed_text = ''.join([sent + punc + '\n' for sent, punc in zip(sentences[::2], sentences[1::2])])

    # Add the processed text to the list
    transcript_text.append(processed_text)

# Join all the processed lines into a single string
output = ''.join(transcript_text)

# Save the output transcript to the specified output file
with open(args.output_file, 'w', encoding='utf-8') as output_file:
    output_file.write(output)

print(f"Transcript extracted and saved to '{args.output_file}'")
