Name     : jdk-commons-math
Version  : 2.1
Release  : 4
URL      : https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.1/commons-math-2.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.1/commons-math-2.1.jar
Source1  : https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.1/commons-math-2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-commons-math-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-commons-math package.
Group: Data

%description data
data components for the jdk-commons-math package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/commons-math.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/commons-math.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/commons-math.xml \
%{buildroot}/usr/share/maven-poms/commons-math.pom \
%{buildroot}/usr/share/java/commons-math.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/commons-math.jar
/usr/share/maven-metadata/commons-math.xml
/usr/share/maven-poms/commons-math.pom
