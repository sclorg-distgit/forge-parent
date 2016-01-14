%global pkg_name forge-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        31
Release:        2.10%{?dist}
Summary:        Sonatype Forge Parent Pom
License:        ASL 2.0
URL:            https://docs.sonatype.org/display/FORGE/Index
Source0:        http://repo1.maven.org/maven2/org/sonatype/forge/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-source-plugin

%description
Sonatype Forge is an open-source community dedicated to the creation of the 
next-generation of development tools and technologies.

%prep
%setup -qcT -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# We don't have nexus-staging-maven-plugin in Fedora
%pom_remove_plugin :nexus-staging-maven-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 31-2.10
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 31-2.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 31-2.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.6
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.5
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.3
- Add missing BR: maven-source-plugin

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-2.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 31-2
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-1
- Update to upstream version 31
- Install missing LICENSE file
- Build with xmvn

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 20 2010 Weinan Li <weli@redhat.com> - 5-5
- Rebuild for dist-f14-maven221

* Thu May 20 2010 Weinan Li <weli@redhat.com> - 5-4
- Change JPP.%{name}.pom to JPP-%{name}.pom

* Fri May 14 2010 Weinan Li <weli@redhat.com> - 5-3
- Each package must consistently use macros, use rm instead of all %{_rm}
- Add Requires: jpackage-utils

* Thu May 13 2010 Weinan Li <weli@redhat.com> - 5-2
- Add the license source note
- Cleanup the svn metadata in source
- Add the full instructions for creating the tar in the comment 

* Wed May 12 2010 Weinan Li <weli@redhat.com> - 5-1
- Initial version
