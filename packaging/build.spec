#
# spec file for package build (Version 2010.03.10)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           build
License:        GPLv2+
Group:          Development/Tools/Building
AutoReqProv:    on
Summary:        A Script to Build SUSE Linux RPMs
Version:        2011.01.10a
Release:        1
# osc rm build-*tar.bz2
# REVISION=$(svn info https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/build | sed -ne "/Revision: /s///p")
# VERSION="$(date +"%Y.%m.%d").r$REVISION"
# svn export -r$REVISION https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/build build-$VERSION
# tar cjvf build-$VERSION.tar.bz2 build-$VERSION
# rm -rf build-$VERSION
# osc add build-$VERSION.tar.bz2
# # There's several occurences of "Version: something" in this file,
# # two of them valid, so we need to be picky in the match.
# sed --in-place build.spec -e"/\(Version:\?[[:space:]]\+\)\([0-9]\{4\}\.[0-9][0-9]\.[0-9][0-9]\.r[0-9]\+\)/s,,\1$VERSION,"
# osc build build.spec
# osc ci
# osc submitreq create -m"current svn snapshot." openSUSE:Tools build openSUSE:Factory
Source:         build-%{version}.tar.gz
Source1:        tizen-1.0.conf
Patch100:       build-pkg-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Manual requires to avoid hard require to bash-static
AutoReqProv:    off
# Keep the following dependencies in sync with obs-worker package
Requires:       bash
Requires:       perl
Requires:       perl-TimeDate
Requires:       binutils
Requires:       tar

%description
This package provides a script for building RPMs for SUSE Linux in a
chroot environment.

%prep
%setup -q
%patch100 -p1

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install
install %{SOURCE1} %{buildroot}%{_prefix}/lib/build/configs
cd %{buildroot}%{_prefix}/lib/build/configs/
ln -s tizen-1.0.conf default.conf

%files
%defattr(-,root,root)
%doc README
%{_bindir}/build
%{_bindir}/buildvc
%{_bindir}/unrpm
%{_prefix}/lib/build
%{_mandir}/man1/build.1*
