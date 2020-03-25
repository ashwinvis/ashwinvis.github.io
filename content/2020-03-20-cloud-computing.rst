Cloud computing for research
############################

:author: Ashwin Vishnu Mohanan
:date: 2020-03-20T11:29:00
:modified: 2020-03-25T22:29:00
:slug: cloud-computing
:status: published
:summary: A journal of how I setup BOINC and Folding@home on my laptop running Arch Linux.
:category: Tech Talk
:tags: software, research, covid-19, hpc

There is an ongoing effort in all disciplines to find solutions the Covid-19
pandemic. Be it policy (social distancing, call for people to work from home),
technology (repurposing auto, beverages and perfume industries to manufacture
ventilators and hand sanitizers etc., open access to research) and art (hobbies
and music to stay upbeat at home).

And then there is BOINC and Folding@home - serious research projects which has
a nice social cloud-computing infrastructure to solve difficult problems. This
also include molecular dynamics simulations using open-source software like
GROMACS by different research groups around the world. My laptop has a
top-notch Quadro RTX 3000 Mobile GPU, so I decided to give it a go.

.. raw:: html

   <div align="center">
   <iframe src="https://pixelfed.social/p/ashwinvis/146561445096722432/embed?caption=true&likes=false&layout=full" class="pixelfed__embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe>
   </div>
   <script async defer src="https://pixelfed.social/embed.js"></script>

First off some essentials::

    # pacman -S opencl-nvidia cuda nvtop

BOINC
=====

References
~~~~~~~~~~

- https://wiki.archlinux.org/index.php/BOINC
- https://boinc.berkeley.edu/projects.php
- http://www.gpugrid.net/join.php
- https://www.gpugrid.net/team_display.php?teamid=2985

How to
~~~~~~

Installing and setting up::

    # pacman -S boinc-nox opencl-nvidia
    # usermod -a -G boinc video
    # systemctl start boinc-client.service
    # systemctl status boinc-client
    ● boinc-client.service - Berkeley Open Infrastructure Network Computing Client
         Loaded: loaded (/usr/lib/systemd/system/boinc-client.service; disabled; vendor preset: disabled)
         Active: active (running) since Fri 2020-03-20 08:06:50 CET; 1h 44min ago
           Docs: man:boinc(1)
       Main PID: 119973 (boinc)
          Tasks: 2 (limit: 38224)
         Memory: 9.6M
         CGroup: /system.slice/boinc-client.service
                 └─119973 /usr/bin/boinc

    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---]    (to change preferences, visit a project web site or select Preferences in the Manager)
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] Setting up project and slot directories
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] Checking active tasks
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] Setting up GUI RPC socket
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] Checking presence of 0 project files
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] This computer is not attached to any projects
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 Initialization completed
    Mar 20 08:07:37 archmage boinc[119973]: 20-Mar-2020 08:07:37 [---] Suspending GPU computation - computer is in use
    Mar 20 08:55:30 archmage boinc[119973]: 20-Mar-2020 08:55:30 [---] Resuming GPU computation
    Mar 20 09:14:26 archmage boinc[119973]: 20-Mar-2020 09:14:26 [---] Suspending GPU computation - computer is in use

This would generate a password at ``/var/lib/boinc/gui_rpc_auth.cfg``::

    # boinccmd --passwd $(cat /var/lib/boinc/gui_rpc_auth.cfg) --get_host_info
      timezone: 3600
      domain name: archmage
      IP addr: 127.0.1.1
      #CPUS: 12
      CPU vendor: GenuineIntel
      CPU model: Intel(R) Core(TM) i7-9850H CPU @ 2.60GHz [Family 6 Model 158 Stepping 13]
      CPU FP OPS: 1000000000.000000
      CPU int OPS: 1000000000.000000
      OS name: Linux Arch
      OS version: Arch Linux [5.5.9-arch1-2|libc 2.31 (GNU libc)]
      mem size: 33419243520.000000
      cache size: 12582912.000000
      swap size: 53687087104.000000
      disk size: 105152544768.000000
      disk free: 57508556800.000000
      NVIDIA GPU: Quadro RTX 3000 (driver version 440.64, CUDA version 10.2, compute capability 7.5, 4096MB, 3970MB available, 5299 GFLOPS peak)
        OpenCL: NVIDIA 0: Quadro RTX 3000 (driver version 440.64, device version OpenCL 1.2 CUDA, 5935MB, 3970MB available, 5299 GFLOPS peak)

Create an account in a project (substitute those variables starting with a $
sign)::

    # boinccmd --passwd $(cat /var/lib/boinc/gui_rpc_auth.cfg) \
        --create_account www.gpugrid.net $email $project_passwd $project_username

