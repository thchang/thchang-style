import sys

# Define global variables
global entry_type
global entry_content
global itemtype
global howpublished
global year
global month
global author
global title
global journal
global editor
global booktitle
global volume
global number
global articleno
global chapter
global pages
global organization
global location
global doi
global url
global isbn
global note


def reset():
    """ Reset the global variables to empty strings """

    # Reference global variables
    global entry_type
    global entry_content
    global itemtype
    global howpublished
    global year
    global month
    global author
    global title
    global journal
    global editor
    global booktitle
    global volume
    global number
    global articleno
    global chapter
    global pages
    global organization
    global location
    global doi
    global url
    global isbn
    global note
    global bib

    entry_type = None
    entry_content = None
    itemtype = None
    howpublished = None
    year = None
    month = None
    author = None
    title = None
    journal = None
    editor = None
    booktitle = None
    volume = None
    number = None
    articleno = None
    chapter = None
    pages = None
    organization = None
    location = None
    doi = None
    url = None
    isbn = None
    note = None
    bib = None


def addEntry():
    """ Update the global helper variables for the corresponding entry """

    # Reference global variables
    global entry_type
    global entry_content
    global itemtype
    global howpublished
    global year
    global month
    global author
    global title
    global journal
    global editor
    global booktitle
    global volume
    global number
    global articleno
    global chapter
    global pages
    global organization
    global location
    global doi
    global url
    global isbn
    global note
    global bib

    from .utils import parseAuthors, parseTitle

    if entry_type is None or entry_content is None:
        return
    if entry_type.lower() in ("bib"):
        bib = entry_content.replace("\\", "\\\\")
        return
    entry_content = entry_content.strip()
    entry_content = entry_content.replace("$", "")
    entry_content = entry_content.replace("\\$", "$DOLLAR")
    entry_content = entry_content.replace("\\&", "$AND")
    entry_content = entry_content.replace("\\bf", "$BOLD1")
    entry_content = entry_content.replace("\\textbf", "$BOLD2")
    entry_content = entry_content.replace("\\sl", "$SLANTED")
    entry_content = entry_content.replace("\\it", "$ITALICS1")
    entry_content = entry_content.replace("\\textit", "$ITALICS2")
    entry_content = entry_content.replace("\\url", "$URL")
    entry_content = entry_content.replace("\\%", "$PERCENT")
    entry_content = entry_content.replace("\\sim", "$TILDE")
    entry_content = entry_content.replace("\\{", "$LBRACK")
    entry_content = entry_content.replace("\\}", "$RBRACK")
    if (    (entry_content[0] == "{" and entry_content[-1] == "}") or
            (entry_content[0] == '"' and entry_content[-1] == '"') or
            (entry_content[0] == "'" and entry_content[-1] == "'")):
        entry_content = entry_content[1:-1]
    elif (    (entry_content[0] == "{" and entry_content[-2:] == "},") or
            (entry_content[0] == '"' and entry_content[-2:] == '",') or
            (entry_content[0] == "'" and entry_content[-2:] == "',")):
        entry_content = entry_content[1:-2]
    if entry_type.lower() in ("type", "howpublished"):
        howpublished = entry_content
    elif entry_type.lower() in ("year"):
        year = entry_content
    elif entry_type.lower() in ("month"):
        month = entry_content
    elif entry_type.lower() in ("author"):
        author = parseAuthors(entry_content)
    elif entry_type.lower() in ("title"):
        title = parseTitle(entry_content)
    elif entry_type.lower() in ("journal"):
        journal = entry_content
    elif entry_type.lower() in ("editor"):
        editor = entry_content
    elif entry_type.lower() in ("booktitle"):
        booktitle = entry_content
    elif entry_type.lower() in ("volume"):
        volume = entry_content
    elif entry_type.lower() in ("number"):
        number = entry_content
    elif entry_type.lower() in ("articleno"):
        articleno = entry_content
    elif entry_type.lower() in ("chapter"):
        chapter = entry_content
    elif entry_type.lower() in ("pages", "numpages"):
        if entry_type.lower() == "pages":
            pages = f"pp. {entry_content}"
        else:
            pages = f"{entry_content} pages"
    elif entry_type.lower() in ("organization", "publisher", "school", "institution"):
        organization = entry_content
    elif entry_type.lower() in ("location", "address"):
        location = entry_content
    elif entry_type.lower() in ("doi"):
        doi = entry_content
    elif entry_type.lower() in ("url"):
        url = entry_content
    elif entry_type.lower() in ("isbn"):
        isbn = entry_content
    elif entry_type.lower() in ("note"):
        note = entry_content


