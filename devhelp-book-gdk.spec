Summary:	DevHelp book: GDK
Summary(pl.UTF-8):	Książka do DevHelpa o GDK
Name:		devhelp-book-gdk
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdk-1.2.tar.gz
# Source0-md5:	82aafa08823f64682195db611cdc60fe
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about GDK 1.2.

%description -l pl.UTF-8
Książka do DevHelpa o GDK 1.2.

%prep
%setup -q -c -n gdk-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gdk-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gdk-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gdk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
