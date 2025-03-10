#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	webcolors
Summary:	Library for working with sRGB color specifications as used in HTML and CSS
Summary(pl.UTF-8):	Biblioteka do pracy z definicjami kolorów sRGB używanymi w formatach HTML i CSS
Name:		python3-%{module}
Version:	1.12
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/ubernostrum/webcolors/releases
Source0:	https://github.com/ubernostrum/webcolors/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	7e330313ce1689d19d2823b329a5e342
URL:		https://github.com/ubernostrum/webcolors
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for working with color names and color value formats defined
by the HTML and CSS specifications for use in documents on the Web.

Support is included for the following formats (RGB colorspace only;
conversion to/from HSL can be handled by the colorsys module in the
Python standard library):
- Specification-defined color names
- Six-digit hexadecimal
- Three-digit hexadecimal
- Integer rgb() triplet
- Percentage rgb() triple

%description -l pl.UTF-8
Biblioteka do pracy z nazwami kolorów oraz formatami wartości kolorów
określonymi w specyfikacjach HTML i CSS, przeznaczonych do użycia w
dokumentach WWW.

Obsługiwane są następujące formaty (tylko przestrzeń nazw RGB;
konwersję do/z HSL można uzyskać korzystając z modułu colorsys
biblioteki standardowej Pythona):
- nazwy kolorów określone w specyfikacji
- sześciocyfrowe wartości szesnastkowe
- trzycyfrowe wartości szesnastkowe
- trójki całkowite rgb()
- trójki procentowe rgb()

%package apidocs
Summary:	Documentation for Python webcolors module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona webcolors
Group:		Documentation

%description apidocs
Documentation for Python webcolors module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu Pythona webcolors.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/webcolors.py
%{py3_sitescriptdir}/__pycache__/webcolors.cpython-*.py[co]
%{py3_sitescriptdir}/webcolors-%{version}-*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
