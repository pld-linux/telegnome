Summary:	TeleGNOME - GNOME application to display teletext
Summary(pl.UTF-8):	TeleGNOME - aplikacja GNOME do wyświetlania teletekstu
Name:		telegnome
Version:	0.3.7
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/telegnome/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	5a7ef484d9aaf496375665ecf1d78341
URL:		https://telegnome.sourceforge.io/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.13
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	gdk-pixbuf2-devel >= 2.26
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.10
Requires:	gdk-pixbuf2 >= 2.26
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeleGNOME - GNOME application to display teletext.

%description -l pl.UTF-8
TeleGNOME - aplikacja GNOME do wyświetlania teletekstu.

%prep
%setup -q

%build
%{__gettextize}
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/telegnome
%{_datadir}/glib-2.0/schemas/org.gnome.telegnome.gschema.xml
%{_datadir}/metainfo/telegnome.appdata.xml
%{_desktopdir}/telegnome.desktop
%{_iconsdir}/hicolor/*x*/apps/telegnome.png
%{_mandir}/man1/telegnome.1*
