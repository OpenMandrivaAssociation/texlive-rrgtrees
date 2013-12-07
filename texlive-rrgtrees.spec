# revision 27322
# category Package
# catalog-ctan /macros/latex/contrib/rrgtrees
# catalog-date 2012-02-10 18:28:55 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-rrgtrees
Version:	1.1
Release:	4
Summary:	Linguistic tree diagrams for Role and Reference Grammar (RRG) with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rrgtrees
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rrgtrees.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rrgtrees.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rrgtrees.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of LaTeX macros that makes it easy to produce linguistic
tree diagrams suitable for Role and Reference Grammar (RRG).
This package allows the construction of trees with crossing
lines, as is required by this theory for many languages. There
is no known limit on number of tree nodes or levels. Requires
the pst-node and pst-tree LaTeX packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rrgtrees/rrgtrees.sty
%doc %{_texmfdistdir}/doc/latex/rrgtrees/Makefile
%doc %{_texmfdistdir}/doc/latex/rrgtrees/README
%doc %{_texmfdistdir}/doc/latex/rrgtrees/rrgtrees.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rrgtrees/rrgtrees.dtx
%doc %{_texmfdistdir}/source/latex/rrgtrees/rrgtrees.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
