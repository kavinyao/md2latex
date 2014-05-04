import sys
import mistune

def newline(func):
    def inner(*args, **argv):
        return '\n\n%s' % func(*args, **argv)

    return inner

class MyRenderer(mistune.Renderer):
    FOOTNOTE = 'FTNT-MAGIC'

    use_block_quote = False
    use_enumerate = False
    use_hyperref = False

    def __init__(self):
        self.footnotes_ = {}

    def not_support(self, feature):
        raise NotImplemented('%s is not supported yet.' % feature)

    def block_code(self, code, lang=None):
        """Ref: http://scott.sherrillmix.com/blog/programmer/displaying-code-in-latex/"""
        code = code.rstrip()
        return '\\begin{verbatim}%s\n\\end{verbatim}' % code

    def block_quote(self, text):
        """Ref: http://tex.stackexchange.com/a/4970/43978"""
        return '\\blockquote{%s}' % text

    def block_html(self, html):
        self.not_support('Block HTML')

    @newline
    def header(self, text, level, raw=None):
        if level > 3:
            self.not_support('Header > 3')

        section = ('sub'*(level-1)) + 'section'
        return '\\%s %s' % (section, text)

    @newline
    def hrule(self):
        """Ref: http://tex.stackexchange.com/a/17126/43978"""
        return r'\noindent\rule{\textwidth}{0.4mm}'

    @newline
    def list(self, body, ordered=True):
        if ordered:
            self.use_enumerate = True
            return '\\begin{enumerate}\n%s\\end{enumerate}' % body
        else:
            return '\\begin{itemize}\n%s\\end{itemize}' % body

    def list_item(self, text):
        return '    \\item %s\n' % text

    @newline
    def paragraph(self, text):
        return '%s' % text

    def table(self, header, body):
        self.not_support('Table')

    def table_row(self, content):
        self.not_support('Table')

    def table_cell(self, content):
        self.not_support('Table')

    def double_emphasis(self, text):
        """Ref: http://tex.stackexchange.com/q/14667/43978"""
        return '\\textbf{%s}' % text

    def emphasis(self, text):
        return '\\emph{%s}' % text

    def codespan(self, text):
        return '\\texttt{%s}' % text

    def linebreak(self):
        return r'\\'

    def strikethrough(self, text):
        self.not_support('Strike-through text')

    def autolink(self, link, is_email=False):
        self.use_hyperref = True

        if is_email:
            return r'\href{mailto:%s}{%s}' % (link, link)
        else:
            return r'\url{%s}' % link

    def link(self, link, title, text):
        if 'javascript:' in link:
            # for safety
            return ''

        self.use_hyperref = True

        # title is ignored
        return r'\href{%s}{%s}' % (link, text)

    def image(self, src, title, text):
        self.not_support('Image')

    def raw_html(self, html):
        self.not_support('Inline HTML')

    def footnote_ref(self, key, index):
        # content will be patched later
        return '\\footnote{%s-%s}' % (self.FOOTNOTE, key)

    def footnote_item(self, key, text):
        # store footnotes for patch
        self.footnotes_[key] = text
        # return empty string as output
        return ''

    def footnotes(self, text):
        # return empty string as output
        return ''

md = mistune.Markdown(renderer=MyRenderer())

with open(sys.argv[1]) as f:
    print md.render(f.read())

