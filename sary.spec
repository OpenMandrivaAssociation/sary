%define major 10
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Suffix array library (with tools)
Name:		sary
Version:	1.2.0
Release:	21
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
%{_libdir}/libsary.so
%{_libdir}/pkgconfig/sary.pc


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.2.0-13mdv2011.0
+ Revision: 669808
- fix requires

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-12mdv2011.0
+ Revision: 607509
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-11mdv2010.1
+ Revision: 523962
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-10mdv2010.0
+ Revision: 426997
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.2.0-9mdv2009.1
+ Revision: 366278
- use configuer2_5x

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-9mdv2009.0
+ Revision: 289292
- fix linkage
- fix devel package naming
- check major

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-7mdv2008.1
+ Revision: 171087
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 02 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.0-6mdv2008.0
+ Revision: 20366
- rebuild for new era
- don't package COPYING (twice!)
- move .so.10 file out of -devel package
- correct descriptions


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.0-5mdk
- Rebuild

* Sun Aug 07 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.2.0-4mdk
- fix buildrequires (x86_64...)

* Sat Aug 06 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.2.0-3mdk
- add requires on libglib2.0-devel to -devel pkg (fixes ruby-sary build)

* Sat Jun 04 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.2.0-2mdk
- add BuildRequires: libglib2.0-devel

* Fri Apr 15 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.0-1mdk
- fix upgrade
- fix directory ownership
- fix major
- new release (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

* Fri Feb 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.1.0-1mdk
- initial spec for mdk

