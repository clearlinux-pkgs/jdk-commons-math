PKG_NAME := jdk-commons-math
URL := https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.1/commons-math-2.1.jar
ARCHIVES := https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.1/commons-math-2.1.pom %{buildroot}

include ../common/Makefile.common
