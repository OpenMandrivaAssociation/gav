%define name	gav
%define	tver	0.7.3
%define version 0.9.0
%define release %mkrel 3
%define	Summary	GPL Arcade Volleyball

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}

Source0:	http://puzzle.dl.sourceforge.net/sourceforge/gav/%{name}-%{version}.tar.bz2
Source1:	%{name}-themes-%{tver}.tar.bz2
Source11:	%{name}16.png
Source12: 	%{name}32.png
Source13: 	%{name}48.png
URL:		http://gav.sourceforge.net/
License:	GPL
Group:		Games/Sports
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel SDL_image-devel SDL_net-devel

%description
An SDL-based rendition of an old favorite CGA game featuring
two characters playing a volleyball-like game. This "revamped"
version is supposed to support theming, multiplayer games,
different input devices and networking (not yet).

This package contains all available themes as well.

%prep
%setup -q -a1

%build
%make depend CXXFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags` -I`pwd`/menu  -I`pwd`/automa  -I`pwd`/net -I`pwd`"
make CXXFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags` -I`pwd`/menu  -I`pwd`/automa  -I`pwd`/net -I`pwd`"
										
%install
rm -rf $RPM_BUILD_ROOT

install -m755 %{name} -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
install -m755 -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/themes
cp -r themes/* $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/themes

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=2-D Volleyball
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

#icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README CHANGELOG
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png



