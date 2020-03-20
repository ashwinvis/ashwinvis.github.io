Back to Arch Linux
##################

:author: Ashwin Vishnu Mohanan
:date: 2020-01-03T10:00:41.042526
:modified: 2020-01-13
:slug: back-to-arch-linux
:status: published
:summary: Within a Ubuntu LTS pre-installed laptop
:category: Tech Talk
:tags: software, linux, ubuntu, archlinux

Why
---
It was October 2019. New job, new laptop.

I tried to tell myself to stay with the LTS that was given to me from the
Canonical and Dell overlords. To be honest, I did not remove Ubuntu from the
get-go was because I was unsure if I can run Nvidia's CUDA toolkit on an
unlisted_ OS. In my old laptop (2011-2014) on which I had a Nvidia GPU and
which ran Manjaro, I would frequently total my installation every time I ran
``pacman -Syu``. The X.org display server would just stop functioning and I
would be left with a terminal to figure out how to get back.

.. _unlisted: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64/

I thought I could just weed out the bloatware (Google Chrome, Amazon etc.)
and be content with what I have. Trust the Ubuntu and Dell repositories.

Fast-forward to January 2020.  Turns out, the project which I am on right now
may not get started with CUDA development soon. Therefore, a good OS and GCC
compiler toolchain is all that I need. I have a mutant Ubuntu LTS already with
all the hacks under the sun to stay up-to-date:

- pyenv_ to have the latest Python
- flatpak_ to install some applications which are *ancient* in the official `Ubuntu repos`_ (Okular, Signal, KeepassXC, Zeal, Zotero etc.)
- appimage_ when flatpak_'s sandbox is too restrictive (Neovim)
- PPA_ / unofficial ``.deb`` packages from GitHub when the start-up overhead of
  flatpak_ or appimage_ is way too high (Neovim, again 😅) or similar reasons
  as above (Nextcloud client, VSCodium etc.)

This is not good at all, I hear you. And I have to wait a good `4 more months`_
for the next LTS release! The final blow came when I saw Vim 8.2 was released
last month with popup_ support, and I do not have it yet! There is no practical
way (apart from yet another PPA_) to get the latest Vim, without compiling it
from source. Either ways, it is also unacceptable to run a desktop environment
(GNOME) which is lagging behind (version 3.28.2) the latest stable release
(version 3.34) for so long!

.. _pyenv: https://github.com/pyenv/pyenv/
.. _flatpak: https://flatpak.org/
.. _Ubuntu repos: https://packages.ubuntu.com/
.. _appimage: https://appimage.org/
.. _PPA: https://help.ubuntu.com/community/PPA
.. _4 more months: https://www.omgubuntu.co.uk/2019/10/ubuntu-20-04-release-features
.. _popup: https://github.com/skywind3000/vim-quickui

How
---

.. note-danger::

  Make sure you understand what how ``chroot`` and ``mount`` commands work.
  Also do not run ``rm -rf`` at any stage below.

There is a nice guide_ which demonstrates how to setup Arch Linux from an
existing Linux OS. I started off by downloading_ the bootstrap image along with
the GPG signature and verifying it::

  $ gpg --keyserver-options auto-key-retrieve --verify archlinux-2020.01.01-x86_64.iso.sig
  gpg: assuming signed data in 'archlinux-2020.01.01-x86_64.iso'
  gpg: Signature made Wed 01 Jan 2020 06:21:41 AM CET
  gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
  gpg: Good signature from "Pierre Schmitz <pierre@archlinux.de>" [unknown]
  gpg: WARNING: This key is not certified with a trusted signature!
  gpg:          There is no indication that the signature belongs to the owner.
  Primary key fingerprint: 4AA4 767B BC9C 4B1D 18AE  28B7 7F2D 434B 9741 E8AC

The key fingerprint was cross-checked_ to be doubly sure.
Then I extracted the bootstrap image::

  $ sudo su
  # tar xzf archlinux-bootstrap-2020.01.01-x86_64.tar.gz -C /tmp

When I skipped a few steps and went into the ``chroot``, I got this::

  # /tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/
  ==> WARNING: /mnt/archlinux/root.x86_64/ is not a mountpoint. This may have undesirable side effects.

I understood_ that the ``chroot`` should be a mount point::

  # mount --bind /tmp/root.x86_64 /tmp/root.x86_64
  # /tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/

And the ``chroot`` worked without any warnings. To clarify the shell I am
running I will prefix the commands with ``[chroot] #`` from here on::

  [chroot] # pacman-key --init
  [chroot] # pacman-key --populate archlinux

