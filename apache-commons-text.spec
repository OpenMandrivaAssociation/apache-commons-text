Name:		apache-commons-text
Version:	1.15.0
Release:	1
Summary:	Utilities for working with text
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-text/
Source0:	https://github.com/apache/commons-text/archive/refs/tags/rel/commons-text-%{version}.tar.gz#/commons-text-%{version}.tar.gz
BuildArch:	noarch
# The site-checkout profile is active when site-content is absent, and
# antrun is on the sysjar keep list.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
BuildRequires:	mvn(org.apache.commons:commons-lang3)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-text --link %{name}

%description
Apache Commons Text provides algorithms for matching, escaping, and
formatting text. Doxia uses its StringEscapeUtils.

%prep
%autosetup -n commons-text-rel-commons-text-%{version}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
