Name:		texlive-orcidlink
Version:	59560
Release:	1
Summary:	Insert hyperlinked ORCiD logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/orcidlink
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a command to insert the ORCiD logo, which
is hyperlinked to the URL of the researcher whose iD was
specified.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/orcidlink
%{_texmfdistdir}/tex/latex/orcidlink
%doc %{_texmfdistdir}/doc/latex/orcidlink

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
