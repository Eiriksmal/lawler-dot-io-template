Title: Linux Cookbooks
Date: 2019-12-24 17:51
Category: Linux
Tags: reference, how-to
Description: Random Linux learnings I've accrued over the years.
Status: Published

<section markdown="1">
I am *forever* losing random blog posts that explain the mysterious inner workings of Advanced Linux Components: udev, kmod, UEFI kernel mod signing, etc.

Rather than continue to accrue bookmarks that rot over time, I'm going to start writing down what I've learned, so I can reference it on a domain that won't disappear in 3 years...

## Installing nVidia drivers + Optimus in Fedora UEFI secure boot
Optimus is nVidia's tech for switching loads from the lame-o built-in Intel GPU<label for="sn-igpu" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-igpu" class="margin-toggle"><span class="sidenote">iGPU, for *integrated*</span> to the beefy, discrete nVidia GPU<label for="sn-egpu" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-egpu" class="margin-toggle"><span class="sidenote">eGPU, for, uh, not-the-intel-one</span> in your workstation-y, game-y laptops. They have A New Thing now they call [PRIME Render Offload](https://download.nvidia.com/XFree86/Linux-x86_64/440.44/README/primerenderoffload.html) that does High-Level Magic to render things on the beefy eGPU then feed it to the iGPU for display in the same X session.

nVidia added Linux support for PRIME in early 2019 or so, judging from the dates on internet comment threads. Fedora 31 supports all the patches to the X11 upstream natively--one of many reasons that Fedora and Arch are the only Linux distributions worth installing. And, surprisingly, [RPM Fusion](https://rpmfusion.org/Howto/Optimus) has a functioning kmod package for the nVidia drivers that's new enough to support PRIME. Convenient!

### Recipe

1. `dnf install akmod-nvidia`
2. `pgrep kmod`--wait for the module to finish compiling before doing anything else, sheesh.
3. You already added your 509 DER sign-y keys<label for="sn-der" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-der" class="margin-toggle"><span class="sidenote">Wait, you *do* have 509 DER sign-y keys, right? No? Then, sheesh, do this: openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=Eric Lawler Gave Me This Script and I Ran It Without Changing Any Values/"</span> to the UEFI MOK, right? If not:
    1. `mokutil --import your-public-key.der`
    2. Give mokutil a nice password
    3. Reboot your machine
    4. Tell the lovely BIOS blue screen you want to add a new key. You should choose `View key #0` to ensure that's the one you added. Is it good through 2119? It probably should be. You don't want your extra kernel modules to stop working next century, right?
    5. ADD THE KEY. You'll have to enter your password from step ii (pronounced [aiai](https://duckduckgo.com/?q=super+monkey+ball+aiai&t=ffab&iar=images&iax=images&ia=images)).
    6. And that's it. When you boot, you can sign things with that MOK key.
4. Sign all the nVidia kernel modules with your DER key. You'll have to do this every time you update the nVidia drivers or install a new kernel. Same as VirtualBox. I have a simple sh script:
```bash
KERNEL=$(uname -r)

echo 'Signing kernel modules for nvidia...'
for i in /usr/lib/modules/$KERNEL/extra/nvidia/*ko; do
  echo "...signing $i"
  sudo /usr/src/kernels/$KERNEL/scripts/sign-file sha256 my-private-key.priv my-public-key.der "$i";
done
echo 'Starting kernel modules'
sudo modprobe -v nvidia
```
...except that, of course, the kernel modules can't start while nouveau is loaded. So reboot one more time after the first install to be running with nVidia's drivers.

### How to use it?
To use your laptop's beefy nVidia GPU, append this environment string to whatever you're running:
`__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia [program]`

Steam launchers can be modified like so:
`__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia %command%`

## Signing VirtualBox drivers
1. Add a new MOK as in the nVidia instructions above.
2. Find your driver:
     - `updatedb && locate vboxdrv` ...or
     - `modinfo -n vboxdrv`
3. Sign it. (This is the path from the RPM Fusion repo.) 
```bash
KERNEL=$(uname -r)

echo 'Signing kernel modules for VirtualBox...'
for i in /lib/modules/$KERNEL/extra/VirtualBox/*ko; do
  echo "...signing $i"
  sudo /usr/src/kernels/$KERNEL/scripts/sign-file sha256 my-private-key.priv my-public-key.der "$i";
done
echo 'Starting kernel modules'
sudo modprobe -v vboxdrv
```

## Remapping caps lock to backspace, 2019 edition
This one's a real mess, but I'm too lazy to type it out now. I'm trusting that this dangling appendage will <del>embarrass</del> shame me into completing it, since the new Ask Fedora is absolutely, 100% useless and all the old Ask Fedora content (now rebranded as Askbot.fedora.org) will vanish soon, including [Ahmad Samir's ridiculously useful answer](https://web.archive.org/web/20190517092849/https://askbot.fedoraproject.org/en/question/37598/how-to-create-custom-keymaps-now-that-libudevkeymap-is-gone/) to my udev question from 2013.

tldr? Dig into the udev Readmes hiding on your system to learn all the udev utilities to run and monitor output while poking keys on your keyboard. Then you'll suss out the manufacturer specific serial numbers/device IDs you can use to run rules or straight-up remap the hardware, as I do. 

Here is my cookbook, for the next computer I purchase. Plop this in `/lib/udev/hwdb.d/90-custom-keyboard.hwdb`, in Linux kernel 5.X+ and this will cause the kernel to translate all slaps of the caps lock key, useless invention that it is, as a backspace key to every single application on your system: In X and Wayland and Virtual Terminals alike.

```bash
# Dell XPS 15
evdev:input:b0011v0001p0001eAB41*
 KEYBOARD_KEY_3a=backspace
 KEYBOARD_KEY_70039=backspace

# generic Logitech
evdev:input:b0003v046DpC31*
 KEYBOARD_KEY_3a=backspace
 KEYBOARD_KEY_70039=backspace

# Microsoft Sculpt Ergo Keyboard
evdev:input:b0003v045Ep07A5*
 KEYBOARD_KEY_3a=backspace
 KEYBOARD_KEY_70039=backspace

# Microsoft Natural Ergonomic Keyboard 4000
evdev:input:b0003v045Ep00DB*
 KEYBOARD_KEY_3a=backspace
 KEYBOARD_KEY_70039=backspace
 KEYBOARD_KEY_c022d=up
 KEYBOARD_KEY_c022e=down

# das keyboard
evdev:input:b0003v24F0*
 KEYBOARD_KEY_3a=backspace
 KEYBOARD_KEY_70039=backspace
```

Merry Christmas.
</section>
