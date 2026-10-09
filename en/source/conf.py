# conf.py for Sphinx + LaTeX + PDF

import os
import sys
from docutils import nodes

# -- Project information -----------------------------------------------------

project = 'JAKA AL Series Hardware User Manual'
copyright = ' 2026, JAKA Robotics'
author = 'JAKA'
release = 'V02'

# -- Substitution ------------------------------------------------------------

rst_epilog = """
.. |product_name| replace:: AL Series
.. |company_name| replace:: JAKA
.. |jaka_app| replace:: Coboπ

"""

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = [
    'Electrical Connections of the Control Cabinet.rst',
    'Initial Start-Up.rst',
    'Control Cabinet Installation.rst',
    'Control Stick Buttons.rst',
    'Electrical Specifications.rst',
]

language = 'en'
locale_dirs = []
master_doc = 'index'

# Keep English quotation marks as typed in the source.  Without this,
# Docutils converts straight quotes/apostrophes to Unicode smart quotes,
# which xeCJK then treats as CJK punctuation in the PDF build.
smartquotes = False

# 自动编号
numfig = True
numfig_secnum_depth = 1

# -- HTML -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/Logo.png'
html_show_sphinx = False
html_show_sourcelink = False
html_copy_source = False

html_css_files = [
    'custom.css',
]

numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s'
}

html_search_language = 'en'

# Production manuals do not load the legacy comment widget.
html_js_files = []

# 查找图片偏好
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/png', 'image/jpeg']

# -- LaTeX -------------------------------------------------

latex_engine = 'xelatex'

latex_documents = [
    ('index', 'JAKA_AL_Series_Hardware_User_Manual.tex', 'JAKA AL Series Hardware User Manual', author, 'manual'),
]

# standard 样式会生成全部横线和竖线；longtable 仍由 list-table 的
# :class: longtable 按需启用。booktabs 会主动省略竖线，不能满足全框线要求。
latex_table_style = ['standard']

