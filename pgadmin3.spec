Summary:	Powerful administration and development platform for the PostgreSQL
Summary(pl):	Potê¿na platforma do administrowania i programowania bazy PostgreSQL
Name:		pgadmin3
Version:	1.4.1
Release:	2
Epoch:		0
License:	Artistic
Group:		Applications/Databases
Source0:	ftp://ftp6.pl.postgresql.org/pub/postgresql/pgadmin3/release/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	bf78696c72acd782d63feb2bd5ce6f48
Source1:	%{name}.desktop
URL:		http://www.pgadmin.org/
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.6.0
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

%description -l pl
pgAdmin III zosta³ zaprojektowany jako odpowied¼ na potrzeby
wszystkich u¿ytkowników, od pisania prostych zapytañ SQL do tworzenia
skomplikowanych baz danych. Graficzny interfejs obs³uguje wszystkie
mo¿liwo¶ci PostgreSQL-a i u³atwia administrowanie. Aplikacja zawiera
tak¿e narzêdzie do budowania zapytañ, edytor SQL, edytor kodu po
stronie serwera i wiele wiêcej. pgAdmin III zosta³ wydany z
instalatorem i nie wymaga ¿adnego dodatkowego sterownika do
komunikowania z serwerem baz danych.

%package -n postgresql-module-pgadmin3
Summary:	Full instrumentation when using PgAdmin
Summary(pl):	Pe³na obs³uga dla funkcjonalno¶ci PgAdmina
Group:		Applications/Databases
Requires:	postgresql >= 8.1

%description -n postgresql-module-pgadmin3
Module which implements a number of support functions which PgAdmin
will use to provide additional functionality if installed on a server.

%description -n postgresql-module-pgadmin3 -l pl
Ten modu³ implementuje wiele funkcji pomocniczych, które u¿ywa PgAdmin
do zapewnienia dodatkowej funkcjonalno¶ci.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub config
%configure \
	--with-wx-config=wx-gtk2-unicode-config
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
%doc LICENCE.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/pgadmin3.desktop
%{_pixmapsdir}/pgadmin3.xpm

%files -n postgresql-module-pgadmin3
%defattr(644,root,root,755)
%doc xtra/admin81/README* xtra/admin81/*.sql
%attr(755,root,root) %{_pgmoduledir}/*.so