def joinAll():
    """ Join all helper variables to form YAML entry """

    # Reference global variables
    global entry_type
    global entry_content
    global itemtype
    global howpublished
    global year
    global month
    global author
    global title
    global journal
    global editor
    global booktitle
    global volume
    global number
    global articleno
    global chapter
    global pages
    global organization
    global location
    global doi
    global url
    global isbn
    global note
    global bib

    if itemtype is None:
        return ""
    elif itemtype.lower() == "article":
        output = "- article:\n"
        if year is not None:
            output = output + f'    year: "{year}"\n'
        if author is not None:
            output = output + f'    author: "{author}"\n'
        if title is not None:
            output = output + f'    title: "{title}"\n'
        if journal is not None:
            output = output + f'    journal: "{journal}"\n'
        if volume is not None:
            output = output + f'    volume: "{volume}"\n'
        if number is not None:
            output = output + f'    number: "{number}"\n'
        if articleno is not None:
            output = output + f'    articleno: "{articleno}"\n'
        if pages is not None:
            output = output + f'    pages: "{pages}"\n'
        if doi is not None:
            output = output + f'    doi: "{doi}"\n'
        if url is not None:
            output = output + f'    url: "{url}"\n'
        if isbn is not None:
            output = output + f'    isbn: "{isbn}"\n'
        if note is not None:
            output = output + f'    note: "{note}"\n'
        if bib is not None:
            output = output + f'    bib: "{bib}"\n'
    elif itemtype.lower() in ("inproceedings", "conference", "incollection",
                              "inbook"):
        output = f"- {itemtype}:\n"
        if year is not None:
            output = output + f'    year: "{year}"\n'
        if author is not None:
            output = output + f'    author: "{author}"\n'
        if title is not None:
            output = output + f'    title: "{title}"\n'
        if editor is not None:
            output = output + f'    editor: "{editor}"\n'
        if booktitle is not None:
            output = output + f'    booktitle: "{booktitle}"\n'
        if volume is not None:
            output = output + f'    volume: "{volume}"\n'
        if number is not None:
            output = output + f'    number: "{number}"\n'
        if articleno is not None:
            output = output + f'    articleno: "{articleno}"\n'
        if chapter is not None:
            output = output + f'    chapter: "{chapter}"\n'
        if pages is not None:
            output = output + f'    pages: "{pages}"\n'
        if organization is not None:
            output = output + f'    organization: "{organization}"\n'
        if location is not None:
            output = output + f'    location: "{location}"\n'
        if doi is not None:
            output = output + f'    doi: "{doi}"\n'
        if url is not None:
            output = output + f'    url: "{url}"\n'
        if isbn is not None:
            output = output + f'    isbn: "{isbn}"\n'
        if note is not None:
            output = output + f'    note: "{note}"\n'
        if bib is not None:
            output = output + f'    bib: "{bib}"\n'
    elif itemtype.lower() in ("techreport", "mastersthesis", "phdthesis"):
        if itemtype == "techreport":
            output = "- techreport:\n    type: Technical Report\n"
        else:
            output = "- thesis:\n"
            if howpublished is not None:
                output = output + f'    type: {howpublished}\n'
            elif itemtype == "mastersthesis":
                output = output + '    type: Masters Thesis\n'
            else:
                output = output + '    type: Ph.D. Dissertation\n'
        if year is not None:
            output = output + f'    year: "{year}"\n'
        if author is not None:
            output = output + f'    author: "{author}"\n'
        if title is not None:
            output = output + f'    title: "{title}"\n'
        if number is not None:
            output = output + f'    number: "{number}"\n'
        if organization is not None:
            output = output + f'    organization: "{organization}"\n'
        if location is not None:
            output = output + f'    location: "{location}"\n'
        if doi is not None:
            output = output + f'    doi: "{doi}"\n'
        if url is not None:
            output = output + f'    url: "{url}"\n'
        if isbn is not None:
            output = output + f'    isbn: "{isbn}"\n'
        if note is not None:
            output = output + f'    note: "{note}"\n'
        if bib is not None:
            output = output + f'    bib: "{bib}"\n'
    elif itemtype.lower() in ("book", "proceedings", "booklet"):
        output = f"- {itemtype}:\n    type: Technical Report\n"
        if year is not None:
            output = output + f'    year: "{year}"\n'
        if author is not None:
            output = output + f'    author: "{author}"\n'
        if title is not None:
            output = output + f'    title: "{title}"\n'
        if number is not None:
            output = output + f'    number: "{number}"\n'
        if editor is not None:
            output = output + f'    editor: "{editor}"\n'
        if organization is not None:
            output = output + f'    organization: "{organization}"\n'
        if location is not None:
            output = output + f'    location: "{location}"\n'
        if doi is not None:
            output = output + f'    doi: "{doi}"\n'
        if url is not None:
            output = output + f'    url: "{url}"\n'
        if isbn is not None:
            output = output + f'    isbn: "{isbn}"\n'
        if note is not None:
            output = output + f'    note: "{note}"\n'
        if bib is not None:
            output = output + f'    bib: "{bib}"\n'
    elif itemtype.lower() == "misc":
        if howpublished is not None:
            output = f"- {''.join(howpublished.lower().strip().split())}:\n"
        else:
            output = output + "- misc:\n"
        if year is not None:
            output = output + f'    year: "{year}"\n'
        if month is not None:
            output = output + f'    month: "{month}"\n'
        if author is not None:
            output = output + f'    author: "{author}"\n'
        if title is not None:
            output = output + f'    title: "{title}"\n'
        if journal is not None:
            output = output + f'    journal: "{journal}"\n'
        if number is not None:
            output = output + f'    number: "{number}"\n'
        if booktitle is not None:
            output = output + f'    booktitle: "{booktitle}"\n'
        if organization is not None:
            output = output + f'    organization: "{organization}"\n'
        if location is not None:
            output = output + f'    location: "{location}"\n'
        if doi is not None:
            output = output + f'    doi: "{doi}"\n'
        if url is not None:
            output = output + f'    url: "{url}"\n'
        if isbn is not None:
            output = output + f'    isbn: "{isbn}"\n'
        if note is not None:
            output = output + f'    note: "{note}"\n'
        if bib is not None:
            output = output + f'    bib: "{bib}"\n'
    else:
        raise Warning(f"Entry type '{itemtype}' not recognized, skipping...")
    return output + "\n"


