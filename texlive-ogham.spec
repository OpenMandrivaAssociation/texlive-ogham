%global tl_name ogham
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for typesetting Ogham script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ogham
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The font provides the Ogham alphabet, which is found on a number of
Irish and Pictish carvings dating from the 4th century AD. The font is
distributed as Metafont source, which has been patched (with the
author's permission) for stability at different output device
resolutions. (Thanks are due to Peter Flynn and Dan Luecking.)

