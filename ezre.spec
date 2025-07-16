Name: gsshs
Version: v1.0.1
Summary: Fast and easy SSH setup for Github on Mac OS and Linux.
Release: 1
License: 3-BSD
URL: https://github.com/alex-free/github-ssh-setup
Packager: Alex Free
Group: Unspecified

%description
Fast and easy SSH setup for Github on Mac OS and Linux.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/gsshs %{buildroot}/usr/bin/

%files
/usr/bin/gsshs
