Name: avr-devel
Summary: Meta package for AVR development on Fedora.
License: MIT
Version: 1.1.0
Release: 1%{?dist}
Source: avr-devel-1.1.0.tar.gz
Requires: avra avr-gcc avr-gdb avr-gcc-c++ avr-binutils avrdude avr-libc gcc-avr32-linux-gnu gcc-c++-avr32-linux-gnu binutils-avr32-linux-gnu minicom

%description
Meta package for AVR development on Fedora.

%prep
%autosetup

%install
mkdir -p %{buildroot}/etc/udev/rules.d
mv %{_builddir}/avr-devel-1.1.0/src/60-buspirate.rules %{buildroot}/etc/udev/rules.d
mv %{_builddir}/avr-devel-1.1.0/src/minirc.buspirate %{buildroot}/etc/minirc.buspirate

%files
%defattr (-,root,root,-)
/etc/udev/rules.d/60-buspirate.rules
/etc/minirc.buspirate
