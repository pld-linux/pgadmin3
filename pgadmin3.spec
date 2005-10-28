%define		_status	beta
%define		_beta	3
Summary:	Powerful administration and development platform for the PostgreSQL
Summary(pl):	Potê¿na platforma do administrowania i programowania bazy PostgreSQL
Name:		pgadmin3
Version:	1.4.0
Release:	0.1.%{_status}%{_beta}
Epoch:		0
License:	Artistic
Group:		Applications/Databases
Source0:	ftp://ftp6.pl.postgresql.org/pub/postgresql/pgadmin3/%{_status}/src/%{name}-%{version}-%{_status}%{_beta}.tar.gz
# Source0-md5:	7220ccfe0732d6258a05fb10770b4168
Source1:	%{name}.desktop
URL:		http://www.pgadmin.org/
BuildRequires:	automake
BuildRequires:	postgresql-devel
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n %{name}-%{version}-%{_status}%{_beta}

%build
cp /usr/share/automake/config.sub config
%configure \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -f ./src/include/images/pgAdmin3.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/pgadmin3.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/pgadmin3.desktop
%{_pixmapsdir}/pgadmin3.xpm
