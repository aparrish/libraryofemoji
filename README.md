#Library of Emoji

This repository contains a Python program, `generate.py`, which I made to
generate the speculative emoji names seen on
[@libraryofemoji](http://twitter.com/libraryofemoji). Also included are several
data files containing large numbers of lemmas from
[WordNet](http://wordnet.princeton.edu/), categorized by part of speech. (These
lemmas are drawn from randomly to fill the structural backbone generated by
`generate.py`).

If you'd like to turn the output of this program (or similar output), into a
Twitter bot, I recommend
[everywordbot](https://github.com/aparrish/everywordbot), which is a Python
program I wrote to tweet, in succession, lines from a text file.

##Requirements

You'll need [Python](http://www.python.org/), of course, and you'll also need
[Pattern](http://www.clips.ua.ac.be/pattern), which you can install with `pip`
like so:

	$ pip install pattern

(Pattern is only used for its `pluralize` function.)

##Usage

After installing the required libraries, run the Python script from the
command-line like so:

	$ python generate.py | more

The `| more` is important, since the script will print an infinite number of
randomly generated emoji names to standard output until you hit `^C`. You can
generate a particular number of emoji names using `head`:

	$ python generate.py | head -1000 >emoji_names.txt

Note: For [@libraryofemoji](http://twitter.com/libraryofemoji), I filtered the
results of running this script with Darius Kazemi's
[wordfilter](https://github.com/dariusk/wordfilter) (which is also available
for Python as part of Leonard Richardson's
[olipy](https://github.com/leonardr/olipy) library), in order to remove
anything obviously unseemly. You might want to do the same!

##License

The (MIT) license for the Python code is included in `LICENSE`. A different
license covers the text files from WordNet; that license is included as
`LICENSE_wordnet`.

