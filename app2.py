from wikiextractor import WikiExtractor as we
import regex as re

# Extract the text from the XML file
text = we.process_dump(input_file="Onlinehelp-en.xml", out_file="extracted")

# Find all of the paragraphs in the text
paragraphs = re.findall(r'(?s)<p>(.*?)</p>', text)

# Print the paragraphs
for paragraph in paragraphs:
    print(paragraph)
