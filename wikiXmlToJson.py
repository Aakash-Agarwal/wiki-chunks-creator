import xml.etree.ElementTree as ET

def covert_to_json(xml_file):
    jsonData = list()
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate through each page element in the XML
    for element in root.iter('page'):
        jsonPage = dict()
        elementText = element.text

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
    xml_file = 'Onlinehelp-en.xml'

    covert_to_json(xml_file)
