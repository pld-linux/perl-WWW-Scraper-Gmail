#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Scraper-Gmail
Summary:	WWW::Scraper::Gmail - Perl extension for loging in and reading Gmail Mailbox information.
Summary(pl):	WWW::Scraper::GMail - rozszerzenie Perla do obs�ugi konta Gmail (logowanie i odczyt informacji).
Name:		perl-WWW-Scraper-Gmail
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	165dc699fb268899b31b75c9404ac4b3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logs into email through HTTPS, does some stuff and gets back a list of
inbox items. Uses ~/.gmailrc for now for username and password. The
format is as follows
[gmail]
username=<username>
password=<password>

you'd do well to chmod it 700.
Doesn't do error checking for log in problems.

%description -l pl
Za po�rednictwem HTTPS loguje si� do konta Gmail, wykonuje pewne
operacje i zwraca list� element�w w skrzynce odbiorczej. Login oraz
has�o zapisane s� w pliku ~/.gmailrc, kt�rego format jest nast�puj�cy:
[gmail]
username=<login>
password=<haslo>

warto zmieni� uprawnienia pliku na 700.
Nie nast�puje sprawdzanie b��d�w w poszukiwaniu problem�w z
logowaniem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Scraper/*.pm
%{_mandir}/man3/*
