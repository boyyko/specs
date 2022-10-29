Name: xfel
Version: 1.2.9
Release: alt2

Summary: Tiny FEL tools for Allwinner SOC
License: MIT License
Group: Development/Tools

Url: https://github.com/xboot/xfel
Source: xfel-1.2.9.tar.gz

BuildRequires: libusb-devel

%description
FEL is a low-level subroutine contained in the BootROM on Allwinner devices. It is used for initial programming and recovery of devices using USB

%prep
%setup -n xfel-%version

%build 
%make_build

%install
%{__install} -p %{name} %{buildroot}/usr/local/bin/

%files
%_usr/local/bin/xfel
%_usr/etc/udev/rules.d/99-xfel.rules
%_usr/share/licenses/xfel/LICENSE



%changelog
* Sat Oct 29 2022 Egor Boyko <nit@altlinux.org> 1.2.9-alt2
- Initial release
- Version 1.2.9

