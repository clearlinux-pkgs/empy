#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : empy
Version  : 3.3.4
Release  : 28
URL      : http://www.alcyone.com/software/empy/empy-3.3.4.tar.gz
Source0  : http://www.alcyone.com/software/empy/empy-3.3.4.tar.gz
Summary  : A templating system for Python.
Group    : Development/Tools
License  : LGPL-2.1
Requires: empy-license = %{version}-%{release}
Requires: empy-python = %{version}-%{release}
Requires: empy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Summary
A powerful and robust templating system for Python.
Overview
EmPy is a system for embedding Python expressions and statements
in template text; it takes an EmPy source file, processes it, and
produces output.  This is accomplished via expansions, which are
special signals to the EmPy system and are set off by a special
prefix (by default the at sign, '@').  EmPy can expand arbitrary
Python expressions and statements in this way, as well as a
variety of special forms.  Textual data not explicitly delimited
in this way is sent unaffected to the output, allowing Python to
be used in effect as a markup language.  Also supported are
callbacks via hooks, recording and playback via diversions, and
dynamic, chainable filters.  The system is highly configurable via
command line options and embedded commands.

%package license
Summary: license components for the empy package.
Group: Default

%description license
license components for the empy package.


%package python
Summary: python components for the empy package.
Group: Default
Requires: empy-python3 = %{version}-%{release}

%description python
python components for the empy package.


%package python3
Summary: python3 components for the empy package.
Group: Default
Requires: python3-core
Provides: pypi(empy)

%description python3
python3 components for the empy package.


%prep
%setup -q -n empy-3.3.4
cd %{_builddir}/empy-3.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582921345
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/empy
cp %{_builddir}/empy-3.3.4/COPYING %{buildroot}/usr/share/package-licenses/empy/e60c2e780886f95df9c9ee36992b8edabec00bcc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/empy/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
