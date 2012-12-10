%define name	gav
%define	tver	0.7.3
%define version 0.9.0
%define release %mkrel 8
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
Patch0:		gav-0.9.0-mdv-fix-gcc-4.3.patch
URL:		http://gav.sourceforge.net/
License:	GPLv2+
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
%patch0 -p1 -b .gcc43

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





%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-8mdv2011.0
+ Revision: 610819
- rebuild

* Mon Dec 07 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 0.9.0-7mdv2010.1
+ Revision: 474277
- fix build with gcc >= 4.3
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 Emmanuel Andry <eandry@mandriva.org> 0.9.0-3mdv2008.0
+ Revision: 83532
- drop old menu


* Wed Sep 13 2006 Nicolas L√©cureuil <neoclust@mandriva.org>
+ 2006-09-12 09:05:47 (61027)
- migrate to XDG

* Fri Aug 04 2006 Nicolas L√©cureuil <neoclust@mandriva.org>
+ 2006-08-03 03:44:52 (43098)
- import gav-0.9.0-1mdv2007.0

* Sun May 28 2006 Emmanuel Andry <eandry@mandriva.org> 0.9.0-1mdk
- 0.9.0

* Tue Jul 05 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.8.0-3mdk
- Rebuild
- %%{1}mdv2007.0
- Make rpmbuildupdate friendly

* Thu Jun 17 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.0-2mdk
- rebuild

* Thu Apr 15 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.0-1mdk
- 0.8.0

* Thu Feb 05 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.3-1mdk
- 0.7.3
- correct name in menu item
- cleanups
- move binary to /usr/games
- compile with $RPM_OPT_FLAGS

