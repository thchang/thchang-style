def titleTex(inlist):
    outstr = []
    for item in inlist:
        if 'name' not in item.keys():
            raise ValueError(f"title data does not contain a name field")
        outstr.append("{\\huge ")
        outstr.append(item['name'])
        outstr.append("}\n\n\\medskip\n\n")
        institution = []
        if 'institution' in item.keys():
            institution.append(item['institution'])
            if 'department' in item.keys():
                institution.append(item['department'])
            if 'address' in item.keys():
                institution.append(item['address'])
        contact = []
        email = False
        website = False
        github = False
        if "email" in item.keys():
            contact.append(f"E-mail: \\href{{mailto:{item['email']}}}{{{item['email']}}}")
        if "website" in item.keys():
            contact.append(f"Website: \\url{{{item['website']}}}")
        if "links" in item.keys():
            for key in item['links']:
                if len(contact) < len(institution):
                    contact.append(f"{key}: \\url{{{item['links'][key]}}}")
        while len(contact) < len(institution):
            contact.append("")
        for infi, ci in zip(institution, contact):
            outstr.append("\\tabboxlarge{" + f"{infi}" + "}" + f"{ci}\\\\\n")
    return "".join(outstr)


def titleLualatex(inlist):
    outstr = []
    for item in inlist:
        if 'name' not in item.keys():
            raise ValueError(f"title data does not contain a name field")
        outstr.append(f"\n\\name{{{item['name']}}}{{ -- CV}}\n")
        institution = []
        if 'institution' in item.keys():
            if 'department' in item.keys():
                institution.append(item['department'])
            institution.append(item['institution'])
        outstr.append(f"\\tagline{{{', '.join(institution)}}}\n")
        outstr.append("\\socialinfo{\n")
        if "email" in item.keys():
            outstr.append(f"\t\\email{{{item['email']}}}\n")
        if 'address' in item.keys():
            outstr.append(f"\t\\address{{{item['address']}}}\\\\\n")
        if "website" in item.keys():
            outstr.append(f"\t\\website{{{item['website']}}}" +
                          f"{{{item['website']}}}")
        if 'links' in item.keys():
            for key in item['links']:
                if key.lower().strip() in ["github", "git hub", "git"]:
                    outstr.append(f"\n\t\\github{{{item['links'][key]}}}")
        outstr.append("\n}\n\n\\makecvheader\n\n")
        outstr.append("\\makecvfooter\n\t\\today\n")
        if 'alias' in item.keys():
            outstr.append(f"\t{{{item['alias'][0].replace(' ', '~')} - CV}}\n")
        else:
            outstr.append(f"\t{{{item['name'].replace(' ', '~')} - CV}}\n")
        outstr.append("\t{\\thepage}\n")
    return "".join(outstr)
