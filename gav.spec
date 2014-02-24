%define tver 0.7.3

Summary:	Arcade volleyball
Name:		gav
Version:	0.9.0
Release:	9
License:	GPLv2+
Group:		Games/Sports
Url:		http://gav.sourceforge.net/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/gav/%{name}-%{version}.tar.bz2
Source1:	%{name}-themes-%{tver}.tar.bz2
Source11:	%{name}16.png
Source12:	%{name}32.png
Source13:	%{name}48.png
Patch0:		gav-0.9.0-mdv-fix-gcc-4.3.patch
Patch1:		gav-0.9.0-no-strip.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_net)

%description
An SDL-based rendition of an old favorite CGA game featuring
two characters playing a volleyball-like game. This "revamped"
version is supposed to support theming, multiplayer games,
different input devices and networking (not yet).

This package contains all available themes as well.

%files
%doc README CHANGELOG
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q -a1
%patch0 -p1 -b .gcc43
%patch1 -p1

%build
%make depend CXXFLAGS="%{optflags} `sdl-config --cflags` -I`pwd`/menu  -I`pwd`/automa  -I`pwd`/net -I`pwd`"
make CXXFLAGS="%{optflags} `sdl-config --cflags` -I`pwd`/menu  -I`pwd`/automa  -I`pwd`/net -I`pwd`"

%install
install -m755 %{name} -D %{buildroot}%{_gamesbindir}/%{name}
install -m755 -d %{buildroot}%{_gamesdatadir}/%{name}/themes
cp -r themes/* %{buildroot}%{_gamesdatadir}/%{name}/themes

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=2D Volleyball
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

#icons
install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

