Summary:	Cabinet File Library and Utilities
Summary(pl):	Biblioteka i narzêdzia do obs³ugi plików Cabinet
Name:		libcabinet
Version:	0.30
Release:	1
License:	non-commercial, see readme.txt
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://Trill.cis.fordham.edu/~barbacha/cabinet_library/%{name}-%{version}.tar.gz
Source1:	%{name}-Makefile
Patch0:		%{name}-endl.patch
URL:		http://Trill.cis.fordham.edu/~barbacha/cabinet_library/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet File library and utilities.

%description -l pl
Biblioteka i narzêdzia do obs³ugi plików Cabinet.

%package devel
Summary:	libcabinet development package
Summary(pl):	libcabinet - czê¶æ dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for libcabinet.

%description devel -l pl
Pliki nag³ówkowe do biblioteki libcabinet.

%package static
Summary:	libcabinet static library
Summary(pl):	Statyczna biblioteka libcabinet
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static version of libcabinet.

%description static -l pl
Statyczna wersja biblioteki libcabinet.

%prep
%setup -q
%patch -p1
install -m644 %{SOURCE1} Makefile

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags} -D_GNU_SOURCE" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libcabinet-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcabinet.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/cabinet

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