latex_elements = {

    'papersize': 'a4paper',
    'pointsize': '11pt',

    'figure_align': 'H',

    # 使用非 .tex 扩展名，避免 Read the Docs 的 latexmk 把封面误认为
    # 第二个主文档（latexmk + -jobname 要求构建目录中只有一个 .tex）。
    'maketitle': r'\input{cover.inc}',
    
    # 恢复原状，去除会导致??的锚点
    'atendofbody': r'''
    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{List of Figures}
    \begingroup
    \hypersetup{allcolors=black}
    \listoffigures
    \endgroup

    \cleardoublepage
    \phantomsection
    \addcontentsline{toc}{chapter}{List of Tables}
    \begingroup
    \hypersetup{allcolors=black}
    \listoftables
    \endgroup

    % Use the last numbered page as the footer total; the back cover has no footer.
    \phantomsection
    \label{LastNumberedPage}

    \cleardoublepage
    \input{backcover.inc}
    ''',

    'fncychap': r'\usepackage[Sonny]{fncychap}',

    'extraclassoptions': 'openany,oneside',

    'preamble': r'''

\usepackage{longtable}
\usepackage{booktabs}    

% ===== 中文支持 =====
\usepackage{xeCJK}
\usepackage[fontset=none]{ctex}

% ===== PDF 正文字体 =====

% 英文字体：
% Windows 本地使用 Arial；
% Read the Docs/Linux 使用 Liberation Sans。
\IfFontExistsTF{Arial}{
    \setmainfont{Arial}[
        UprightFont = Arial,
        BoldFont = Arial Bold,
        ItalicFont = Arial Italic,
        BoldItalicFont = Arial Bold Italic
    ]
}{
    \setmainfont{Liberation Sans}[
        UprightFont = Liberation Sans,
        BoldFont = Liberation Sans Bold,
        ItalicFont = Liberation Sans Italic,
        BoldItalicFont = Liberation Sans Bold Italic
    ]
}

% 中文字体：
% 本地存在思源宋体文件时直接加载；
% Read the Docs 使用系统安装的 Noto Serif CJK SC。
\IfFileExists{C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/SourceHanSerifCN-Regular.ttf}{
    \setCJKmainfont{SourceHanSerifCN}[
        Path = C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/,
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf,
        ItalicFont = *-Regular.ttf,
        BoldItalicFont = *-Bold.ttf,
        ItalicFeatures = {FakeSlant=0.2},
        BoldItalicFeatures = {FakeSlant=0.2}
    ]
    \setCJKsansfont{SourceHanSerifCN}[
        Path = C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/,
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf
    ]
    \setCJKmonofont{SourceHanSerifCN}[
        Path = C:/Users/JAKA/AppData/Local/Microsoft/Windows/Fonts/,
        UprightFont = *-Regular.ttf,
        BoldFont = *-Bold.ttf
    ]
}{
    \setCJKmainfont{Noto Serif CJK SC}[
        UprightFont = Noto Serif CJK SC,
        BoldFont = Noto Serif CJK SC Bold,
        AutoFakeSlant = 0.2
    ]
    \setCJKsansfont{Noto Sans CJK SC}[
        UprightFont = Noto Sans CJK SC,
        BoldFont = Noto Sans CJK SC Bold
    ]
    \setCJKmonofont{Noto Sans Mono CJK SC}[
        UprightFont = Noto Sans Mono CJK SC,
        BoldFont = Noto Sans Mono CJK SC Bold
    ]
}

% Arial/Liberation Sans 可能不包含这两个组合字符。
\XeTeXcharclass"2103=1 % ℃
\XeTeXcharclass"2109=1 % ℉

% ===== 页面边距与页眉空间分配 =====
\usepackage{geometry}
\geometry{
    left=14.5mm,
    right=14.5mm,
    top=24mm,
    bottom=20mm,
    headheight=25pt, % 留足页眉高度
    headsep=4mm,
    footskip=7mm
}

% ===== 图片路径 =====
\graphicspath{{images/}}

% ===== 禁止图表浮动 =====
\usepackage{float}
\usepackage{placeins}

\makeatletter
\def\fps@figure{H}
\def\fps@table{H}
\def\fps@sphinxfigure{H}
\def\fps@sphinxTable{H}
\makeatother

% ==== 强制图片后换行 ===
\usepackage{etoolbox}
\AtEndEnvironment{figure}{\par\noindent}
\AtEndEnvironment{sphinxfigure}{\par\noindent}

% ===== 代码高亮 =====
\usepackage{listings}

% ===== PDF书签 =====
\usepackage{bookmark}

% ===== 自定义变量 =====
\newcommand{\docversion}{''' + release + r'''}
\newcommand{\docname}{''' + project + r'''}

% ===== 页眉页脚 =====
\usepackage{fancyhdr}

% 1. 重定义 Sphinx 的正文页样式 (normal)
\fancypagestyle{normal}{
    \fancyhf{}  
    \fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}}  
    \fancyfoot[L]{Version: \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastNumberedPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt} 
    \renewcommand{\footrulewidth}{0.4pt}
}

% 2. 重定义 Sphinx 的章节起始页样式 (plain)
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}} 
    \fancyfoot[L]{Version: \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastNumberedPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}   
    \renewcommand{\footrulewidth}{0.4pt}
}

% Front matter displays only its current Roman page number.
\fancypagestyle{frontmatter}{
    \fancyhf{}
    \fancyhead[L]{\raisebox{0.05cm}{\includegraphics[height=0.5cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}}
    \fancyfoot[L]{Version: \docversion}
    \fancyfoot[C]{\thepage}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% ===== 标题样式 =====
\usepackage{titlesec}
\usepackage{xcolor}

% chapter 至 subparagraph 共六级标题均显示编号。
\setcounter{secnumdepth}{5}

% 定义红色
\definecolor{TitleRed}{HTML}{D80C1E}

% 章节间距
\titlespacing*{\chapter}{0pt}{-30pt}{20pt}

% Chapter
\titleformat{\chapter}
{\Huge\bfseries\color{TitleRed}}
{\thechapter}{0.5em}{}

% Section
\titleformat{\section}
{\Large\bfseries\color{TitleRed}}
{\thesection}{0.5em}{}

% Subsection
\titleformat{\subsection}
{\large\bfseries\color{TitleRed}}
{\thesubsection}{0.5em}{}

% Subsubsection
\titleformat{\subsubsection}
{\normalsize\bfseries\color{TitleRed}}
{\thesubsubsection}{0.5em}{}

% ===== 超链接颜色 =====
\usepackage{hyperref}

\hypersetup{
colorlinks=true,
linkcolor=blue,
urlcolor=blue,
citecolor=blue
}

% ===== Main table of contents =====
\renewcommand{\sphinxtableofcontents}{
    \cleardoublepage
    \pagenumbering{Roman}
    \pagestyle{frontmatter}
    \begingroup
      \parskip=0pt
      \hypersetup{linkcolor=black}
      \tableofcontents
    \endgroup
    \clearpage
    \pagenumbering{arabic}
    \pagestyle{normal}
}

\makeatletter
\renewcommand{\tableofcontents}{%
    \phantomsection
    \markboth{\contentsname}{\contentsname}%
    \begin{center}
      {\Huge\bfseries\color{TitleRed}\contentsname\par}
    \end{center}
    \vspace{1.5em}
    \@starttoc{toc}%
}
\renewcommand{\@pnumwidth}{2.2em}
\renewcommand{\@tocrmarg}{3.2em}
\newcommand*\JAKAdottedtocline[5]{%
  \ifnum #1>\c@tocdepth\relax\else
    \vskip \z@ \@plus.2\p@
    {\leftskip #2\relax
     \rightskip \@tocrmarg
     \parfillskip -\rightskip
     \parindent \z@
     \@afterindenttrue
     \interlinepenalty\@M
     \leavevmode
     \@tempdima #3\relax
     \advance\leftskip \@tempdima
     \null\nobreak\hskip -\@tempdima
     {#4}\nobreak
     \leaders\hbox{$\m@th
        \mkern \@dotsep mu\hbox{.}\mkern \@dotsep mu$}\hfill
     \nobreak
     \hb@xt@\@pnumwidth{\hfil\normalfont\normalcolor #5}%
     \par}%
  \fi
}
\renewcommand*\l@chapter[2]{%
  \addvspace{0.6em}%
  \begingroup
    \bfseries
    \@dottedtocline{0}{0em}{2.8em}{#1}{#2}%
  \endgroup
}
\renewcommand*\l@section[2]{\JAKAdottedtocline{1}{1.8em}{3.2em}{#1}{#2}}
\renewcommand*\l@subsection[2]{\JAKAdottedtocline{2}{5.0em}{4.2em}{#1}{#2}}
\renewcommand*\l@subsubsection[2]{\JAKAdottedtocline{3}{9.2em}{5.0em}{#1}{#2}}
\renewcommand*\l@figure{\@dottedtocline{1}{1.5em}{3em}}
\renewcommand*\l@table{\@dottedtocline{1}{1.5em}{3em}}
\makeatother

% 2. 图目录
\let\origlistoffigures\listoffigures
\renewcommand{\listoffigures}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoffigures
    \endgroup
}

% 3. 表目录
\let\origlistoftables\listoftables
\renewcommand{\listoftables}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoftables
    \endgroup
}

% ===== 表格样式 =====
\usepackage{colortbl}
\usepackage{longtable}

% 表头 #D80C1E；边框 #9E9E9E、0.75 pt。
\definecolor{tableheader}{HTML}{D80C1E}
\definecolor{tableborder}{HTML}{9e9e9e}
\setlength{\arrayrulewidth}{0.75pt}
\arrayrulecolor{tableborder}

% Sphinx 会在每个表头单元格开头调用此命令。使用 cellcolor 比在
% varwidth 内调用 rowcolor 稳定，并且兼容 tabulary 与 longtable。
\renewcommand{\sphinxstyletheadfamily}{%
  \cellcolor{tableheader}\color{white}\bfseries%
}

% ===== 表格跨页与宽度控制 =====
\usepackage{tabularx}
\usepackage{ltablex}
\keepXColumns

% 表格自动换行
\renewcommand{\tabularxcolumn}[1]{m{#1}}

% 表格不要超出页边距
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}

% ===== 代码块分页优化 =====
\sphinxsetup{
verbatimwithframe=false,
div.note_box-decoration-break=clone,
div.hint_box-decoration-break=clone,
div.important_box-decoration-break=clone,
div.tip_box-decoration-break=clone,
div.warning_box-decoration-break=clone,
div.caution_box-decoration-break=clone,
div.attention_box-decoration-break=clone,
div.danger_box-decoration-break=clone,
div.error_box-decoration-break=clone
}

% ===== Figure and table names =====
\AtBeginDocument{
    \renewcommand{\figurename}{Figure}
    \renewcommand{\tablename}{Table}
    \renewcommand{\listfigurename}{List of Figures}
    \renewcommand{\listtablename}{List of Tables}
    
}

''',
}

