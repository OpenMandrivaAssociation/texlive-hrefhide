Name:		texlive-hrefhide
Version:	66189
Release:	1
Summary:	Suppress hyper links when printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hrefhide
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the command \hrefdisplayonly (which
provides a substitute for \href). While the (hyperlinked) text
appears like an ordinary \href in the compiled PDF file, the
same text will be "hidden" when printing the text. (Hiding is
actually achieved by making the text the same colour as the
background, thus preserving the layout of the rest of the
text.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hrefhide/hrefhide.sty
%doc %{_texmfdistdir}/doc/latex/hrefhide/README
%doc %{_texmfdistdir}/doc/latex/hrefhide/hrefhide-example.pdf
%doc %{_texmfdistdir}/doc/latex/hrefhide/hrefhide-example.tex
%doc %{_texmfdistdir}/doc/latex/hrefhide/hrefhide.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hrefhide/hrefhide.drv
%doc %{_texmfdistdir}/source/latex/hrefhide/hrefhide.dtx
%doc %{_texmfdistdir}/source/latex/hrefhide/hrefhide.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
