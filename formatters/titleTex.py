def titleTex(inlist):
    outstr = []
    for item in inlist:
        if 'name' not in item.keys():
            raise ValueError(f"title data does not contain a name field")
        outstr.append("{\\huge \\bf ")
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
        for key in item['links']:
            if len(contact) < len(institution):
                contact.append(f"{key}: \\url{{{item['links'][key]}}}")
        while len(contact) < len(institution):
            contact.append("")
        for infi, ci in zip(institution, contact):
            outstr.append("\\tabboxlarge{" + f"{infi}" + "}" + f"{ci}\\\\\n")
    return "".join(outstr)
