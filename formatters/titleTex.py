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
        for i in range(len(institution)):
            if not email and 'email' in item.keys():
                contact.append("E-mail: \\href{mailto:" +
                               f"{item['email']}" + "}{"
                               f"{item['email']}" + "}")
                email = True
            elif not website and 'website' in item.keys():
                contact.append("Website: \\url{" +
                               f"{item['website']}" + "}")
                website = True
            elif not github and 'github' in item.keys():
                contact.append("GitHub: \\url{" +
                               f"{item['github']}" + "}")
                github = True
            else:
                contact.append("")
        for infi, ci in zip(institution, contact):
            outstr.append("\\tabboxlarge{" + f"{infi}" + "}" + f"{ci}\\\\\n")
    return "".join(outstr)
