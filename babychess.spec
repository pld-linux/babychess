Summary:	BabyChess - a chess program
Summary(pl):	BabyChess - program do gry w szachy
Name:		babychess
Version:	14.1
Release:	2
Epoch:		0
License:	GPL
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~kunegis/babychess/download/%{name}-%{version}.tar.bz2
# Source0-md5:	4d63c534dabfa7dda87ccea77ce45198
URL:		http://user.cs.tu-berlin.de/~kunegis/babychess/
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-desktop.patch
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BabyChess is a chess program. You can edit chess games, play chess on
the internet, and play locally against engines.

%description -l pl
BabyChess jest programem do gry w szachy. Mo¿liwa jest edycja stanu
gry, gra poprzez internet, oraz gra z komputerem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	gcc="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -D_GNU_SOURCE -DNDEBUG -fno-implicit-inline-templates -fno-rtti -fno-inline-functions `gtk-config --cflags`" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
#mv -f "$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Games/*.desktop" $RPM_BUILD_ROOT%{_desktopdir}
#mv "$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Games/BabyChess Game Archive.desktop" $RPM_BUILD_ROOT%{_desktopdir}
#mv "$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Games/BabyChess Game.desktop" $RPM_BUILD_ROOT%{_desktopdir}

for i in "$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Games/*"
do
	mv -f $i $RPM_BUILD_ROOT%{_desktopdir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README LICENSING
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_datadir}/baby
