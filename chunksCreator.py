import json
from collections import OrderedDict

def breakChunks(page_title, page_text, chunk_num = 1):
    chunks = list()
    prefix = "page_title: " + page_title + "\npage_text: "
    str = prefix + page_text
    if (len(str) > 1000):
        chunk1 = str[0:1000]
        chunk2 = str[800:]
        
        chunks.append(chunk1)
        
        if (len(prefix + chunk2) > 1000):
            for brokenChunk in breakChunks(page_title, chunk2, chunk_num + 1):
                chunks.append(brokenChunk)
        else:
            chunks.append(prefix + chunk2)
    else:
        chunks.append(str)
    
    return chunks


def createChunks(jsonFile):
    chunks = list()
    data = dict()
    with open(jsonFile, 'r', encoding='utf-8') as file:
        wiki_text = file.read()
        wiki_json = json.loads(wiki_text)
        page_list = wiki_json['mediawiki']['page']
        for wiki_page in page_list:
            page_title = wiki_page['title']
            page_text = wiki_page['revision']['text']['__text']
            for brokenChunk in breakChunks(page_title, page_text):
                chunks.append(brokenChunk)
    num = 1
    for chunk in chunks:
        data[num] = chunk
        num += 1
    
    with open("chunks_dict2.json", "w",encoding="utf-8") as f:
        # Dump the JSON object to the file
        json.dump(data, f, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    file = 'Onlinehelp-en.json'
    createChunks(file)
    chunks = list()
    with open("chunks_dict2.json", 'r', encoding='utf-8') as file:
        for chunk in json.load(file, object_hook=OrderedDict).values():
            chunks.append(chunk)
    
    print(len(chunks))