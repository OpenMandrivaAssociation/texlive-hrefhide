# revision 22255
# category Package
# catalog-ctan /macros/latex/contrib/hrefhide
# catalog-date 2011-04-29 14:22:52 +0200
# catalog-license lppl1.3
# catalog-version 1.0f
Name:		texlive-hrefhide
Version:	1.0f
Release:	11
Summary:	Suppress hyper links when printing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hrefhide
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrefhide.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0f-2
+ Revision: 752585
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0f-1
+ Revision: 718623
- texlive-hrefhide
- texlive-hrefhide
- texlive-hrefhide
- texlive-hrefhide

