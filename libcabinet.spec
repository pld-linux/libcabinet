Summary:	Cabinet File Library and Utilities
Summary(pl.UTF-8):	Biblioteka i narzędzia do obsługi plików Cabinet
Name:		libcabinet
Version:	0.30
Release:	3
License:	non-commercial, see readme.txt
Group:		Libraries
Source0:	http://Trill.cis.fordham.edu/~barbacha/cabinet_library/%{name}-%{version}.tar.gz
# Source0-md5:	f6b0683b4cf57ee3b9614135d0f8d0fe
Source1:	%{name}-Makefile
Patch0:		%{name}-endl.patch
Patch1:		%{name}-gcc3.patch
URL:		http://Trill.cis.fordham.edu/~barbacha/cabinet_library/
# needed with gcc3 patch
BuildRequires:	libstdc++-devel >= 5:3.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet File library and utilities.

%description -l pl.UTF-8
Biblioteka i narzędzia do obsługi plików Cabinet.

%package devel
Summary:	libcabinet development package
Summary(pl.UTF-8):	libcabinet - część dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 5:3.2

%description devel
Header files for libcabinet.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki libcabinet.

%package static
Summary:	libcabinet static library
Summary(pl.UTF-8):	Statyczna biblioteka libcabinet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libcabinet.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libcabinet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
install -m644 %{SOURCE1} Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libcabinet-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcabinet.so
%{_libdir}/*.la
%{_includedir}/cabinet

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