After editing the mirror list outside of the ``chroot``::

  $ sudoedit /tmp/root.x86_64/etc/pacman.d/mirrorlist

I updated the bootstrap::

  [chroot] # pacman -Syyu

And mounted the partitions to be bootstrapped::

  [chroot] # mount /dev/nvme0n1p5 /mnt
  [chroot] # mount /dev/nvme0n1p4 /mnt/home
  [chroot] # genfstab -U /mnt >> /mnt/etc/fstab
  [chroot] # umount /mnt/home

.. note-info::

  In preparation, I had created these partitions by shrinking the existing ones
  with a GParted_ USB live medium, long time ago.  The home partition was also
  created and made separate such that it can be shared between Ubuntu and Arch
  Linux for a dual-boot setup.

and installed some essentials::

  [chroot] # pacman -S base base-devel
  :: There are 24 members in group base-devel:
  :: Repository core
     1) autoconf  2) automake  3) binutils  4) bison  5) fakeroot  6) file
     7) findutils  8) flex  9) gawk  10) gcc  11) gettext  12) grep  13) groff
     14) gzip  15) libtool  16) m4 17) make  18) pacman  19) patch  20) pkgconf
     21) sed  22) sudo  23) texinfo  24) which
  ...

Did the same for the target Arch Linux partition mounted at ``/mnt``::

  [chroot] # pacstrap /mnt base base-devel
  [chroot] # pacstrap /mnt linux-lts linux-firmware intel-ucode lsb-release

Thereafter I followed the official `installation guide`_::

  [chroot] # arch-chroot /mnt

.. note-info::

  The step above runs ``arch-chroot`` from within a ``chroot``. Now, I see why
  Leo was so confused in Inception. Whenever in doubt, run ``df``.

.. _downloading: https://www.archlinux.org/download/
.. _guide: https://wiki.archlinux.org/index.php/Install_Arch_Linux_from_existing_Linux#From_a_host_running_another_Linux_distribution
.. _cross-checked: https://www.archlinux.org/master-keys/
.. _Gparted: https://distrowatch.com/table.php?distribution=gparted
.. _Disks: https://wiki.gnome.org/Apps/Disks
.. _understood: https://bugs.archlinux.org/task/46169
.. _installation guide: https://wiki.archlinux.org/index.php/Installation_guide#Configure_the_system

Cleaning up and dual booting
----------------------------
Exit the ``chroot`` and unmount everything::

  [chroot in a chroot] # exit
  [chroot] # exit
  # umount -R /tmp/root.x86_64

The Ubuntu installation came with a GRUB_ boot loader and ``os-loader`` package
which should detect the new Arch Linux installation (since we installed the
``lsb-release`` package). To make it happen, reboot? from Ubuntu run::

  # sudo update-grub

That did not work! `Turns out`_ ``/etc/default/grub`` had two offending lines::

  GRUB_TIMEOUT_STYLE=hidden
  GRUB_DISABLE_OS_PROBER=true

which when commented out, it started working. Follow this by ``update-grub`` or
``grub-mkconfig -o /boot/grub/grub.cfg`` and it is good to go.

.. _GRUB: https://wiki.archlinux.org/index.php/GRUB#Detecting_other_operating_systems
.. _Turns out: https://askubuntu.com/questions/111085/how-do-i-hide-the-grub-menu-showing-up-at-the-beginning-of-boot

Epilogue: some personal choices
-------------------------------
What follows below are not necessary but I note it down for future reference.
Here are the packages I chose to install::

  neovim vim code  # editors
  plasma kdegraphics-thumbnailers # KDE desktop meta package
  konsole
  acpi
  inetutils  # many network commands, including hostname
  openssh
  parted  # partitioning tool
  xonsh zsh # alternatives to bash
  tlp  # CPU and FAN governor
  man-db  # man pages
  arch-wiki-docs  # provides wiki-search
  arch-wiki-lite  # and wiki-search-html commands
  ttf-joypixels ttf-roboto adobe-source-sans-pro-fonts adobe-source-serif-pro-fonts ttf-arphic-uming terminus-font  # extra fonts
  libreoffice-fresh  # writer, calc, impress...
  gcc-fortran gcc-go rust  # compilers
  pacman-contrib reflector  # pacman utilities
  firefox thunderbird zeal okular ark nextcloud-client mplayer  # ... and more applications
  flatpak  # for sandboxing non-free applications

