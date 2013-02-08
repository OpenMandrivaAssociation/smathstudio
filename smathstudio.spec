%define rel 2

%{?dist: %{expand: %%define %dist 1}}

Summary: Small mathematic packet with MathCad style
Name: smathstudio
Version: 0.89
Release: %mkrel %{rel}
License: EULA
Group: Sciences/Mathematics
URL: http://ru.smath.info/forum/default.aspx?g=posts&t=130

Source0: SMathStudioDesktop.0_89.Mono.tar.gz
Source1: SSLogo48.png
#Source2: Text_RUS.lang

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#Obsoletes: smathstudio < %{version}
Requires: mono, mono-winforms

%description
A free mathematical package with a graphical interface for the calculation 
of mathematical expressions, and constructing two-dimensional and
three-dimensional graphs.

%build
%prep
%setup -q -n SMathStudioDesktop.0_89.Mono

%pre
rm -f %{_bindir}/smathstudio

%post
gzip -d /opt/%{name}-%{version}/lang/*.gz
gzip -d /opt/%{name}-%{version}/examples/*.gz
gzip -d /opt/%{name}-%{version}/book/*.gz
gzip -d /opt/%{name}-%{version}/plugins/*.gz

%postun
rm -rf /opt/%{name}-%{version}

%install
mkdir -p %{buildroot}/opt
mkdir %{buildroot}/opt/%{name}-%{version}
mkdir %{buildroot}/opt/%{name}-%{version}/book
mkdir %{buildroot}/opt/%{name}-%{version}/lang
mkdir %{buildroot}/opt/%{name}-%{version}/examples
mkdir %{buildroot}/opt/%{name}-%{version}/plugins

mkdir %{buildroot}/usr
mkdir %{buildroot}/usr/bin
mkdir %{buildroot}/usr/share
mkdir %{buildroot}/usr/share/applications
#cp -a lang %{buildroot}/opt/%{name}-%{version}/
#cp -a examples %{buildroot}/opt/%{name}-%{version}/
#cp -a book %{buildroot}/opt/%{name}-%{version}/
install -Dm644 *.pc %{buildroot}/opt/%{name}-%{version}/
install -Dm755 *.dll %{buildroot}/opt/%{name}-%{version}/
install -Dm755 *.exe %{buildroot}/opt/%{name}-%{version}/
gzip lang/*
gzip book/*
gzip examples/*
gzip plugins/*
cp lang/* %{buildroot}/opt/%{name}-%{version}/lang
cp book/* %{buildroot}/opt/%{name}-%{version}/book
cp examples/* %{buildroot}/opt/%{name}-%{version}/examples
cp plugins/* %{buildroot}/opt/%{name}-%{version}/plugins

install -Dm644 %{SOURCE1} %{buildroot}/opt/%{name}-%{version}/SSLogo48.png
echo "//// SMath Studio 0.88" >> %{buildroot}/opt/%{name}-%{version}/settings.inf
echo "Language=RUS" >> %{buildroot}/opt/%{name}-%{version}/settings.inf


chmod 666 %{buildroot}/opt/%{name}-%{version}/settings.inf

install -dm 755 %{buildroot}%{_datadir}/applications
cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=SMath Studio Desktop
GenericName[ru]=SMath Studio Desktop
Name=SMathStudio
Name[ru]=SMathStudio
Exec=%{_bindir}/smathstudio_mono
Comment=mathematical editor with MathCad style
Icon=/opt/smathstudio-%{version}/SSLogo48.png
Type=Application
Categories=Education;Math;
EOF
install -m 0644 %{name}.desktop \
%{buildroot}%{_datadir}/applications/%{name}.desktop

install -dm 755 %{buildroot}%{_bindir}
cat > smathstudio_mono << EOF
#!/bin/sh
exec mono "/opt/%{name}-%{version}/SMathStudio_Desktop.exe" "\$@"
exit
EOF

install -m 7655 smathstudio_mono \
%{buildroot}%{_bindir}/smathstudio_mono

%clean
rm -rf %{buildroot}
%files
%defattr(-,root, root)

/opt/%{name}-%{version}
%{_bindir}/smathstudio_mono
%{_datadir}/applications/smathstudio.desktop



%changelog
* Sat Jul 23 2011 Александр Казанцев <kazancas@mandriva.org> 0.89-1mdv2011.0
+ Revision: 691160
- imported package smathstudio
- Created package structure for smathstudio.

