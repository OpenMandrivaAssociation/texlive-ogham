# revision 24876
# category Package
# catalog-ctan /fonts/ogham
# catalog-date 2011-12-19 12:56:45 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-ogham
Version:	20190228
Release:	1
Summary:	Fonts for typesetting Ogham script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ogham
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111219-2
+ Revision: 754505
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111219-1
+ Revision: 745304
- texlive-ogham

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080927-1
+ Revision: 719155
- texlive-ogham
- texlive-ogham
- texlive-ogham
- texlive-ogham

