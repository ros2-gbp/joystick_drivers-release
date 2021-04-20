%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-wiimote
Version:        3.0.0
Release:        5%{?dist}%{?release_suffix}
Summary:        ROS wiimote package

License:        GPL
URL:            http://www.ros.org/wiki/wiimote
Source0:        %{name}-%{version}.tar.gz

Requires:       bluez-libs
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-components
Requires:       ros-galactic-rclcpp-lifecycle
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-std-srvs
Requires:       ros-galactic-wiimote-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  bluez-libs-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-cmake-auto
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-components
BuildRequires:  ros-galactic-rclcpp-lifecycle
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-std-srvs
BuildRequires:  ros-galactic-wiimote-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The wiimote package allows ROS nodes to communicate with a Nintendo Wiimote and
its related peripherals, including the Nunchuk, Motion Plus, and
(experimentally) the Classic. The package implements a ROS node that uses
Bluetooth to communicate with the Wiimote device, obtaining accelerometer and
gyro data, the state of LEDs, the IR camera, rumble (vibrator), buttons,
joystick, and battery state. The node additionally enables ROS nodes to control
the Wiimote's LEDs and vibration for feedback to the human Wiimote operator.
LEDs and vibration may be switched on and off, or made to operate according to a
timed pattern.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Apr 20 2021 Jonathan Bohren <jbo@jhu.edu> - 3.0.0-5
- Autogenerated by Bloom

* Fri Mar 26 2021 Jonathan Bohren <jbo@jhu.edu> - 3.0.0-4
- Autogenerated by Bloom

* Tue Mar 16 2021 Jonathan Bohren <jbo@jhu.edu> - 3.0.0-3
- Autogenerated by Bloom

* Fri Mar 12 2021 Jonathan Bohren <jbo@jhu.edu> - 3.0.0-2
- Autogenerated by Bloom

