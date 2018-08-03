%global debug_package %{nil}
%global _iconsdir /usr/share/icons

%global gitdate 20180802
%global commit0 d8cfab12bb7a64694a9fdcf76440c443f7e84802
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           attract
Version:        2.4
Release:        1%{?dist}
Summary:        Graphical frontend for command line emulators
Group:          Applications/Emulators
License:        GPLv3+
URL:            http://attractmode.org
Source0:	https://github.com/mickelson/attract/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	https://github.com/mickelson/attract/releases/download/v1.6.2/ATTRACT.MODE.intro.16-9.v6.1080p.mp4
Source2:	https://github.com/mickelson/attract/releases/download/v1.6.2/ATTRACT.MODE.intro.4-3.v6.1080p.mp4
Patch0:         attract-2.3.0-makefile.patch

BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sfml-graphics)
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
BuildRequires:  pkgconfig(sfml-window)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel
BuildRequires:	libjpeg-turbo-devel 
Recommends:	mame

%description
Attract-Mode is a graphical frontend for command line emulators such as
MAME, MESS, and Nestopia. It hides the underlying operating system and
is intended to be controlled with a joystick, gamepad or spin dial,
making it ideal for use in arcade cabinet setups.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

install -D -m644 util/icon.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Attract-Mode
Comment=Graphical frontend for command line emulators
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Game;Emulator;
EOF

#Intro
install -Dm644 %{S:1} %{buildroot}/%{_datadir}/%{name}/intro/intro.mp4
install -Dm644 %{S:2} %{buildroot}/%{_datadir}/%{name}/intro/intro_4x3.mp4

%files
%doc Layouts.md Readme.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/512x512/apps/%{name}.png


%changelog

* Thu Aug 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4-1 
- Updated to 2.4

* Wed Aug 01 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.3.0-4 
- Upstream

* Wed May 30 2018 akien <akien> 2.3.0-3.mga7
  (not released yet)
+ Revision: 1233088
- Rebuild for SFML 2.5.0

* Sun Apr 29 2018 daviddavid <daviddavid> 2.3.0-2.mga7
+ Revision: 1223469
- add upstream patch to fix build with ffmpeg 4.0

* Sat Dec 30 2017 akien <akien> 2.3.0-1.mga7
+ Revision: 1187622
- Version 2.3.0

* Tue May 02 2017 akien <akien> 2.2.1-3.mga6
+ Revision: 1098266
- Rebuild for ffmpeg 3.3

* Wed Mar 08 2017 akien <akien> 2.2.1-2.mga6
+ Revision: 1089835
- Rebuild for ffmpeg 3.2.4

* Mon Jan 09 2017 akien <akien> 2.2.1-1.mga6
+ Revision: 1080812
- Version 2.2.1

* Sun Nov 13 2016 akien <akien> 2.2.0-1.mga6
+ Revision: 1067056
- Version 2.2.0

* Sat Oct 08 2016 akien <akien> 2.1.0-1.mga6
+ Revision: 1059581
- Version 2.1.0

* Sun Apr 03 2016 akien <akien> 2.0.0-0.rc3.1.mga6
+ Revision: 997868
- Add desktop file and icon
- imported package attract

