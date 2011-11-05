# revision 15878
# category Package
# catalog-ctan /fonts/ogham
# catalog-date 2008-09-27 14:07:03 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-ogham
Version:	20080927
Release:	1
Summary:	Fonts for typesetting Ogham script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ogham
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ogham.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
The font provides the Ogham alphabet, which is found on a
number of Irish and Pictish carvings dating from the 4th
century AD. The font is distributed as a MetaFont program,
which has been patched (with the author's permission) for
stability at different output device resolutions. (Thanks are
due to Peter Flynn and Dan Luecking.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ogham/ogham.mf
%{_texmfdistdir}/fonts/tfm/public/ogham/ogham.tfm
%doc %{_texmfdistdir}/doc/latex/ogham/testfont.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
