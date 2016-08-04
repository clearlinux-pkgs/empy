#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : empy
Version  : 3.3.2
Release  : 1
URL      : http://www.alcyone.com/software/empy/empy-3.3.2.tar.gz
Source0  : http://www.alcyone.com/software/empy/empy-3.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: empy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
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

%package python
Summary: python components for the empy package.
Group: Default

%description python
python components for the empy package.


%prep
%setup -q -n empy-3.3.2

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
