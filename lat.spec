Summary:	LAT - LDAP Administration Tool
Summary(pl.UTF-8):	LAT - narzędzie administracyjne dla LDAP
Name:		lat
Version:	1.2.3
Release:	1	
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dev.mmgsecurity.com/downloads/lat/1.2/lat-%{version}.tar.gz
# Source0-md5:	0725508d180720d260a70c5b39d387ba
Source1:	%{name}.png
Patch0:		%{name}-scrollkeeper_dir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-lib64.patch
URL:		http://dev.mmgsecurity.com/projects/lat/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= 2.4
BuildRequires:	gnome-keyring-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.12.1
BuildRequires:	scrollkeeper
Requires:	scrollkeeper
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAT stands for LDAP Administration Tool. The tool allows you to browse
LDAP-based directories and add/edit/delete entries contained within.
It can store profiles for quick access to different servers. There are
also different views available such as Users, Groups and Hosts which
allow you to easily manage objects without having to deal with the
intricacies of LDAP.

%description -l pl.UTF-8
LAT to skrót od LDAP Administration Tool (narzędzie administracyjne
LDAP). Narzędzie pozwala przeglądać katalogi oparte o LDAP i
dodawać/modyfikować/usuwać zawarte w nich wpisy. Może przechowywać
profile do szybkiego dostępu do różnych serwerów. Są dostępne także
różne widoki, takie jak użytkownicy, grupy i hosty, pozwalające łatwo
zarządzać obiektami bez potrzeby zajmowania się komplikacjami LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/fr{_FR,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}
%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.dll*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*
%{_mandir}/man1/lat.1*
%{_datadir}/omf/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/application-registry/%{name}.applications
%{_sharedstatedir}/scrollkeeper/*
%{_pkgconfigdir}/*.pc