latex_additional_files = [
    '_static/cover.inc',
    '_static/backcover.inc',
    '_static/Logo.png',
    '_static/官网二维码.png',
    '_static/AL系列机器人.png',
]

latex_keep_old_macro_names = True
latex_use_xindy = False
latex_toplevel_sectioning = 'chapter'

latex_elements.update({
    'releasename': 'Version',
})

# -- todo extension ---------------------------------------

todo_include_todos = True

# -- autodoc ----------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Automatic merging of empty table cells -------------------------------

def _table_entry_is_empty(entry):
    """Return True only when an entry has no image and no visible text."""
    if any(entry.findall(nodes.image)):
        return False
    return not entry.astext().strip()


def _merge_empty_cells_horizontally(rows, grid, column_count):
    """Merge empty entries into the nearest non-empty entry on the left.

    An entry that already spans rows cannot be extended horizontally because
    doing so could create an L-shaped region that HTML can represent but LaTeX
    tables cannot represent reliably.
    """
    for row_index, row in enumerate(rows):
        anchor = None
        for column in range(column_count):
            cell = grid[row_index][column]
            if cell is None:
                anchor = None
                continue
            if (_table_entry_is_empty(cell) and anchor is not None
                    and not anchor.get('morerows', 0)):
                anchor['morecols'] = int(anchor.get('morecols', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = None if _table_entry_is_empty(cell) else cell


def _merge_empty_cells_vertically(rows, grid, column_count):
    """Merge empty entries into the nearest non-empty entry above.

    An entry that already spans columns is not extended vertically, preventing
    non-rectangular merged regions.
    """
    for column in range(column_count):
        anchor = None
        for row_index, row in enumerate(rows):
            cell = grid[row_index][column]
            if cell is None:
                anchor = None
                continue
            if (_table_entry_is_empty(cell) and anchor is not None
                    and not anchor.get('morecols', 0)):
                anchor['morerows'] = int(anchor.get('morerows', 0)) + 1
                row.remove(cell)
                grid[row_index][column] = None
            else:
                anchor = (
                    None
                    if _table_entry_is_empty(cell) or cell.get('morecols', 0)
                    else cell
                )


def _merge_empty_cells_in_table(table, logger):
    """Safely merge empty entries in a regular table grid.

    The default remains horizontal-first for compatibility with specification
    tables whose unused model columns are intentionally merged. Add the class
    ``merge-empty-vertical`` to grouped tables whose blank category cells must
    extend the category above them. ``merge-empty-horizontal`` can be used to
    state the default explicitly.
    """
    tgroup = next(
        (child for child in table.children if isinstance(child, nodes.tgroup)),
        None,
    )
    if tgroup is None:
        return

    entries = list(tgroup.findall(nodes.entry))
    if any(entry.get('morerows', 0) or entry.get('morecols', 0)
           for entry in entries):
        logger.warning(
            'Automatic empty-cell merging skipped: the table already contains '
            'row or column spans.',
            location=table,
        )
        return

    tbody = next(
        (child for child in tgroup.children if isinstance(child, nodes.tbody)),
        None,
    )
    if tbody is None:
        return

    rows = [child for child in tbody.children if isinstance(child, nodes.row)]
    if not rows:
        return

    column_count = int(tgroup.get('cols', 0)) or max(
        len(row.children) for row in rows
    )
    if any(len(row.children) != column_count for row in rows):
        logger.warning(
            'Automatic empty-cell merging skipped: the table is not a regular '
            'rectangular grid.',
            location=table,
        )
        return

    # Preserve original coordinates; removed entries are represented by None.
    grid = [list(row.children) for row in rows]

    if 'merge-empty-vertical' in table.get('classes', []):
        _merge_empty_cells_vertically(rows, grid, column_count)
        _merge_empty_cells_horizontally(rows, grid, column_count)
    else:
        _merge_empty_cells_horizontally(rows, grid, column_count)
        _merge_empty_cells_vertically(rows, grid, column_count)


def _merge_empty_table_cells(app, doctree, docname):
    """Transform table nodes immediately before HTML or LaTeX output."""
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    for table in list(doctree.findall(nodes.table)):
        # Ordinary tabulary tables cannot split across pages.  Use longtable
        # consistently for LaTeX so long tables continue on the next page.
        if app.builder.format == 'latex':
            classes = table.setdefault('classes', [])
            if 'longtable' not in classes:
                classes.append('longtable')

        # A table can opt out with ``:class: no-auto-merge``.
        if 'no-auto-merge' not in table.get('classes', []):
            _merge_empty_cells_in_table(table, logger)


# -- 自定义 ------------------------------------------------

def setup(app):
    app.connect('doctree-resolved', _merge_empty_table_cells)
    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

latex_elements['utf8extra'] = ''
