
#
# _without_dist_kernel - build without kernel from distribution.

Summary:	
Summary(pl):	
Name:		siefs
Version:	0.1
Release:	1@%{_kernel_ver_str}
Copyright:	GPL
Group:		Base/Kernel
Source0:	http://mirror01.users.i.com.ua/~dmity_z/%{name}-%{version}.tar.gz
#BuildRequires:
#Requires:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