An AUR helper::

  $ git clone https://aur.archlinux.org/yay.git
  $ cd yay && makepkg -s
  # pacman -U /home/avmo/.cache/makepkg/yay-*

Check and activate periodic TRIM_ for long-term performance::

  $ lsblk --discard
  NAME        DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
  nvme0n1            0      512B       2T         0
  |-nvme0n1p1        0      512B       2T         0
  |-nvme0n1p2        0      512B       2T         0
  |-nvme0n1p3        0      512B       2T         0
  |-nvme0n1p4        0      512B       2T         0
  |-nvme0n1p5        0      512B       2T         0
  `-nvme0n1p6        0      512B       2T         0

  # systemctl enable fstrim.timer
  Created symlink /etc/systemd/system/timers.target.wants/fstrim.timer → /usr/lib/systemd/system/fstrim.timer.

Format a swap_ partition in the empty space available and mount it with TRIM_
(``discard``) support::

  # parted /dev/nvme0n1
  GNU Parted 3.3
  Using /dev/nvme0n1
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) print
  Model: KXG60ZNV512G NVMe TOSHIBA 512GB (nvme)
  Disk /dev/nvme0n1: 512GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number  Start   End     Size    File system  Name                  Flags
   1      1049kB  819MB   818MB   fat32        EFI system partition  boot, esp
   2      819MB   6188MB  5369MB  fat32        Basic data partition  msftres
   3      6188MB  140GB   134GB   ext4
   4      194GB   301GB   107GB   btrfs
   5      405GB   512GB   107GB   ext4

  (parted) mkpart primary linux-swap 140GB 194GB
  (parted) print
  Model: KXG60ZNV512G NVMe TOSHIBA 512GB (nvme)
  Disk /dev/nvme0n1: 512GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number  Start   End     Size    File system     Name                  Flags
   1      1049kB  819MB   818MB   fat32           EFI system partition  boot, esp
   2      819MB   6188MB  5369MB  fat32           Basic data partition  msftres
   3      6188MB  140GB   134GB   ext4
   6      140GB   194GB   53.7GB  linux-swap(v1)  primary
   4      194GB   301GB   107GB   btrfs
   5      405GB   512GB   107GB   ext4

  (parted) quit
  # mkswap /dev/nvme0n1p6
  Setting up swapspace version 1, size = 50 GiB (53687087104 bytes)
  no label, UUID=6ce1daf4-6a66-44a8-a14b-bd4ea3eb9c40
  # swapon --discard
  # echo "UUID=6ce1daf4-6a66-44a8-a14b-bd4ea3eb9c40 none swap defaults,discard 0 0" >> /etc/fstab

Installed an alternative shell (as listed in ``/etc/shells``) and added myself
as a user::

  # useradd --no-create-home --uid 1001 --user-group avmo --shell /usr/bin/xonsh
  # passwd avmo

Then to make the desktop and essential components appear::

  # systemctl enable sddm NetworkManager tlp

Configure sensors from ``lm_sensors``::

  # sensors-detect
  # sensors
  Adapter: ISA adapter
  Package id 0:  +45.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 0:        +45.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 1:        +44.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 2:        +44.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 3:        +47.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 4:        +42.0°C  (high = +100.0°C, crit = +100.0°C)
  Core 5:        +42.0°C  (high = +100.0°C, crit = +100.0°C)

  dell_smm-virtual-0
  Adapter: Virtual device
  fan1:        2288 RPM
  fan2:        2317 RPM

  pch_cannonlake-virtual-0
  Adapter: Virtual device
  temp1:        +55.0°C

  acpitz-acpi-0
  Adapter: ACPI interface
  temp1:        +25.0°C  (crit = +107.0°C)

  iwlwifi-virtual-0
  Adapter: Virtual device
  temp1:        +48.0°C

  BAT0-acpi-0
  Adapter: ACPI interface
  in0:          12.80 V
  curr1:       1000.00 uA

.. _TRIM: https://wiki.archlinux.org/index.php/Solid_state_drive#TRIM
.. _swap: https://wiki.archlinux.org/index.php/Swap

Nvidia
------

The riskiest part, IMHO, although it is well documented_. The driver package
depends on the GPU model and the kernel. Thankfully no kernel panic occurred by
installing::

  # pacman -S nvidia xorg-xrandr

.. note::

  If anything goes wrong, it often helped by simply clearing up
  ``/etc/X11/xorg.conf.d``.

Option 1: Nvidia alone
~~~~~~~~~~~~~~~~~~~~~~

Tried::

  # nvidia-xconfig

However, SDDM did not start when X server was configured to use ``nvidia``
display driver. The key was to run some commands `before SDDM`_ starts, with
the following lines in ``/usr/share/sddm/scripts/Xsetup``.

.. code:: bash

  xrandr --setprovideroutputsource modesetting NVIDIA-0
  xrandr --auto

.. _before SDDM: https://wiki.archlinux.org/index.php/NVIDIA_Optimus#SDDM

Option 2: Optimus Prime
~~~~~~~~~~~~~~~~~~~~~~~

After reading a bit more, I chose NOT to do Option 1, but instead go for
switchable_ graphics. The following package provides a ``prime-run`` command
and a X server configuration::

  # pacman -S nvidia-prime

Rebooted and verified it::

  $ xrandr --listproviders
  Providers: number : 2
  Provider 0: id: 0x48 cap: 0xf, Source Output, Sink Output, Source Offload, Sink Offload crtcs: 3 outputs: 6 associated providers: 0 name:modesetting
  Provider 1: id: 0x2a3 cap: 0x0 crtcs: 0 outputs: 0 associated providers: 0 name:NVIDIA-G0

  # pacman -S mesa-demos
  $ prime-run glxinfo | grep OpenGL

Finally
~~~~~~~

There was a small hiccup_ in detecting the external HDMI monitor. Turns out it
was regression_ due to a change in ``nvidia-utils``. It was fixed by adding
back the line::

  Option "PrimaryGPU" "yes"

to ``/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf``.

CUDA
----
Installation_::

  # pacman -S cuda

Testing::

  $ cp -r /opt/cuda/samples/ .
  $ cd samples/1_Utilities/deviceQuery
  $ make
  $ ./deviceQuery
  ./deviceQuery Starting...

   CUDA Device Query (Runtime API) version (CUDART static linking)

  Detected 1 CUDA Capable device(s)

  Device 0: "Quadro RTX 3000"
    CUDA Driver Version / Runtime Version          10.2 / 10.2
    CUDA Capability Major/Minor version number:    7.5
    Total amount of global memory:                 5935 MBytes (6222839808 bytes)
    (30) Multiprocessors, ( 64) CUDA Cores/MP:     1920 CUDA Cores
    GPU Max Clock rate:                            1380 MHz (1.38 GHz)
    Memory Clock rate:                             7001 Mhz
    Memory Bus Width:                              192-bit
    L2 Cache Size:                                 3145728 bytes
    Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
    Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
    Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
    Total amount of constant memory:               65536 bytes
    Total amount of shared memory per block:       49152 bytes
    Total number of registers available per block: 65536
    Warp size:                                     32
    Maximum number of threads per multiprocessor:  1024
    Maximum number of threads per block:           1024
    Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
    Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
    Maximum memory pitch:                          2147483647 bytes
    Texture alignment:                             512 bytes
    Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
    Run time limit on kernels:                     Yes
    Integrated GPU sharing Host Memory:            No
    Support host page-locked memory mapping:       Yes
    Alignment requirement for Surfaces:            Yes
    Device has ECC support:                        Disabled
    Device supports Unified Addressing (UVA):      Yes
    Device supports Compute Preemption:            Yes
    Supports Cooperative Kernel Launch:            Yes
    Supports MultiDevice Co-op Kernel Launch:      Yes
    Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
    Compute Mode:
       < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

  deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 10.2, CUDA Runtime Version = 10.2, NumDevs = 1
  Result = PASS


.. _documented: https://wiki.archlinux.org/index.php/NVIDIA
.. _key: https://wiki.archlinux.org/index.php/NVIDIA_Optimus#SDDM
.. _switchable: https://wiki.archlinux.org/index.php/NVIDIA_Optimus#Using_PRIME_render_offload
.. _hiccup: https://bbs.archlinux.org/viewtopic.php?id=251919
.. _regression: https://git.archlinux.org/svntogit/packages.git/commit/trunk?h=packages/nvidia-utils&id=65ce50c4fd7388e91987cd2d271881e4ae126902
.. _Installation: https://wiki.archlinux.org/index.php/GPGPU#CUDA

Docker
------
Installing docker_ is straightforward, but I wanted to avoid adding my default
login into the ``docker`` group which is root equivalent. So I created a
special user to do this::

  # pacman -S docker
  # systemctl start docker
  # useradd --no-create-home -g docker docker
  # passwd
  $ su - docker

.. _docker: https://wiki.archlinux.org/index.php/Docker#Installation
