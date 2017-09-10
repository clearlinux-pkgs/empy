#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : empy
Version  : 3.3.3
Release  : 5
URL      : http://www.alcyone.com/software/empy/empy-3.3.3.tar.gz
Source0  : http://www.alcyone.com/software/empy/empy-3.3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: empy-legacypython
Requires: empy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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

%package legacypython
Summary: legacypython components for the empy package.
Group: Default

%description legacypython
legacypython components for the empy package.


%package python
Summary: python components for the empy package.
Group: Default
Requires: empy-legacypython

%description python
python components for the empy package.


%prep
%setup -q -n empy-3.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505002161
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505002161
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
