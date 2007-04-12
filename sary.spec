%define version	1.2.0
%define release	5mdk

%define libname_orig lib%{name}
%define libname %mklibname %{name} 10

Name:		sary
Summary:	Sary is a set of a suffix array library and tools
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		LGPL
URL:			http://prime.sourceforge.jp/src/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	glib2-devel
Requires:			%{libname} = %{version}

%description
Sary is a suffix array library and tools. It provides fast
full-text search facilities for text files on the order of
10 to 100 MB using a data structure called a suffix array.
It can also search specific fields in a text file by
assigning index points to those fields. 


%package -n %{libname}
Summary:	Sary library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
sary library.

%package -n %{libname}-devel
Summary:	Headers of uim for development
Group:		Development/C
Requires:		%{libname} = %{version}
Requires:		libglib2.0-devel
Provides:		%{name}-devel = %{version}-%{release}
Provides:		%{libname_orig}-devel = %{version}-%{release}
Obsoletes: libsary0-devel

%description -n %{libname}-devel
Headers of %{name} for development.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/mksary
%{_bindir}/sary
%{_datadir}/%name
%_mandir/man*/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libsary.so.10.0.0

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_includedir}/*
%{_libdir}/libsary.a
%{_libdir}/libsary.la
%{_libdir}/libsary.so
%{_libdir}/libsary.so.10
%{_libdir}/pkgconfig/sary.pc


