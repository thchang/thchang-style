% BibTeX standard bibliogra:hy style `unsrt'
   % Version 0.99b (8-Dec-10 release) for BibTeX versions 0.99a or later.
   % Copyright (C) 1984, 1985, 1988, 2010 Howard Trickey and Oren Patashnik.
   % Unlimited copying and redistribution of this file are permitted as long as
   % it is unmodified.  Modifications (and redistribution of modified versions)
   % are also permitted, but only if the resulting file is renamed to something
   % besides btxbst.doc, plain.bst, unsrt.bst, alpha.bst, and abbrv.bst.
   % This restriction helps ensure that all standard styles are identical.
   % The file btxbst.doc has the documentation for this style.

ENTRY
  { address
    author
    booktitle
    chapter
    edition
    editor
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    volume
    year
    doi
    isbn
    url
    location
    articleno
    numpages
    subtitle
    language
    github
    version
    agency
    foa
    role
    director
    pi
    copi
    anllead
    length
    budget
  }
  {}
  { label.year extra.label sort.year sort.label }

STRINGS { name }
INTEGERS { output.state before.all mid.sentence after.sentence after.block }

FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.sentence :=
  #3 'after.block :=
  "T.~H. Chang" 'name :=
}

STRINGS { s t }

FUNCTION {output.nonnull}
{ 's :=
  output.state mid.sentence =
    { ", " * write$ }
    { output.state after.block =
        { add.period$ write$
          newline$
          "\newblock " write$
        }
        { output.state before.all =
            'write$
            { add.period$ " " * write$ }
          if$
        }
      if$
      mid.sentence 'output.state :=
    }
  if$
  s
}

FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.nonnull
  if$
}

FUNCTION {output.check}
{ 't :=
  duplicate$ empty$
    { pop$ "empty " t * " in " * cite$ * warning$ }
    'output.nonnull
  if$
}

FUNCTION {output.bibitem}
{ newline$
  "\bibitem[]{" write$
  cite$ write$
  "}" write$
  newline$
  ""
  before.all 'output.state :=
}

FUNCTION {fin.entry}
{ add.period$
  write$
  newline$
}

FUNCTION {fin.entry_nodot}
{ write$
  newline$
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    { after.block 'output.state := }
  if$
}

FUNCTION {new.sentence}
{ output.state after.block =
    'skip$
    { output.state before.all =
        'skip$
        { after.sentence 'output.state := }
      if$
    }
  if$
}

FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}

FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}

FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}

FUNCTION {new.block.checka}
{ empty$
    'skip$
    'new.block
  if$
}

FUNCTION {new.block.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.block
  if$
}

FUNCTION {new.sentence.checka}
{ empty$
    'skip$
    'new.sentence
  if$
}

FUNCTION {new.sentence.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.sentence
  if$
}

FUNCTION {field.or.null}
{ duplicate$ empty$
    { pop$ "" }
    'skip$
  if$
}

FUNCTION {emphasize}
{ duplicate$ empty$
    { pop$ "" }
    { "{" swap$ * "}" * }
  if$
}

INTEGERS { nameptr namesleft numnames }

FUNCTION {format.names}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr "{f.~}{vv~}{ll}{, jj}" format.name$ 't :=
      nameptr #1 >
        { namesleft #1 >
            {
              t name =
                { ", {\bf " * t * "}" * }
                { ", " * t * }
              if$
            }
            { numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                {
                  t name =
                    { " and {\bf " * t * "}" * }
                    { " and " * t * }
                  if$
                }
              if$
            }
          if$
        }
        {
          t name =
            { "{\bf " t * "}" * }
            't
          if$
        }
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {format.devs}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr "{f.~}{vv~}{ll}{, jj}" format.name$ 't :=
      nameptr #1 >
        { namesleft #1 >
            {
              t name =
                { ", {\bf " * t * "}" * }
                { ", " * t * }
              if$
            }
            { numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                {
                  t name =
                    { " and {\bf " * t * "}" * }
                    { " and " * t * }
                  if$
                }
              if$
            }
          if$
        }
        {
          t name =
            { "{\bf " t * "}~(lead)" * }
            't
          if$
        }
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {format.language}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr "{ff~}{vv~}{ll}" format.name$ 't :=
      nameptr #1 >
        { namesleft #1 >
            { ", {\tt " * t * "}" * }
            { numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                { " and {\tt " * t * "}" * }
              if$
            }
          if$
        }
        { "{\tt " t * "}" * }
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {format.authors}
{ author empty$
    { "" }
    { author format.names }
  if$
}

FUNCTION {format.developers}
{ author empty$
    { "" }
    { "\\Devs:~" author format.devs * }
  if$
}

FUNCTION {format.languages}
{ language empty$
    { "" }
    { "$\quad$Primary~Prog.~Lang: " language format.language * }
  if$
}

FUNCTION {format.editors}
{ editor empty$
    { "" }
    { editor format.names
      editor num.names$ #1 >
        { ", editors" * }
        { ", editor" * }
      if$
    }
  if$
}

FUNCTION {format.title}
{ title empty$
    { "" }
    { title "t" change.case$ }
  if$
}

FUNCTION {n.dashify}
{ 't :=
  ""
    { t empty$ not }
    { t #1 #1 substring$ "-" =
        { t #1 #2 substring$ "--" = not
            { "--" *
              t #2 global.max$ substring$ 't :=
            }
            {   { t #1 #1 substring$ "-" = }
                { "-" *
                  t #2 global.max$ substring$ 't :=
                }
              while$
            }
          if$
        }
        { t #1 #1 substring$ *
          t #2 global.max$ substring$ 't :=
        }
      if$
    }
  while$
}

FUNCTION {format.date}
{ year empty$
    { month empty$
        { "" }
        { "there's a month but no year in " cite$ * warning$
          month
        }
      if$
    }
    { month empty$
        'year
        { month " " * year * }
      if$
    }
  if$
}

FUNCTION {format.in.isbn}
{ isbn empty$
    { "" }
    { url empty$
        { "In ISBN: " isbn * }
        { "In ISBN: \href{" url * "}{" * isbn * "}" * }
      if$
    }
  if$
}

FUNCTION {format.isbn}
{ isbn empty$
    { "" }
    { url empty$
        { "ISBN: " isbn * }
        { "ISBN: \href{" url * "}{" * isbn * "}\EatDot" * }
      if$
    }
  if$
}

FUNCTION {format.doi}
{ doi empty$
    { "" }
    { "{\tt doi:~\href{https://doi.org/" doi * "}{" * doi * "}}\EatDot" * }
  if$
}

FUNCTION {format.github}
{ github empty$
    { "" }
    { "\\{\tt git:~\url{https://github.com/" github * "}}\EatDot" * }
  if$
}

FUNCTION {format.version}
{ version empty$
    { "" }
    { "Release:~" version * }
  if$
}

FUNCTION {format.btitle}
{ "{\sl " title * "}" *
}

FUNCTION {format.swtitle}
{ subtitle empty$
    { "{\bf " title * "}" * }
    { "{\bf " title * "}: " * subtitle * }
  if$
}

FUNCTION {tie.or.space.connect}
{ duplicate$ text.length$ #3 <
    { "~" }
    { " " }
  if$
  swap$ * *
}

FUNCTION {either.or.check}
{ empty$
    'pop$
    { "can't use both " swap$ * " fields in " * cite$ * warning$ }
  if$
}

FUNCTION {format.bvolume}
{ volume empty$
    { "" }
    { "Vol." volume tie.or.space.connect
      series empty$
        'skip$
        { " of " * series emphasize * }
      if$
      "Vol. and No." number either.or.check
    }
  if$
}

FUNCTION {format.number.series}
{ volume empty$
    { number empty$
        { series field.or.null }
        { output.state mid.sentence =
            { "No." }
            { "No." }
          if$
          number tie.or.space.connect
        }
      if$
    }
    { "" }
  if$
}

FUNCTION {format.number.article}
{ articleno empty$
    { "" }
    { "Article " articleno * }
  if$
}

FUNCTION {format.edition}
{ edition empty$
    { "" }
    { output.state mid.sentence =
        { edition "l" change.case$ " edition" * }
        { edition "t" change.case$ " edition" * }
      if$
    }
  if$
}

INTEGERS { multiresult }

FUNCTION {multi.page.check}
{ 't :=
  #0 'multiresult :=
    { multiresult not
      t empty$ not
      and
    }
    { t #1 #1 substring$
      duplicate$ "-" =
      swap$ duplicate$ "," =
      swap$ "+" =
      or or
        { #1 'multiresult := }
        { t #2 global.max$ substring$ 't := }
      if$
    }
  while$
  multiresult
}

FUNCTION {format.pages}
{ pages empty$
    {
      numpages empty$
        { "" }
        { numpages " pages" * }
      if$
    }
    { pages multi.page.check
        { "pp." pages n.dashify tie.or.space.connect }
        { "p." pages tie.or.space.connect }
      if$
    }
  if$
}

FUNCTION {format.numpages}
{ numpages empty$
    { "" }
    { numpages " pages" * }
  if$
}

FUNCTION {format.journal.vol.num.pages}
{ journal empty$
    'skip$
    { volume empty$ % field.or.null
        { "{\sl " journal * "}" * }
        { "{\sl " journal * "} " * volume * }
      if$
      number empty$
        'skip$
        { "(" * number * ")" * }
      if$
      articleno empty$
        'skip$
        { ", Article " * articleno * }
      if$
      pages empty$
        { numpages empty$
            'skip$
            { ", " * numpages * " pages" * }
          if$
        }
        { duplicate$ empty$
            { pop$ format.pages }
            { ", pp. " * pages n.dashify * }
          if$
        }
      if$
    }
  if$
}

FUNCTION {format.agency.foa}
{ agency empty$
    { foa empty$
        { "" }
        { "\\FOA: {\sl " foa * "}" * }
      if$
    }  
    { foa empty$
        { "\\Funding Agency: " agency * }
        { "\\FOA: " agency * ", {\sl " * foa * "}" * }
      if$
    }
  if$
  number empty$
    'skip$
    { " (" * number * ")" * }
  if$
}

FUNCTION {format.proposaltype}
{ type empty$
    { "" }
    { "\\Type:~" type * }
  if$
  numpages empty$
    'skip$
    { " (" * numpages * ")" * }
  if$
}

FUNCTION {format.proposalsize}
{ budget empty$
    { "" }
    { "Proposed Budget:~\$" budget * ". " * }
  if$
  length empty$
    'skip$
    { "Proposed Length:~" * length * }
  if$
}

FUNCTION {format.proposalrole}
{ role empty$
    { "" }
    { "\\ \hskip 12pt {\bf Role:~" role * "}" * }
  if$
  director empty$
    'skip$
    { ".$\qquad$ Director:~" * director format.names * }
  if$
  pi empty$
    'skip$
    { ".$\qquad$ PI:~" * pi format.names * }
  if$
  copi empty$
    'skip$
    { " (w/ " * copi format.names * ")" * }
  if$
  anllead empty$
    'skip$
    { ".$\qquad$ ANL~Lead:~" * anllead format.names * }
  if$
}

FUNCTION {format.chapter.pages}
{ chapter empty$
    'format.pages
    { type empty$
        { "chapter" }
        { type "l" change.case$ }
      if$
      chapter tie.or.space.connect
      pages empty$
        'skip$
        { ", " * format.pages * }
      if$
    }
  if$
}

FUNCTION {format.in.ed.booktitle}
{ booktitle empty$
    { "" }
    { editor empty$
        { "In {\sl " booktitle * "}" * }
        { "In " format.editors * " (Ed.), {\sl " * booktitle * "}" * }
      if$
      volume empty$
        'skip$
        { " {\sl " * format.bvolume * "}" * }
      if$
    }
  if$
}

FUNCTION {format.location}
{ location empty$
    { "" }
    { location }
  if$
}

FUNCTION {empty.misc.check}
{ author empty$ title empty$ howpublished empty$
  month empty$ year empty$ note empty$
  and and and and and
    { "all relevant fields are empty in " cite$ * warning$ }
    'skip$
  if$
}

FUNCTION {format.thesis.type}
{ type empty$
    'skip$
    { pop$
      type "t" change.case$
    }
  if$
}

FUNCTION {format.tr.number}
{ type empty$
    { "Technical Report" }
    'type
  if$
  number empty$
    { "t" change.case$ }
    { number tie.or.space.connect }
  if$
}

FUNCTION {format.article.crossref}
{ key empty$
    { journal empty$
        { "need key or journal for " cite$ * " to crossref " * crossref *
          warning$
          ""
        }
        { "In {" journal * "\/}" * }
      if$
    }
    { "In " key * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.crossref.editor}
{ editor #1 "{vv~}{ll}" format.name$
  editor num.names$ duplicate$
  #2 >
    { pop$ " et~al." * }
    { #2 <
        'skip$
        { editor #2 "{vv~}{ll}{ jj}" format.name$ "others" =
            { " et~al." * }
            { " and " * editor #2 "{vv~}{ll}" format.name$ * }
          if$
        }
      if$
    }
  if$
}

FUNCTION {format.book.crossref}
{ volume empty$
    { "empty volume in " cite$ * "'s crossref of " * crossref * warning$
      "In "
    }
    { "Vol." volume tie.or.space.connect
      " of " *
    }
  if$
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { series empty$
            { "need editor, key, or series for " cite$ * " to crossref " *
              crossref * warning$
              "" *
            }
            { "{" * series * "\/}" * }
          if$
        }
        { key * }
      if$
    }
    { format.crossref.editor * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.incoll.inproc.crossref}
{ editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { booktitle empty$
            { "need editor, key, or booktitle for " cite$ * " to crossref " *
              crossref * warning$
              ""
            }
            { "In {" booktitle * "\/}" * }
          if$
        }
        { "In " key * }
      if$
    }
    { "In " format.crossref.editor * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {article}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.journal.vol.num.pages output.nonnull
    }
    { format.article.crossref output.nonnull
      format.pages output
    }
  if$
  new.block
  note output
  new.block
  format.isbn output
  format.doi output
  fin.entry
}

FUNCTION {software}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.swtitle "title" output.check
  new.block
  format.version output
  new.block
  format.developers "devs" output.check
  new.block
  format.languages "lang" output.check
  new.block
  note output
  new.block
  format.github output
  fin.entry
}

FUNCTION {proposal}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.title "title" output.check
  new.block
  format.agency.foa output.nonnull
  new.block
  format.proposaltype output
  new.block
  format.proposalsize output
  new.block
  format.proposalrole output
  new.block
  note output
  fin.entry
}

FUNCTION {book}
{ output.bibitem
  format.date "year" output.check
  new.block
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  new.block
  format.btitle "title" output.check
  crossref missing$
    { format.bvolume output
      new.block
      format.number.series output
      new.sentence
      publisher "publisher" output.check
      address output
    }
    { new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  new.block
  note output
  new.block
  format.isbn output
  fin.entry
}

FUNCTION {booklet}
{ output.bibitem
  format.authors output
  new.block
  format.title "title" output.check
  howpublished address new.block.checkb
  howpublished output
  address output
  format.date output
  new.block
  note output
  new.block
  format.isbn output
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  format.date "year" output.check
  new.block
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  new.block
  format.btitle "title" output.check
  crossref missing$
    { format.bvolume output
      format.chapter.pages "chapter and pages" output.check
      format.number.article output
      new.block
      format.number.series output
      new.sentence
      publisher "publisher" output.check
      address output
    }
    { format.chapter.pages "chapter and pages" output.check
      new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  new.block
  note output
  new.block
  format.in.isbn output
  fin.entry
}

FUNCTION {incollection}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.number.series output
      format.chapter.pages output
      new.sentence
      publisher "publisher" output.check
      address output
      format.edition output
    }
    { format.incoll.inproc.crossref output.nonnull
      format.chapter.pages output
    }
  if$
  new.block
  note output
  new.block
  format.in.isbn output
  fin.entry
}

FUNCTION {inproceedings}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.title "title" output.check
  new.block
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.number.series output
      format.number.article output
      format.pages output
    }
    { format.incoll.inproc.crossref output.nonnull
      format.pages output
    }
  if$
  format.location output
  new.block
  note output
  new.block
  format.in.isbn output
  format.doi output
  fin.entry
}

FUNCTION {conference} { inproceedings }

FUNCTION {manual}
{ output.bibitem
  author empty$
    { organization empty$
        'skip$
        { organization output.nonnull
          address output
        }
      if$
    }
    { format.authors output.nonnull }
  if$
  new.block
  format.btitle "title" output.check
  author empty$
    { organization empty$
        { address new.block.checka
          address output
        }
        'skip$
      if$
    }
    { organization address new.block.checkb
      organization output
      address output
    }
  if$
  format.edition output
  format.date output
  new.block
  note output
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.btitle "title" output.check
  new.block
  "Master's Thesis" format.thesis.type output.nonnull
  new.block
  school "school" output.check
  address output
  new.block
  note output
  fin.entry
}

FUNCTION {misc}
{ output.bibitem
  format.authors output
  new.block
  format.date output
  new.block
  format.title "title" output.check
  new.block
  booktitle output
  address output
  new.block
  howpublished new.block.checka
  howpublished output
  new.block
  note output
  fin.entry
  empty.misc.check
}

FUNCTION {phdthesis}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.btitle "title" output.check
  new.block
  "Ph.D.\ Dissertation" format.thesis.type output.nonnull
  new.block
  school "school" output.check
  address output
  new.block
  note output
  fin.entry
}

FUNCTION {proceedings}
{ output.bibitem
  format.date "year" output.check
  new.block
  editor empty$
    { organization output }
    { format.editors output.nonnull }
  if$
  new.block
  format.btitle "title" output.check
  format.bvolume output
  format.number.series output
  address empty$
    { editor empty$
        { publisher new.sentence.checka }
        { organization publisher new.sentence.checkb
          organization output
        }
      if$
      publisher output
    }
    { address output.nonnull
      new.sentence
      editor empty$
        'skip$
        { organization output }
      if$
      publisher output
    }
  if$
  new.block
  format.isbn output
  note output
  fin.entry
}

FUNCTION {techreport}
{ output.bibitem
  format.date "year" output.check
  new.block
  format.authors "author" output.check
  new.block
  format.btitle "title" output.check
  new.block
  format.tr.number output.nonnull
  new.block
  institution "institution" output.check
  address output
  new.block
  note output
  fin.entry
}

FUNCTION {unpublished}
{ output.bibitem
  format.authors "author" output.check
  format.date output
  new.block
  format.title "title" output.check
  new.block
  note "note" output.check
  fin.entry
}

FUNCTION {default.type} { misc }

MACRO {jan} {"January"}

MACRO {feb} {"February"}

MACRO {mar} {"March"}

MACRO {apr} {"April"}

MACRO {may} {"May"}

MACRO {jun} {"June"}

MACRO {jul} {"July"}

MACRO {aug} {"August"}

MACRO {sep} {"September"}

MACRO {oct} {"October"}

MACRO {nov} {"November"}

MACRO {dec} {"December"}

MACRO {acmcs} {"ACM Computing Surveys"}

MACRO {acta} {"Acta Informatica"}

MACRO {cacm} {"Communications of the ACM"}

MACRO {ibmjrd} {"IBM Journal of Research and Development"}

MACRO {ibmsj} {"IBM Systems Journal"}

MACRO {ieeese} {"IEEE Transactions on Software Engineering"}

MACRO {ieeetc} {"IEEE Transactions on Computers"}

MACRO {ieeetcad}
 {"IEEE Transactions on Computer-Aided Design of Integrated Circuits"}

MACRO {ipl} {"Information Processing Letters"}

MACRO {jacm} {"Journal of the ACM"}

MACRO {jcss} {"Journal of Computer and System Sciences"}

MACRO {scp} {"Science of Computer Programming"}

MACRO {sicomp} {"SIAM Journal on Computing"}

MACRO {tocs} {"ACM Transactions on Computer Systems"}

MACRO {tods} {"ACM Transactions on Database Systems"}

MACRO {tog} {"ACM Transactions on Graphics"}

MACRO {toms} {"ACM Transactions on Mathematical Software"}

MACRO {toois} {"ACM Transactions on Office Information Systems"}

MACRO {toplas} {"ACM Transactions on Programming Languages and Systems"}

MACRO {tcs} {"Theoretical Computer Science"}

READ

FUNCTION {begin.bib}
{ preamble$ empty$
    'skip$
    { preamble$ write$ newline$ }
  if$
  "\begin{thebibliography}{x}" write$ newline$
}

EXECUTE {begin.bib}

EXECUTE {init.state.consts}

ITERATE {call.type$}

FUNCTION {end.bib}
{ newline$
  "\end{thebibliography}" write$ newline$
}

EXECUTE {end.bib}
