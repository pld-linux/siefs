#
# Conditional build:
# _without_dist_kernel - build without kernel from distribution
#
Summary:	SieFS - virtual filesystem for Siemens mobile phones' memory
Summary(pl):	SieFS - wirtualny system plików do pamiêci telefonów komórkowych Siemens
Name:		siefs
Version:	0.1
Release:	1@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://mirror01.users.i.com.ua/~dmitry_z/%{name}-%{version}.tar.gz
# Source0-md5:	90ee7d5b2801e44c85fffeb9958f641e
URL:		http://mirror01.users.i.com.ua/~dmitry_z/siefs/
%{!?_without_dist_kernel:BuildRequires:	kernel-headers >= 2.4}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is SieFS - a virtual filesystem for accessing Siemens mobile
phones' memory via datacable. Now you can mount your phone to a Linux
box and browse it like a simple directory! The program is tested on
SL45, but should work also on S45/ME45/M(T)50.

%description -l pl
SieFS - wirtualny system plików udostêpniaj±cy pamiêæ telefonów
komórkowych Siemens pod³±czonych kablem. Pozwala podmontowaæ telefon
spod Linuksa i przegl±daæ go tak, jak zwyk³y katalog. Program jest
testowany na SL45, ale powinien dzia³aæ tak¿e z S45/ME45/M(T)50.

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
%doc ChangeLog NEWS README.fuse TODO
# fuse
%attr(755,root,root) %{_bindir}/fusermount
# siefs itself
%attr(755,root,root) %{_bindir}/siefs
%attr(755,root,root) %{_bindir}/slink

# -devel or fuse-devel?
#%{_includedir}/fuse.h
#%{_libdir}/libfuse.a

# kernel-fs-fuse?
# /lib/modules/.../fuse.o*
