%global tl_name hrefhide
%global tl_revision 73641

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	Suppress hyper links when printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hrefhide
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the command \hrefdisplayonly (additionally to
\href provided by the hyperref package). While the (hyperlinked) text
appears like an ordinary \href in the compiled pdf-file, the same text
will be "hidden" when printing the text. Hiding is actually achieved by
making the text the same colour as the background, thus preserving the
layout of the rest of the text. Further the commands \hycon and \hycoff
(hyper-colour-on/off) can be used to simulate switching option
ocgcolorlinks of the hyperref package on and off. This package is
possibly obsolete, see section 3: "Alternatives" in the documentation.

