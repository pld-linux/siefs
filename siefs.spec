#
# Conditional build:
%bcond_without	dist_kernel	# build without kernel from distribution
#
Summary:	SieFS - virtual filesystem for Siemens mobile phones' memory
Summary(pl):	SieFS - wirtualny system plików do pamiêci telefonów komórkowych Siemens
Name:		siefs
Version:	0.4
Release:	1@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://mirror01.users.i.com.ua/~dmitry_z/%{name}-%{version}.tar.gz
# Source0-md5:	d7e72b47e74d89c0385d0abb407d78b5
URL:		http://mirror01.users.i.com.ua/~dmitry_z/siefs/
%{?with_dist_kernel:BuildRequires:	kernel-headers >= 2.4}
BuildRequires:	libfuse-static
# check it
Requires:	fusermount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is SieFS - a virtual filesystem for accessing Siemens mobile
phones' memory via datacable. Now you can mount your phone to a Linux
box and browse it like a simple directory! The program was tested on
S45/ME45/SL45/S55/M55/MC60, but should work also on C55/M50/MT50/SL55/C60.

%description -l pl
SieFS - wirtualny system plików udostêpniaj±cy pamiêæ telefonów
komórkowych Siemens pod³±czonych kablem. Pozwala podmontowaæ telefon
spod Linuksa i przegl±daæ go tak, jak zwyk³y katalog. Program by³
testowany na S45/ME45/SL45/S55/MC60, ale powinien dzia³aæ tak¿e z
C55/M50/MT50/SL55/C60.

%prep
%setup -q

%build
%configure2_13 \
	--with-kernel=%{_kernelsrcdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
# fuse only
%doc ChangeLog NEWS 
# fuse
# %%attr(755,root,root) %{_bindir}/fusermount
# siefs itself
%attr(755,root,root) %{_bindir}/siefs
%attr(755,root,root) %{_bindir}/slink
%attr(755,root,root) %{_bindir}/vmo2wav

# -devel or fuse-devel?
#%{_includedir}/fuse.h
#%{_libdir}/libfuse.a
#
# It is in kernel-misc-fuse.spec
#
# kernel-fs-fuse?
# /lib/modules/.../fuse.o*
# It is in kernel-misc-fuse.spec (fuse.o)
