from googletrans import Translator
import xml.etree.ElementTree as ET

def translate_xml(xml_file, target_language='en'):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize the translator
    translator = Translator()

    # Iterate through each text element in the XML and translate
    for element in root.iter('text'):
        german_text = element.text

        # Skip if text is None or empty
        if not german_text:
            continue

        # Translate the text to English
        english_text = translator.translate(german_text, dest=target_language).text

        # Update the text element with the translated text
        element.text = english_text

    # Save the translated XML to a new file
    translated_xml_file = xml_file.replace('.xml', '_translated.xml')
    tree.write(translated_xml_file)

    print(f"Translation complete. Translated XML saved to: {translated_xml_file}")

# Example usage
if __name__ == "__main__":
    xml_file = 'test.xml'
    target_language = 'en'  # English

    translate_xml(xml_file, target_language)
