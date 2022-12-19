def articleWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a target="_blank" href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = (outstr + f'<a target="_blank" href="{item["url"]}">' +
                      f'url: {item["url"]}</a>')
        elif 'isbn' in item.keys():
            outstr = outstr + f"In ISBN: {item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',`{popup_text}`)">View bib entry</a>\n"""
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def proceedingsWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'booktitle' in item.keys():
            outstr = outstr + f"<i> In {item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a target="_blank" href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = (outstr + f'<a target="_blank" href="{item["url"]}">' +
                      f'url: {item["url"]}</a>')
        elif 'isbn' in item.keys():
            outstr = outstr + f"In ISBN: {item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',`{popup_text}`)">View bib entry</a>\n"""
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def techreportWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"<i>{item['title']}</i>. "
        if 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' not in item.keys():
                outstr = outstr + ". "
        if 'number' in item.keys():
            outstr = outstr + f" {item['number']}. "
        if 'organization' in item.keys():
            outstr = outstr + f"{item['organization']}"
            if 'location' in item.keys():
                outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a target="_blank" href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = (outstr + f'<a target="_blank" href="{item["url"]}">' +
                      f'url: {item["url"]}</a>')
        elif 'isbn' in item.keys():
            outstr = outstr + f"In ISBN: {item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',`{popup_text}`)">View bib entry</a>\n"""
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def talkWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'month' in item.keys():
            outstr = outstr + f"{item['month']} "
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'booktitle' in item.keys():
            outstr = outstr + f"<i>{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ", "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def miscPubWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'booktitle' in item.keys():
            outstr = outstr + f"<i>{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',`{popup_text}`)">View bib entry</a>\n"""
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def softwareWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'logo' in item.keys():
            outstr = outstr + f'<img src="{item["logo"]}" display="block" align="right" height="50em" width="auto" hspace="20em">\n'
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'title' in item.keys():
            outstr = outstr + f"<b>{item['title']}</b>"
            if 'subtitle' in item.keys():
                outstr = outstr + f": {item['subtitle']}"
            if 'version' in item.keys():
                outstr = outstr + f"<br>\nRelease: {item['version']}"
        if 'author' in item.keys():
            outstr = outstr + f"<br>\nDevs: {item['author']}"
        if 'language' in item.keys():
            outstr = (outstr + f"<br>\nPrimary Prog. Lang: {item['language']}")
        if 'note' in item.keys():
            outstr = outstr + f"<br>\n{item['note']}"
        if 'description' in item.keys() or 'links' in item.keys() or 'git' in item.keys() or 'url' in item.keys() or 'doi' in item.keys():
            outstr = outstr + "\n<br>\n"
            desc = ""
            link = ""
            if 'description' in item.keys():
                outstr = outstr + f'<button onclick="{item["title"]}Desc()">More Info</button>\n'
                desc = item['description']
            if 'links' in item.keys() or 'doi' in item.keys() or 'git' in item.keys() or 'url' in item.keys():
                link = link + "<ul>\n"
                outstr = outstr + f'<button onclick="{item["title"]}Link()">View Links</button>\n'
                if 'doi' in item.keys():
                    link = (link + '<li><a target="_blank" ' +
                            f'href="https://doi.org/{item["doi"]}>"' +
                            f"doi: {item['doi']}</a></li>\n")
                if 'git' in item.keys():
                    link = (link + '<li><a target="_blank" ' +
                            f'href="{item["git"]}">' +
                            f"Git Repository</a></li>\n")
                if 'url' in item.keys():
                    link = (link + '<li><a target="_blank" ' +
                            f'href="{item["url"]}>"' +
                            f"link: {item['url']}</a></li>\n")
                if 'links' in item.keys():
                    for li in item['links']:
                        for key in li.keys():
                            link = link + '<li><a target="_blank" '
                            link = link + f'href="{li[key]}">{key}</a></li>\n'
                link = link + "</ul>\n"
            outstr = outstr + f'</p>\n<p id="{item["title"]}Info"></p>\n'
            outstr = outstr + f"""<script>
    function {item['title']}Desc() {{
        document.getElementById("{item['title']}Info").innerHTML = `
    <button onclick="{item['title']}Hide()">hide</button><br>
    {desc}
    `;
    }}

	function {item['title']}Link() {{
        document.getElementById("{item['title']}Info").innerHTML = `
    <button onclick="{item['title']}Hide()">hide</button><br>
    {link}
    `;
    }}

    function {item['title']}Hide() {{
        document.getElementById("{item['title']}Info").innerHTML = "";
    }}
    </script>\n"""
        outlist.append("<p>\n")
        outlist.append(outstr)
    return "\n<br>\n".join(outlist)

def proposalWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        elif 'start' in item.keys():
            outstr = outstr + f"{item['start']} - "
            if 'end' in item.keys():
                outstr = outstr + f"{item['end']}. "
            else:
                outstr = outstr + "Present. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f": {item['subtitle']}. "
            else:
                outstr = outstr + ". "
        outstr = outstr + "<br>\n"
        if 'role' in item.keys():
            outstr = (outstr + f"<b>Role: {item['role']}</b>.")
            if 'collaborators' in item.keys():
                for collab in item['collaborators']:
                    for key in collab.keys():
                        outstr = (outstr + f" &nbsp {key}: {collab[key]}.")
        outstr = outstr + "<br>\n"
        if 'agency' in item.keys():
            outstr = outstr + f"{item['agency']}"
        if 'foa' in item.keys():
            if 'agency' in item.keys():
                outstr = outstr + ": "
            outstr = outstr + f"<i>{item['foa']}</i>"
        if 'number' in item.keys():
            if 'foa' in item.keys():
                outstr = outstr + f" ({item['number']})"
            else:
                outstr = outstr + f" {item['number']}"
        outstr = outstr + ".<br>\n"
        if 'type' in item.keys():
            outstr = (outstr + f"Type: {item['type']}")
        if 'numpages' in item.keys():
            outstr = (outstr + f" ({item['numpages']})")
        if 'budget' in item.keys():
            outstr = (outstr + f". Budget: {item['budget']}")
        if 'length' in item.keys():
            outstr = (outstr + f". Length: {item['length']}")
        outstr = outstr + "."
        if 'note' in item.keys():
            outstr = outstr + f"<br>\n{item['note']}"
        if 'doi' in item.keys():
            outstr = (outstr + '<br>\n <a target="_blank" ' +
                      f'href="https://doi.org/{item["doi"]}>"' +
                      f"doi: {item['doi']}</a>")
        if 'git' in item.keys():
            outstr = (outstr + '<br>\n <a target="_blank" ' +
                      f'href="{item["git"]}>"' +
                      f"git: {item['git']}</a>")
        if 'url' in item.keys():
            outstr = (outstr + '<br>\n <a target="_blank" ' +
                      f'href="{item["url"]}>"' +
                      f"link: {item['url']}</a>")
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def anypubWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'journal' not in item.keys() and 'booktitle' not in item.keys():
            if 'title' in item.keys():
                outstr = outstr + f"<i>{item['title']}</i>. "
        else:
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'booktitle' in item.keys():
            if 'chapter' in item.keys():
                outstr = outstr + f"Ch. {item['chapter']} "
            outstr = outstr + "<i>In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' in item.keys():
                outstr = outstr + f" {item['number']}"
            outstr = outstr + ". "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        else:
            if 'number' in item.keys():
                outstr = outstr + f"{item['number']}. "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = outstr + f'<a href="{item["url"]}">url: {item["url"]}</a>'
        elif 'isbn' in item.keys():
            outstr = outstr + "In isbn: " + f"{item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',`{popup_text}`)">View bib entry</a>\n"""
        outlist.append(outstr)
    return "\n<br><br>\n".join(outlist)

def collapsablePubWeb(inlist):
    yearlists = {}
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'journal' not in item.keys() and 'booktitle' not in item.keys():
            if 'title' in item.keys():
                outstr = outstr + f"<i>{item['title']}</i>. "
        else:
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'booktitle' in item.keys():
            if 'chapter' in item.keys():
                outstr = outstr + f"Ch. {item['chapter']} "
            outstr = outstr + "<i>In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' in item.keys():
                outstr = outstr + f" {item['number']}"
            outstr = outstr + ". "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        else:
            if 'number' in item.keys():
                outstr = outstr + f"{item['number']}. "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = outstr + f'<a href="{item["url"]}">url: {item["url"]}</a>'
        elif 'isbn' in item.keys():
            outstr = outstr + "In isbn: " + f"{item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',\`{popup_text}\`)">View bib entry</a>\n"""
        if 'year' in item.keys():
            if f"{item['year']}" in yearlists.keys():
                yearlists[f'{item["year"]}'].append(outstr)
            else:
                yearlists[f'{item["year"]}'] = [outstr]
        else:
            if "NoYear" in yearlists.keys():
                yearlists['NoYear'].append(outstr)
            else:
                yearlists['NoYear'] = [outstr]
    outstr = ""
    for key in yearlists.keys():
        outstr = outstr + f"""    <button onclick="pubs{key}Show()"
        id="pubs{key}Button">
        {key} ({len(yearlists[key])} items)</button>
    </p>
    <p id="pubs{key}List"></p>
    <script>
    var pubs{key}Button = document.getElementById("pubs{key}Button");
    pubs{key}Button.style.cssText = 'width: 100%';
    function pubs{key}Show() {{
        document.getElementById("pubs{key}List").innerHTML = `
    <button onclick="pubs{key}Hide()">hide</button><br>
    {"<br><br>".join(yearlists[key])}
    `;
    }}

    function pubs{key}Hide() {{
        document.getElementById("pubs{key}List").innerHTML = "";
    }}
    </script>
    <p>\n"""
    return outstr

