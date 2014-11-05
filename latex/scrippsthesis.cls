% \iffalse meta-comment
% 
% scrippsthesis.cls -- Scripps College Senior Thesis LaTeX Class File
% 
% Copyright (C) 2005 Lisa Lambeth, Natalya St. Clair and 
% the Department of Mathematics, Scripps College
%
% Visit http://www.scrippscollege.edu/dept/math/tex.html
% for more details
%
% Adapted from hmcposter.cls by C.M. Connelly
%
% Visit <http://math.hmc.edu/computing/support/tex/classes/hmcthesis/>
% for more details
%
% *** SCRIPPS STUDENTS SHOULD NOT CHANGE THE TYPESETTING PARAMETERS FOR  ***
% *** THEIR THESIS REPORTS.  STUDENTS WISHING TO ADD FEATURES SHOULD ***
% *** DO SO WITH OTHER FILES, NOT BY MODIFYING THIS FILE.            *** 
%
% License:
% 
%   This program is free software; you can redistribute it and/or
%   modify it under the terms of the GNU General Public License as
%   published by the Free Software Foundation; either version 2 of the
%   License, or (at your option) any later version.
%
%   This program is distributed in the hope that it will be useful,
%   but WITHOUT ANY WARRANTY; without even the implied warranty of
%   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%   GNU General Public License for more details. 
%
%   You should have received a copy of the GNU General Public License
%   along with this program; if not, write to the Free Software
%   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
%   02111-1307  USA 
%
% \fi
%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{scrippsthesis}[2005/12/10 Scripps Math Thesis class]

%%% Get some useful information when errors occur.
\setcounter{errorcontextlines}{25}


%%% Load some required/very useful packages.
\RequirePackage{amsmath}
\RequirePackage[psamsfonts]{amsfonts}
\RequirePackage{xspace}
\RequirePackage{verbatim}
\RequirePackage{booktabs}
\RequirePackage{ifthen}
\RequirePackage{graphics}
\RequirePackage{fancyhdr}
%\RequirePackage[options]{natbib}


%%% Set the default typeface via a package.
\RequirePackage{palatino}

%%% Declare and set some options.

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
%\ExecuteOptions{}
\ProcessOptions\relax %% <-- Change this if we decide to declare some
                      %%     options for this class!



%%% Load the book class with some default options.
\LoadClass[11pt,openright, oneside]{book}


%%% Include local configuration file, if any.
\InputIfFileExists{scrippsthesis.cfg}{}{}


%%% Define some environments.
\newenvironment{abstract}{\chapter*{Abstract}%
\addcontentsline{toc}{chapter}{Abstract}}{}

\newenvironment{acknowledgments}{\chapter*{Acknowledgments}%
\addcontentsline{toc}{chapter}{Acknowledgments}}{}


%%% Set the headers and footers.

\setlength{\headheight}{14pt}

\pagestyle{fancy}{%
  \fancyhf{} %% Clear all headers and footers.
 %\fancyhead[LE]{\textbf{\thepage{}}\hspace{1em}\nouppercase\leftmark}
  \fancyhead[LE]{\nouppercase\rightmark\hspace{1em}\textbf{\thepage}}
  \fancyhead[RE]{\chaptername\ \thechapter}
  \fancyhead[LO]{Section \thesection}
  \fancyhead[RO]{\nouppercase\rightmark\hspace{1em}\textbf{\thepage}}
  \fancyfoot{}
}

