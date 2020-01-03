Back to Arch Linux
##################

:author: Ashwin Vishnu Mohanan
:date: 2020-01-03T10:00:41.042526
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
- ppa_ / unofficial ``.deb`` packages from GitHub when the startup overhead of
  flatpak_ or appimage_ is way too high (Neovim, again 😅) or similar reasons
  as above (Nextcloud client, VSCodium etc.)

This is not good at all, I hear you. And I have to wait a good `4 more months`_
for the next LTS release! The final blow came when I saw Vim 8.2 was released
last month with popup_ support, and I do not have it yet! There is no practical
way (apart from yet another ppa_) to get the latest Vim, without compiling it
from source. Either ways, it is also unacceptable to run a desktop environment
(GNOME) which is lagging behind (version 3.28.2) the latest stable release
(version 3.34) for so long!

.. _pyenv: https://github.com/pyenv/pyenv/
.. _flatpak: https://flatpak.org/
.. _Ubuntu repos: https://packages.ubuntu.com/
.. _appimage: https://appimage.org/
.. _ppa: https://help.ubuntu.com/community/PPA
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

  ❯ gpg --keyserver-options auto-key-retrieve --verify archlinux-2020.01.01-x86_64.iso.sig
  gpg: assuming signed data in 'archlinux-2020.01.01-x86_64.iso'
  gpg: Signature made Wed 01 Jan 2020 06:21:41 AM CET
  gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
  gpg: Good signature from "Pierre Schmitz <pierre@archlinux.de>" [unknown]
  gpg: WARNING: This key is not certified with a trusted signature!
  gpg:          There is no indication that the signature belongs to the owner.
  Primary key fingerprint: 4AA4 767B BC9C 4B1D 18AE  28B7 7F2D 434B 9741 E8AC

The key fingerprint was cross-checked_ to be doubly sure.
I extracted the bootstrap image over there::

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

Did the same for the target Arch Linux installation::

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