def collapsableShortWeb(inlist):
    yearlists = {}
    maxitems = 6
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'journal' not in item.keys() and 'booktitle' not in item.keys():
            if 'title' in item.keys():
                outstr = outstr + f"<i>{item['title']}</i>. "
        else:
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'booktitle' in item.keys():
            if 'chapter' in item.keys():
                outstr = outstr + f"Ch. {item['chapter']} "
            outstr = outstr + "<i>In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' in item.keys():
                outstr = outstr + f" {item['number']}"
            outstr = outstr + ". "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        else:
            if 'number' in item.keys():
                outstr = outstr + f"{item['number']}. "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = outstr + f'<a href="{item["url"]}">url: {item["url"]}</a>'
        elif 'isbn' in item.keys():
            outstr = outstr + "In isbn: " + f"{item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',\`{popup_text}\`)">View bib entry</a>\n"""
        if "All" in yearlists.keys():
            if len(yearlists['All']) < maxitems:
                yearlists['All'].append(outstr)
        else:
            yearlists['All'] = [outstr]
    outstr = ""
    for key in yearlists.keys():
        outstr = outstr + f"""    <button onclick="pubs{key}ShortShow()"
        id="pubs{key}ShortButton">
        {key} ({len(yearlists[key])} items)</button>
    </p>
    <p id="pubs{key}ShortList"></p>
    <script>
    var pubs{key}ShortButton = document.getElementById("pubs{key}ShortButton");
    pubs{key}ShortButton.style.cssText = 'width: 100%';
    function pubs{key}ShortShow() {{
        document.getElementById("pubs{key}ShortList").innerHTML = `
    <button onclick="pubs{key}ShortHide()">hide</button><br>
    {"<br><br>".join(yearlists[key])}
    `;
    }}

    function pubs{key}ShortHide() {{
        document.getElementById("pubs{key}ShortList").innerHTML = "";
    }}
    </script>
    <p>\n"""
    return outstr

def collapsableMedWeb(inlist):
    maxitems = 10
    yearlists = {}
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'journal' not in item.keys() and 'booktitle' not in item.keys():
            if 'title' in item.keys():
                outstr = outstr + f"<i>{item['title']}</i>. "
        else:
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + f"<i>{item['journal']}</i>"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'booktitle' in item.keys():
            if 'chapter' in item.keys():
                outstr = outstr + f"Ch. {item['chapter']} "
            outstr = outstr + "<i>In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "</i>"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' in item.keys():
                outstr = outstr + f" {item['number']}"
            outstr = outstr + ". "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        else:
            if 'number' in item.keys():
                outstr = outstr + f"{item['number']}. "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + '<a href="https://doi.org/' +
                      f'{item["doi"]}">doi: {item["doi"]}</a>')
        elif 'url' in item.keys():
            outstr = outstr + f'<a href="{item["url"]}">url: {item["url"]}</a>'
        elif 'isbn' in item.keys():
            outstr = outstr + "In isbn: " + f"{item['isbn']}"
        if 'bib' in item.keys():
            popup_text = item['bib'].replace("\\", "\\\\")
            outstr = outstr + f"""<br><a onclick="window.prompt('Bib entry:',\`{popup_text}\`)">View bib entry</a>\n"""
        if "All" in yearlists.keys():
            if len(yearlists['All']) < maxitems:
                yearlists['All'].append(outstr)
        else:
            yearlists['All'] = [outstr]
    outstr = ""
    for key in yearlists.keys():
        outstr = outstr + f"""    <button onclick="pubs{key}MedShow()"
        id="pubs{key}MedButton">
        {key} ({len(yearlists[key])} items)</button>
    </p>
    <p id="pubs{key}MedList"></p>
    <script>
    var pubs{key}MedButton = document.getElementById("pubs{key}MedButton");
    pubs{key}MedButton.style.cssText = 'width: 100%';
    function pubs{key}MedShow() {{
        document.getElementById("pubs{key}MedList").innerHTML = `
    <button onclick="pubs{key}MedHide()">hide</button><br>
    {"<br><br>".join(yearlists[key])}
    `;
    }}

    function pubs{key}MedHide() {{
        document.getElementById("pubs{key}MedList").innerHTML = "";
    }}
    </script>
    <p>\n"""
    return outstr
