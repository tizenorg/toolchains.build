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
Release:        %{?release_prefix:%{release_prefix}.}1.45.%{?dist}%{!?dist:tizen}
VCS:            toolchains/build#submit/trunk/20121019.064836-0-gd0510e0a54964f2ae5dd88fc302e533ff6419c83
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
%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.064836 
- PROJECT: toolchains/build
- COMMIT_ID: d0510e0a54964f2ae5dd88fc302e533ff6419c83
- PATCHSET_REVISION: d0510e0a54964f2ae5dd88fc302e533ff6419c83
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103285
- PATCHSET_REVISION: d0510e0a54964f2ae5dd88fc302e533ff6419c83
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 2011.01.10a
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Mon Jul  9 2012 UkJung Kim <ujkim@samsung.com> - 2011.01.10a
- Ignore pkg-config from config file lists
* Wed Jan 19 2011 Jian-feng Ding <jian-feng.ding@intel.com> - 2011.01.10a
- Update to 2011.01.10 snapshot, with three extra commits
  git HEAD: 585759875f7d225b6fc8f3e76cdffe955825dab4
* Wed Dec  1 2010 Fathi Boudra <fathi.boudra@nokia.com> - 2010.11.24
- Update to 2010.11.24: add workaround for Ubuntu 10 builds (BMC#10713)
* Tue Aug 10 2010 Jian-feng Ding <jian-feng.ding@intel.com> 2010.08.04
- Update to 2010.08.04 snapshot
* Fri Apr 16 2010 Yi Yang <yi.y.yang@intel.com> - 2010.04.15
- Update to 2010.04.15
* Fri Jan 15 2010 Anas Nashif <anas.nashif@intel.com> - 2010.01.13
- Update to  2010.01.13 snapshot
- Added moblin config file
* Mon Aug 10 2009 Anas Nashif <anas.nashif@intel.com> - 2009.07.27
- Update to 2009.07.27 snapshot
