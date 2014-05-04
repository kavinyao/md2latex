# Markdown to \LaTeX Test Document

- author: Kavin Yao <kavinyao@gmail.com>

---

# Why I Do This

I love \LaTeX for its pretty typesetting, but not like its verbose syntax very much. 95\% of the time, I only use a very small subset of \LaTeX and really miss the simplicity of markdown every time I have to type in plain \LaTeX.

I also use [TeXmacs](http://www.texmacs.org/tmweb/home/welcome.en.html). Its a great tool and I love it. However, the source code of TeXmacs documents, with an XML-like structure, is not human-readable. It's not good for source control, either.

So, my conclusion is that, since what I mostly use in \LaTeX can be mapped to markdown, why not write document in markdown and convert it to \LaTeX? I find [Pandoc][pandoc] but it's too cryptic to use[^note1].

[pandoc]: http://johnmacfarlane.net/pandoc/
[^note1]: Pandoc is too omnipotent and lack the simplicity I prefer.

And an idea bubbles up in my head: why not write my own converter from markdown to \LaTeX?

I have a great start point: [mistune](https://github.com/lepture/mistune). It's a fast, clean implementation of markdown with a killer feature - footnote. I tend to use footnote much in \LaTeX.

## Plan

My current plan of the converter includes:

- title and author (with meta header)
- sections (headers in markdown)
- lists (ordered with `enumerate` and unordered with `itemize` package)
- emphasize, strong and monospace styles
- hyperlink
- footnote
- math[^math]

[^math]: since there's no inline math in markdown, it is translated as is.

Now let's see how much we can do...
