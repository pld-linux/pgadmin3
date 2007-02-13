Summary:	Powerful administration and development platform for the PostgreSQL
Summary(pl.UTF-8):	Potężna platforma do administrowania i programowania bazy PostgreSQL
Name:		pgadmin3
Version:	1.6.1
Release:	1
Epoch:		0
License:	Artistic
Group:		Applications/Databases
Source0:	ftp://ftp6.pl.postgresql.org/pub/postgresql/pgadmin3/release/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	0cdfffceb09e40787ead39541bcd5683
Source1:	%{name}.desktop
Patch0:		%{name}-m4.patch
Patch1:		%{name}-wx.patch
URL:		http://www.pgadmin.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2 >= 2.6.18
BuildRequires:	libxslt >= 1.1
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel >= 7.4
BuildRequires:	postgresql-backend-devel >= 7.4
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pgmoduledir		%{_libdir}/postgresql

%description
pgAdmin III is designed to answer the needs of all users, from writing
simple SQL queries to developing complex databases. The graphical
interface supports all PostgreSQL features and makes administration
easy. The application also includes a query builder, an SQL editor, a
server-side code editor and much more. pgAdmin III is released with an
installer and does not require any additional driver to communicate
with the database server.

%description -l pl.UTF-8
pgAdmin III został zaprojektowany jako odpowiedź na potrzeby
wszystkich użytkowników, od pisania prostych zapytań SQL do tworzenia
skomplikowanych baz danych. Graficzny interfejs obsługuje wszystkie
możliwości PostgreSQL-a i ułatwia administrowanie. Aplikacja zawiera
także narzędzie do budowania zapytań, edytor SQL, edytor kodu po
stronie serwera i wiele więcej. pgAdmin III został wydany z
instalatorem i nie wymaga żadnego dodatkowego sterownika do
komunikowania z serwerem baz danych.

%package -n postgresql-module-pgadmin3
Summary:	Full instrumentation when using PgAdmin
Summary(pl.UTF-8):	Pełna obsługa dla funkcjonalności PgAdmina
Group:		Applications/Databases
Requires:	postgresql >= 8.1

%description -n postgresql-module-pgadmin3
Module which implements a number of support functions which PgAdmin
will use to provide additional functionality if installed on a server.

%description -n postgresql-module-pgadmin3 -l pl.UTF-8
Ten moduł implementuje wiele funkcji pomocniczych, które używa PgAdmin
do zapewnienia dodatkowej funkcjonalności.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f config/*
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-wx-config="%{_bindir}/wx-gtk2-unicode-config" \
	--with-wx-version="2.8"
%{__make}

sed 's#MODULE_PATHNAME#%{_pgmoduledir}/admin81#g' xtra/admin81/admin81.sql.in > xtra/admin81/admin81.sql
%{__cc} %{rpmcflags} -fpic -I. -I%{_includedir}/postgresql/server -c -o xtra/admin81/admin81.o xtra/admin81/admin81.c -MMD
%{__cc} -shared %{rpmldflags} -o xtra/admin81/admin81.so xtra/admin81/admin81.o

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_pgmoduledir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/include/images/pgAdmin3.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/pgadmin3.xpm

install xtra/admin81/admin81.so $RPM_BUILD_ROOT%{_pgmoduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/pgadmin3.desktop
%{_pixmapsdir}/pgadmin3.xpm

%files -n postgresql-module-pgadmin3
%defattr(644,root,root,755)
%doc xtra/admin81/README* xtra/admin81/*.sql
%attr(755,root,root) %{_pgmoduledir}/*.so
