Name:         kegs
License:      GPLv2
Group:        Emulators
Autoreqprov:  on
Version:      0.91
Release:      %mkrel 0.3
Summary:      Apple IIgs emulator
URL:          http://kegs.sourceforge.net/
Source:       http://kegs.sourceforge.net/%name.%version.tar.gz
Patch0:       %name.%version.dif
Patch1:       kegs-0.91-joystickpath.patch
Patch2:       kegs-0.91-crosscompile.patch
BuildRequires: X11-devel

%description
Requires ROM and disk images to work.

%prep
%setup -q -n %name.%version
%patch0 -p0
%patch1 -p1 -b .jspath~
%patch2 -p1 -b .cross~

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

AS = \$(CC)
PERL = perl

XOPTS =
EOT

make %{?jobs:-j%jobs} CC=%__cc


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