%%% Redefine the \chaptermark and \sectionmark commands.  Note that
%%%  this redefinition must occur after setting pagestyle to fancy.
\renewcommand{\chaptermark}[1]{%
  \markboth{#1}{}}
\renewcommand{\sectionmark}[1]{%
  \markright{#1}{}}

\addtolength{\headwidth}{.5\marginparsep}
\addtolength{\headwidth}{.5\marginparwidth}

\fancypagestyle{plain}{%
  \fancyhf{} %% Clear all headers and footers.
%  \fancyfoot[LE,RO]{\thepage}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

\fancypagestyle{empty}{%
  \fancyhf{} %% Clear all headers and footers.
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

\fancypagestyle{front}{%
  \fancyhf{} %% Clear all headers and footers.
  \fancyhead[LO]{\nouppercase\leftmark}
  %\fancyhead[RE]{\nouppercase\rightmark\hspace{1em}\textbf{\thepage}}
  \fancyhead[RO]{\nouppercase\rightmark \hspace{1em}\textbf{\thepage}}
}




%%% Define the layout of the title page.

\newcommand{\@sigline}{\vspace{2ex}\hbox to \textwidth{\hrulefill}\hfill}

\renewcommand{\maketitle}{\begin{titlepage}%
      \enlargethispage{1.5in}
      \let\footnotesize\small
      \let\footnoterule\relax
      \let\thanks\ignoreit
      \parindent\z@
      \vspace*{-1in}
      \begin{center}%
      {\scalebox{0.65}{\includegraphics{scripps-logo-green.png}}\par}%
      \vspace{\stretch{1.5}}
      {\LARGE \noindent\@title \par}%
      \vskip 2em
      {\Large
        \let\and\par
        \textbf{\@author}
        \par}%
      \vspace{\stretch{1}}
      {\normalsize
        \def\and{\!, Advisor\par}
        \@advisor, Advisor\par}
      %\vspace{\stretch{.5}}
      {\normalsize
        \def\and{\!, Reader\par}
        \@reader, Reader\par}
      \vspace{\stretch{1.5}}
      {\normalsize
        Submitted to Scripps College in Partial Fulfillment\\
        of the Degree of Bachelor of Arts\par}
      \vspace{\stretch{1.5}}
    {\large \@date\\[1em]
      Department of Mathematics%\\[1em]
%      Department of Economics
        \par}%
\end{center}
                                %\par
    \@thanks
    \vfill\null
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}

%%% Define some commands for specifying information for the title page
%%%  (and other parts of the document).

\def\reader#1{\gdef\@reader{#1}}
\def\@reader{\@latex@warning@no@line{No \noexpand\liaison given}}
\def\advisor#1{\gdef\@advisor{#1}}
\def\@advisor{\@latex@warning@no@line{No \noexpand\advisor given}}



%%% Print only the chapter and section number in the Table of Contents.

\setcounter{tocdepth}{1}

%%% Specify some details about the appearance of the table of contents.


\renewcommand{\tableofcontents}{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\contentsname
        \@mkboth{%
           \contentsname}{\contentsname}}%
    \@starttoc{toc}%
    \if@restonecol\twocolumn\fi
    }




%%% Print only the chapter and section number in the Table of Contents.

\setcounter{tocdepth}{1}


%%% Set Metafont font.  If logo not available, use the second form.
%%%
%%% \font\mffont=logosl10 scaled\magstep1
\let\mffont=\sf

\renewcommand{\frontmatter}{%
    \cleardoublepage
  \@mainmatterfalse
  \pagenumbering{roman}
  \pagestyle{front}}

\renewcommand{\mainmatter}{%
    \cleardoublepage
  \@mainmattertrue
  \pagenumbering{arabic}%
\pagestyle{fancy}}

\renewenvironment{thebibliography}[1]
     {\chapter*{\bibname
        \@mkboth{\bibname}{\bibname}
      \addcontentsline{toc}{chapter}{\bibname}}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\renewcommand\newblock{\hskip .11em\@plus.33em\@minus.07em}
\let\@openbib@code\@empty

\AtBeginDocument{\@ifundefined{bibsection}{}{%
    % Handle natbib
    \let\N@tbibsection\bibsection
    \def\bibsection{\N@tbibsection\addcontentsline{toc}{chapter}{\bibname}}%
}}

\renewenvironment{theindex}
               {\if@twocolumn
                  \@restonecolfalse
                \else
                  \@restonecoltrue
                \fi
                \columnseprule \z@
                \columnsep 35\p@
                \twocolumn[\@makeschapterhead{\indexname}]%
                \@mkboth{\indexname}%
                        {\indexname}%
                        \addcontentsline{toc}{chapter}{\indexname}%
                \thispagestyle{plain}\parindent\z@
                \parskip\z@ \@plus .3\p@\relax
                \let\item\@idxitem}
               {\if@restonecol\onecolumn\else\clearpage\fi}


%%% Fix \cleardoublepage so it doesn't put headers on pages that are
%%% supposed to be blank.

\renewcommand*{\cleardoublepage}{%
% original definition, see latex.ltx
  \clearpage
  \if@twoside
     \ifodd\c@page
  \else
     \thispagestyle{empty}% added
     \hbox{}\newpage
     \if@twocolumn
        \hbox{}\newpage
     \fi
     \fi
  \fi
}

%% Ragged bottom is better than the alternative...

\raggedbottom



