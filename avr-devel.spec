Name: avr-devel
Summary: Meta package for AVR development on Fedora.
License: MIT
Version: 1.0.0
Release: 1%{?dist}
Source: avr-devel-1.0.0.tar.gz
Requires: avra avr-gcc avr-gdb avr-gcc-c++ avr-binutils avrdude avr-libc gcc-avr32-linux-gnu gcc-c++-avr32-linux-gnu binutils-avr32-linux-gnu

%description
Meta package for AVR development on Fedora.

%prep
%autosetup

%install
mkdir -p %{buildroot}/etc/udev/rules.d
mv %{_builddir}/avr-devel-1.0.0/src/60-buspirate.rules %{buildroot}/etc/udev/rules.d

%files
%defattr (-,root,root,-)
/etc/udev/rules.d/60-buspirate.rules