Find the "weak account key" by `logging in <https://www.gpugrid.net/login_form.php>`_. Then attach the account to the
project::

    # boinccmd --passwd $(cat /var/lib/boinc/gui_rpc_auth.cfg) --project_attach www.gpugrid.net $weak_account_key

The client should then run while the system is idle.

Folding @ home
==============

References
~~~~~~~~~~

- https://foldingathome.org/start-folding
- https://wiki.archlinux.org/index.php/Folding@home
- https://stats.foldingathome.org/team/45032

How to
~~~~~~

Install::

    # pacman -S foldingathome

`Register for an account (optional) <https://apps.foldingathome.org/getpasskey>`_

Run as a user::

    ❯ mkdir ~/{.config,.cache}/foldingathome
    ❯ cd ~/.config/foldingathome
    ❯ FAHClient --configure
    User name [Anonymous]: ****
    Team number [0]: 45032
    Passkey: ****
    Enable SMP [true]: false
    Enable GPU [true]:
    Name of configuration file [config.xml]:
    ❯ mkdir -p ~/.config/systemd/user/

Create a service ``~/.config/systemd/user/foldingathome.service``:

.. code:: ini

   [Unit]
   Description=Run folding at home client

   [Service]
   WorkingDirectory=/home/avmo/.cache/foldingathome
   ExecStart=/usr/bin/FAHClient --config /home/avmo/.config/foldingathome/config.xml

Execute::

    ❯ systemctl --user start foldingathome.service
    ❯ systemctl --user status foldingathome.service
    ● foldingathome.service - Run folding at home client
         Loaded: loaded (/home/avmo/.config/systemd/user/foldingathome.service; static; vendor preset: enabled)
         Active: active (running) since Fri 2020-03-20 09:38:15 CET; 4s ago
       Main PID: 149577 (FAHClient)
         CGroup: /user.slice/user-1001.slice/user@1001.service/foldingathome.service
                 └─149577 /usr/bin/FAHClient --config /home/avmo/.config/foldingathome/config.xml

    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:  <!-- Folding Slots -->
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:</config>
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:Trying to access database...
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:Successfully acquired database lock
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:Enabled folding slot 00: READY cpu:1
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:Enabled folding slot 01: PAUSED gpu:0:TU106GLM [Quadro RTX 3000 Mobile / Max-Q] (waiting for idle)
    Mar 20 09:38:15 archmage FAHClient[149577]: 08:38:15:WU00:FS00:Connecting to 65.254.110.245:8080
    Mar 20 09:38:16 archmage FAHClient[149577]: 08:38:16:WU00:FS00:Assigned to work server 128.252.203.9
    Mar 20 09:38:16 archmage FAHClient[149577]: 08:38:16:WU00:FS00:Requesting new work unit for slot 00: READY cpu:1 from 128.252.203.9

    # after a while ...
    ❯ systemctl --user status foldingathome.service
    ● foldingathome.service - Run folding at home client
         Loaded: loaded (/home/avmo/.config/systemd/user/foldingathome.service; static; vendor preset: enabled)
         Active: active (running) since Fri 2020-03-20 09:38:15 CET; 19min ago
       Main PID: 149577 (FAHClient)
         CGroup: /user.slice/user-1001.slice/user@1001.service/foldingathome.service
                 ├─149577 /usr/bin/FAHClient --config /home/avmo/.config/foldingathome/config.xml
                 ├─153643 /usr/bin/FAHCoreWrapper /home/avmo/.cache/foldingathome/cores/cores.foldingathome.org/v7/lin/64bit/avx/Core_a7.fah/FahCore_a7 -dir 00 -suffix 01 -ver>
                 └─153647 /home/avmo/.cache/foldingathome/cores/cores.foldingathome.org/v7/lin/64bit/avx/Core_a7.fah/FahCore_a7 -dir 00 -suffix 01 -version 705 -lifeline 15364>

    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:********************************************************************************
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Project: 14328 (Run 6, Clone 756, Gen 14)
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Unit: 0x000000109bf7a4d65e6d0ea7eac01f9c
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Reading tar file core.xml
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Reading tar file frame14.tpr
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Digital signatures verified
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Calling: mdrun -s frame14.tpr -o frame14.trr -cpt 15 -nt 1
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Steps: first=3500000 total=250000
    Mar 20 09:55:19 archmage FAHClient[149577]: 08:55:19:WU00:FS00:0xa7:Completed 1 out of 250000 steps (0%)
    Mar 20 09:57:25 archmage FAHClient[149577]: 08:57:25:WU00:FS00:0xa7:Completed 2500 out of 250000 steps (1%)

While the client is running / idle, you can schedule and tweak using the `web client <http://0.0.0.0:7396/>`_.

.. note::

   If you want GPU jobs alone, comment out the CPU slots in
   ``~/.config/foldingathome/config.xml`` and set power to "Medium" in the web
   client.
