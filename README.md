# md2latex

A lame Markdown to LaTeX converter.

See `test.md` for an example and run `python md2latex.py test.md > test.tex` to taste a flavor of it.

## Features

- title
- author(s)
- headings (converted to sections)
- lists (converted to enumerate/itemize)
- emphasis, strong and monospace text style
- hyperlink (using `hyperref` package)
- footnote (in mistune syntax)

## Caveats

You can inline LaTeX commands because they are not markdown-parsable. However, md2latex doesn't do auto-escaping for you so if you have underscore LaTeX meta chracters such as \_ or % in your document, be cautious!

## Acknowledgement

Thanks @lepture for the super awersome [mistune](https://github.com/lepture/mistune) markdown parser.
