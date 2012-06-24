Summary:	LAT - LDAP Administration Tool
Summary(pl):	LAT - narz�dzie administracyjne dla LDAP
Name:		lat
Version:	1.0	
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://people.mmgsecurity.com/~lorenb/lat/releases/%{name}-%{version}.tar.gz
# Source0-md5:	427b6b2f633c907e01816291f8657e16
Source1:	%{name}.png
Patch0:		%{name}-scrollkeeper_dir.patch
Patch1:		%{name}-desktop.patch
URL:		http://people.mmgsecurity.com/~lorenb/lat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-gnome-devel >= 2.4
BuildRequires:	intltool
BuildRequires:	mono-csharp >= 1.1.12.1
Requires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAT stands for LDAP Administration Tool. The tool allows you to browse
LDAP-based directories and add/edit/delete entries contained within.
It can store profiles for quick access to different servers. There are
also different views available such as Users, Groups and Hosts which
allow you to easily manage objects without having to deal with the
intricacies of LDAP.

%description -l pl
LAT to skr�t od LDAP Administration Tool (narz�dzie administracyjne
LDAP). Narz�dzie pozwala przegl�da� katalogi oparte o LDAP i
dodawa�/modyfikowa�/usuwa� zawarte w nich wpisy. Mo�e przechowywa�
profile do szybkiego dost�pu do r�nych serwer�w. S� dost�pne tak�e
r�ne widoki, takie jak u�ytkownicy, grupy i hosty, pozwalaj�ce �atwo
zarz�dza� obiektami bez potrzeby zajmowania si� komplikacjami LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

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
%attr(755,root,root) %{_libdir}/%{name}/*
%{_mandir}/man1/lat.1*
%{_datadir}/omf/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/application-registry/%{name}.applications
%{_sharedstatedir}/scrollkeeper/*
