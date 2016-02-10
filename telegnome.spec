Summary:	TeleGNOME - GNOME application to display teletext
Summary(pl.UTF-8):	TeleGNOME - aplikacja GNOME do wyświetlania teletekstu
Name:		telegnome
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/telegnome/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	ead2f4134f88fb19289a6336a7a6cf5c
URL:		http://telegnome.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	dconf-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.26
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	scrollkeeper
Requires:	cairo >= 1.10
Requires:	gdk-pixbuf2 >= 2.26
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeleGNOME - GNOME application to display teletext.

%description -l pl.UTF-8
TeleGNOME - aplikacja GNOME do wyświetlania teletekstu.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%scrollkeeper_update_post

%postun
%glib_compile_schemas
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog* MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/telegnome
%{_datadir}/glib-2.0/schemas/org.gnome.telegnome.gschema.xml
%{_desktopdir}/telegnome.desktop
%{_mandir}/man1/telegnome.1*
