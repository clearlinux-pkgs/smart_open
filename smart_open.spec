#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smart_open
Version  : 4.0.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/fd/aa/eae69b4a86ed401625820a202272f3c0cbd8eade5abdbe248396aa5a837d/smart_open-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/aa/eae69b4a86ed401625820a202272f3c0cbd8eade5abdbe248396aa5a837d/smart_open-4.0.0.tar.gz
Summary  : Utils for streaming large files (S3, HDFS, GCS, Azure Blob Storage, gzip, bz2...)
Group    : Development/Tools
License  : MIT
Requires: smart_open-license = %{version}-%{release}
Requires: smart_open-python = %{version}-%{release}
Requires: smart_open-python3 = %{version}-%{release}
Requires: awscli
Requires: azure-common
Requires: azure-core
Requires: azure-storage-blob
Requires: boto3
Requires: requests
BuildRequires : awscli
BuildRequires : azure-common
BuildRequires : azure-core
BuildRequires : azure-storage-blob
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : bz2file
BuildRequires : requests

%description
smart_open — utils for streaming large files in Python
        ======================================================
        
        
        |License|_ |Travis|_ |Appveyor|_ |Coveralls|_ |Downloads|_

%package license
Summary: license components for the smart_open package.
Group: Default

%description license
license components for the smart_open package.


%package python
Summary: python components for the smart_open package.
Group: Default
Requires: smart_open-python3 = %{version}-%{release}

%description python
python components for the smart_open package.


%package python3
Summary: python3 components for the smart_open package.
Group: Default
Requires: python3-core
Provides: pypi(smart_open)
Requires: pypi(requests)

%description python3
python3 components for the smart_open package.


%prep
%setup -q -n smart_open-4.0.0
cd %{_builddir}/smart_open-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606261107
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/smart_open
cp %{_builddir}/smart_open-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/smart_open/088eeb3fff4ab23573e49bd76ebf2c0e02b5ea51
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/smart_open/088eeb3fff4ab23573e49bd76ebf2c0e02b5ea51

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
