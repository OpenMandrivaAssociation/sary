%define major 10
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Suffix array library (with tools)
Name:		sary
Version:	1.2.0
Release:	%mkrel 13
Group:		System/Internationalization
License:	LGPL
URL:		http://prime.sourceforge.jp/src/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		sary-linkage_fix.diff
BuildRequires:	glib2-devel
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Sary is a suffix array library. It provides fast full-text search facilities
for text files on the order of 10 to 100 MB using a data structure called a
suffix array. It can also search specific fields in a text file by assigning
index points to those fields. 

%package -n	%{libname}
Summary:	Sary library
Group:		System/Internationalization
Provides:	%{libname_orig} = %{version}-%{release}

%description -n	%{libname}
Sary is a suffix array library. It provides fast full-text search facilities
for text files on the order of 10 to 100 MB using a data structure called a
suffix array. It can also search specific fields in a text file by assigning
index points to those fields. 

%package -n	%{develname}
Summary:	Development headers for sary
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes:	%{mklibname sary 0 -d}
Obsoletes:	%{mklibname sary 10 -d}

%description -n	%{develname}
Sary is a suffix array library. It provides fast full-text search facilities
for text files on the order of 10 to 100 MB using a data structure called a
suffix array. It can also search specific fields in a text file by assigning
index points to those fields. 

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/mksary
%{_bindir}/sary
%{_datadir}/%{name}
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsary.so.%{major}.0.0
%{_libdir}/libsary.so.%{major}

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libsary.a
%{_libdir}/libsary.la
%{_libdir}/libsary.so
%{_libdir}/pkgconfig/sary.pc
