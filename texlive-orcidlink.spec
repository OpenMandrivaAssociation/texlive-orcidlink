%global tl_name orcidlink
%global tl_revision 78657

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Insert hyperlinked ORCiD logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/orcidlink
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/orcidlink.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a command to insert the ORCiD logo, which is
hyperlinked to the URL of the researcher whose iD was specified.

