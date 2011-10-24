Name:         kegs
License:      COPYRIGHT
Group:        Emulators
Autoreqprov:  on
Version:      0.91
Release:      %mkrel 0.2
Summary:      Apple IIgs emulator
Source:       %name.%version.tar.gz
Patch0:       %name.%version.dif
BuildRequires: X11-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
Requires ROM and disk images to work.

%prep
%setup -q -n %name.%version
%patch0 -p0

%build
# build section
cd src
rm -f vars
cat <<EOT >vars
TARGET = xkegs
OBJECTS = \$(OBJECTS1) xdriver.o
CCOPTS = $RPM_OPT_FLAGS
%ifarch %ix86 x86_64 %arm ia64
OPTS = -DKEGS_LITTLE_ENDIAN -DNDEBUG
%else
OPTS = -DNDEBUG
%endif
SUFFIX =
NAME = xkegs
LDFLAGS =
LDOPTS =
LD = \$(CC)
EXTRA_LIBS = -lXext
EXTRA_SPECIALS =

AS = cc
PERL = perl

XOPTS =
EOT

make %{?jobs:-j%jobs}


%install
# install section
install -D -m 755 xkegs $RPM_BUILD_ROOT/%{_bindir}/xkegs
install -D -m 644 config.kegs $RPM_BUILD_ROOT/%{_datadir}/%{name}/config.kegs
chmod 755 $RPM_BUILD_ROOT%{_bindir}/xkegs

%files
%defattr(-,root,root)
# %{_docdir}/%{name}/*.txt
# %{_bindir}/kegs
%{_bindir}/xkegs
%{_datadir}/%{name}/config.kegs
# %{_sysconfdir}/default.config.kegs
