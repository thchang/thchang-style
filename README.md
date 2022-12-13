# thchang-style -- Steal my CV/Website style

Source code to automatically generate a responsive academic website and CV
from ``.bib`` files of publications and past talks and ``.yaml`` files
of past research experience, students, activities, research ideas, etc.

## The Story

This started out as a customized ``.bst`` files (see ``styles/cv.bst``)
for building my CV from bib entries.
Then I started storing everything in ``.bib`` files, and creating weird bib
entries in my ``cv.bst`` file to handle increasingly bazaar document types.

Eventually I realized it would be better to automate website maintenance
as well.
But this requires increased flexibility, and a lot of Python scripts.

Eventually I realized I needed to store certain items (such as work experience,
awards, degree, collaborators, and fun links) in some other format.
I was inspired to use YAML after stumbling across Brandon Amos's CV:
  https://github.com/bamos/cv

## Usage

Using this project requires

 - ``pdflatex``,
 - GNU Make,
 - Python 3, and
 - Matplotlib.

After you have all dependencies, create a copy of the info folder with your
personal information in it.

Then, create a template for each of your CV and Website, by modifying either
of the ``cv.template`` or ``web.template`` files.

Update the ``Makefile`` to point to your preferred installation and
build directories.
Make sure the ``Makefile`` also is aware of any image files or other
dependencies for your website, or make sure that they are already saved in
the build directory.

Create additional rules if you have multiple versions (i.e., a long and short
CV).

Then use the ``make`` command to build everything.

See my website repo for an example of how I use this:
  https://github.com/thchang/thchang.github.io
