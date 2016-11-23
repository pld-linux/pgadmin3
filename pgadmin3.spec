Summary:	Powerful administration and development platform for the PostgreSQL
Summary(pl.UTF-8):	Potężna platforma do administrowania i programowania bazy PostgreSQL
Name:		pgadmin3
Version:	1.22.2
Release:	1
Epoch:		0
License:	Artistic
Group:		Applications/Databases
Source0:	http://ftp.postgresql.org/pub/pgadmin3/release/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	cc5ad37470e36b3353ab925a8e82eb35
Source1:	%{name}.desktop
Patch0:		%{name}-m4.patch
URL:		http://www.pgadmin.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.6.18
BuildRequires:	libxslt-devel >= 1.1
BuildRequires:	openssl-devel
BuildRequires:	postgresql-backend-devel >= 8.3.0
BuildRequires:	postgresql-devel >= 8.3.0
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.8.0
BuildRequires:	wxWidgets-utils >= 2.8.0
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

%prep
%setup -q
%patch0 -p1

%build
rm -f config/*
%{__aclocal}
%{__autoconf}
cp -f config.rpath.in config/config.rpath
%{__automake}
%configure \
	--with-wx-config="%{_bindir}/wx-gtk2-unicode-config" \
	--with-wx-version="3.0"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_pgmoduledir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p pkg/debian/pgadmin3.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/pgadmin3.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/pgadmin3.desktop
%{_pixmapsdir}/pgadmin3.xpm