def bib2yml(fin):
    """ Convert fin to a yaml-style string and return """

    # Reference global variables
    global entry_type
    global entry_content
    global itemtype
    global howpublished
    global year
    global month
    global author
    global title
    global journal
    global editor
    global booktitle
    global volume
    global number
    global articleno
    global chapter
    global pages
    global organization
    global location
    global doi
    global url
    global isbn
    global note
    global bib
 
    # Read the input .bib file
    with open(fin, 'r') as fp:
        inlines = fp.readlines()
    
    # Initialize list of output lines and loop over all lines in the file
    reset()
    outlines = []
    bibstr = ""
    for line in inlines:
        # Append item and join types
        if len(line.strip()) > 0 and line.strip()[0] == '@':
            # remove trailing bracket
            if entry_content is not None:
                entry_content = entry_content.strip()[:-1]
            addEntry()
            if len(bibstr) > 0:
                entry_type = "bib"
                entry_content = bibstr
                addEntry()
            outlines.append(joinAll())
            reset()
            itemtype = line.split('@')[1].split("{")[0]
            bibstr = line
        else:
            if len(line.strip().split('=')) >= 2:
                addEntry()
                entry_type = line.strip().split('=')[0].strip()
                entry_content = "=".join(line.strip().split('=')[1:]).strip()
                bibstr = bibstr + f"  {line}"
            elif len(line.strip()) > 0 and entry_content is not None:
                if len(line.strip()) > 0:
                    entry_content = entry_content + " " + line.strip()
                bibstr = bibstr + line
    # Add last trailing item to the yaml
    if entry_content is not None:
        entry_content = entry_content[:-1].strip()
    addEntry()
    if len(bibstr) > 0:
        entry_type = "bib"
        entry_content = bibstr
        addEntry()
    outlines.append(joinAll())
    
    return "".join(outlines)
