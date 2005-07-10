Summary:	LAT - LDAP Administration Tool.
Name:		lat
Version:	0.6
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://people.mmgsecurity.com/~lorenb/lat/releases/%{name}-%{version}.tar.gz
# Source0-md5:	35813cf148fe7b69361f68b6b4eadb2c
Patch0:		%{name}-scrollkeeper_dir.patch
Patch1:		%{name}-desktop.patch
URL:		http://people.mmgsecurity.com/~lorenb/lat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	dotnet-gtk-sharp-devel >= 1.9.5-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAT stands for LDAP Administration Tool. The tool allows you to browse
LDAP-based directories and add/edit/delete entries contained within.
It can store profiles for quick access to different servers. There are
also different views available such as Users, Groups and Hosts which
allow you to easily manage objects without having to deal with the
intricacies of LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%scrollkeeper_update_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%{_mandir}/man1/lat.1*
%{_datadir}/locale/*
%{_datadir}/gnome/help/*
%{_datadir}/omf/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/application-registry/%{name}.applications
%{_sharedstatedir}/scrollkeeper/*
