Summary:	BabyChess is a chess program.
Summary(pl):	Program do gry w szachy.
Name:		babychess
Version:	14.1
Release:	1
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BabyChess is a chess program. You can edit chess games, play chess on
the internet, and play locally against engines.

%description -l pl
BabyChess jest programem do gry w szachy. Mo�liwa jest edycja stanu
gry, gra poprzez internet, oraz gra z komputerem.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_desktopdir}
mv "$RPM_BUILD_ROOT%{_applnkdir}/Games/BabyChess Server.desktop" $RPM_BUILD_ROOT/%{_desktopdir}
mv "$RPM_BUILD_ROOT%{_applnkdir}/Games/BabyChess Game Archive.desktop" $RPM_BUILD_ROOT/%{_desktopdir}
mv "$RPM_BUILD_ROOT%{_applnkdir}/Games/BabyChess Game.desktop" $RPM_BUILD_ROOT/%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README LICENSING
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_datadir}/baby