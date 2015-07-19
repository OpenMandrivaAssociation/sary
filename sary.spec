%define major 10
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Suffix array library (with tools)
Name:		sary
Version:	1.2.0
Release:	23
Group:		System/Internationalization
License:	LGPL
URL:		http://prime.sourceforge.jp/src/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		sary-linkage_fix.diff
BuildRequires:	pkgconfig(glib-2.0)
Requires:	%{libname} = %{version}

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
%configure
%make

%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/mksary
%{_bindir}/sary
%{_datadir}/%{name}
%{_mandir}/man*/*

%files -n %{libname}
%{_libdir}/libsary.so.%{major}.0.0
%{_libdir}/libsary.so.%{major}

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libsary.so
%{_libdir}/pkgconfig/sary.pc
