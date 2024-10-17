Name:		texlive-ogham
Version:	24876
Release:	2
Summary:	Fonts for typesetting Ogham script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ogham
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font provides the Ogham alphabet, which is found on a
number of Irish and Pictish carvings dating from the 4th
century AD. The font is distributed as Metafont source, which
has been patched (with the author's permission) for stability
at different output device resolutions. (Thanks are due to
Peter Flynn and Dan Luecking.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ogham/ogham.mf
%{_texmfdistdir}/fonts/tfm/public/ogham/ogham.tfm
%doc %{_texmfdistdir}/doc/fonts/ogham/testfont.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
