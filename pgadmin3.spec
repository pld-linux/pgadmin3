# Conditional build:
Summary:	Powerful administration and development platform for the PostgreSQL
Name:		pgadmin3
Version:	1.2.0
Release:	1
Epoch:		0
License:	Artistic License
Group:		Applications/Databases
Source0:	ftp://ftp6.pl.postgresql.org/pub/postgresql/pgadmin3/release/v1.2.0/src/%{name}-%{version}.tar.gz
# Source0-md5:	09caa00a0249978781215bf3e4ac02b8
URL:		http://www.pgadmin.org/
BuildRequires:	wxGTK2-unicode-devel >= 2.5.3
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pgAdmin III is designed to answer the needs of all users, from writing simple 
SQL queries to developing complex databases. The graphical interface supports 
all PostgreSQL features and makes administration easy. The application also 
includes a query builder, an SQL editor, a server-side code editor and much 
more. pgAdmin III is released with an installer and does not require any 
additional driver to communicate with the database server.

%prep
%setup -q -n %{name}-%{version}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc LICENCE.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
