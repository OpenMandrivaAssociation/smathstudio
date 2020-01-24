%define debug_package %{nil}

Summary: Small mathematic packet with MathCad style

Name: smathstudio
Version: 0.99.7030
Release: 1
License: EULA
Group: Sciences/Mathematics
URL: http://ru.smath.info/forum/default.aspx?g=posts&t=130

Source0: https://smath.com/file/5TGzK/SMathStudioDesktop.0_99_7030.Mono.tar.gz
Source1: SSLogo48.png
#Source2: Text_RUS.lang
Source100:	smathstudio.rpmlintrc

#Obsoletes: smathstudio < %{version}
Requires: mono, mono-winforms

%description
A free mathematical package with a graphical interface for the calculation 
of mathematical expressions, and constructing two-dimensional and
three-dimensional graphs.

%build
%prep
%setup -q -n SMathStudioDesktop.0_99_7030.Mono

%pre
rm -f %{_bindir}/smathstudio

%post
gzip -d %{_datadir}/%{name}-%{version}/lang/*.gz
gzip -d %{_datadir}/%{name}-%{version}/examples/*.gz
gzip -d %{_datadir}/%{name}-%{version}/book/*.gz
gzip -d %{_datadir}/%{name}-%{version}/plugins/*.gz

%postun
rm -rf %{_datadir}/%{name}-%{version}

%install
mkdir -p %{buildroot}/%{_datadir}
mkdir %{buildroot}/%{_datadir}/%{name}-%{version}
mkdir %{buildroot}/%{_datadir}/%{name}-%{version}/book
mkdir %{buildroot}/%{_datadir}/%{name}-%{version}/lang
mkdir %{buildroot}/%{_datadir}/%{name}-%{version}/examples
mkdir %{buildroot}/%{_datadir}/%{name}-%{version}/plugins

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
#cp -a lang %{buildroot}/opt/%{name}-%{version}/
#cp -a examples %{buildroot}/opt/%{name}-%{version}/
#cp -a book %{buildroot}/opt/%{name}-%{version}/
#install -Dm644 *.pc %{buildroot}/%{_datadir}/%{name}-%{version}/
install -Dm755 *.dll %{buildroot}/%{_datadir}/%{name}-%{version}/
install -Dm755 *.exe %{buildroot}/%{_datadir}/%{name}-%{version}/
gzip lang/*
gzip book/*
gzip examples/*
gzip plugins/*
chmod a-x lang/*
chmod a-x book/*
chmod a-x examples/*
chmod a-x plugins/*
cp lang/* %{buildroot}/%{_datadir}/%{name}-%{version}/lang
cp book/* %{buildroot}/%{_datadir}/%{name}-%{version}/book
cp examples/* %{buildroot}/%{_datadir}/%{name}-%{version}/examples
cp plugins/* %{buildroot}/%{_datadir}/%{name}-%{version}/plugins

install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/%{name}-%{version}/SSLogo48.png
echo "//// SMath Studio 0.88" >> %{buildroot}/%{_datadir}/%{name}-%{version}/settings.inf
echo "Language=RUS" >> %{buildroot}/%{_datadir}/%{name}-%{version}/settings.inf


chmod 666 %{buildroot}/%{_datadir}/%{name}-%{version}/settings.inf

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
exec mono "%{_datadir}/%{name}-%{version}/SMathStudio_Desktop.exe" "\$@"
exit
EOF

install -m 7655 smathstudio_mono \
%{buildroot}%{_bindir}/smathstudio_mono

%clean

%files
%{_datadir}/%{name}-%{version}
%{_bindir}/smathstudio_mono
%{_datadir}/applications/smathstudio.desktop

