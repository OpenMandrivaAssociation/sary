%define name sary
%define version	1.2.0
%define release	%mkrel 6

%define libname_orig lib%{name}
%define libname %mklibname %{name} 10

Name:		%{name}
Summary:	Suffix array library (with tools)
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
Sary is a suffix array library. It provides fast full-text 
search facilities for text files on the order of 10 to 100 
MB using a data structure called a suffix array. It can also 
search specific fields in a text file by assigning index 
points to those fields. 


%package -n %{libname}
Summary:	Sary library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Sary is a suffix array library. It provides fast full-text 
search facilities for text files on the order of 10 to 100 
MB using a data structure called a suffix array. It can also 
search specific fields in a text file by assigning index 
points to those fields. 

%package -n %{libname}-devel
Summary:	Development headers for sary
Group:		Development/C
Requires:		%{libname} = %{version}
Requires:		libglib2.0-devel
Provides:		%{name}-devel = %{version}-%{release}
Provides:		%{libname_orig}-devel = %{version}-%{release}
Obsoletes: libsary0-devel

%description -n %{libname}-devel
Sary is a suffix array library. It provides fast full-text 
search facilities for text files on the order of 10 to 100 
MB using a data structure called a suffix array. It can also 
search specific fields in a text file by assigning index 
points to those fields.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure
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
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/mksary
%{_bindir}/sary
%{_datadir}/%name
%_mandir/man*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsary.so.10.0.0
%{_libdir}/libsary.so.10

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libsary.a
%{_libdir}/libsary.la
%{_libdir}/libsary.so
%{_libdir}/pkgconfig/sary.pc


