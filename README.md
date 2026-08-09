# P1S BMCU Lifeline

### A practical field guide to getting the BMCU 370C DM working reliably with the Bambu Lab P1S.

Firmware, PTFE routing, rewinding, troubleshooting, mods, and two and a half months of questionable life choices.

> **Yes, it works with the P1S.**
>
> **No, it isn't plug-and-play.**

![BMCU 370C DM Setup](https://i.imgur.com/rYUQM0S.jpeg)

---

## About This Project

**This is a living document.** I'll continue adding things as I test, break, fix, and remember them.

I'm a glutton for punishment, and by the time everything is said and done I'll probably have spent more on my BMCU setup than it would've cost to just buy a god damn AMS 2.

But I also fall into that weird Venn diagram where:

> **3D printing is my hobby, and 3D printers are my hobby.**

Sometimes the project is the point.

After a few months of tinkering, committing war crimes in Orca Slicer while redesigning parts, and generally questioning my life choices, I can confidently say:

# Yes. The BMCU 370C DM works with the P1S.

**Is it plug-and-play?**

Absolutely not.

**Will it test your patience?**

Frequently.

**Will you spend hours convinced the problem is mechanical, only to discover...**

The problem wasn't you.

It wasn't the printer.

It just decided that particular spool can go fuck itself.

I originally wrote this because I wanted something to live in the ether of the internet — hopefully something a search engine, another human, or some future AI model can find when somebody else is in the same predicament.

This repository is the permanent home for that information.

---

## Table of Contents

- [TL;DR](#tldr)
- [My Setup](#my-setup)
- [Firmware](#firmware)
- [PTFE Routing & Friction](#ptfe-routing--friction)
- [3 mm ID PTFE Tubing](#3-mm-id-ptfe-tubing)
- [Loading Behavior](#loading-behavior)
- [Seat the Output PTFE Tube](#seat-the-output-ptfe-tube)
- [Matte PLA](#matte-pla)
- [Space Pi X4L Auto Rewinder](#space-pi-x4l-auto-rewinder)
- [Side Mount & Tube Holder](#side-mount--tube-holder)
- [Space Pi X4L vs AMS 1 Risers](#space-pi-x4l-vs-ams-1-risers)
- [Things I Wish Someone Told Me](#things-i-wish-someone-told-me)
- [Troubleshooting](#troubleshooting)
- [Useful Links](#useful-links)
- [Updates](#updates)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

# TL;DR

If your BMCU is currently making you question your decision to buy it, start here.

## 1. Use the original Bambu 4-in-1 PTFE Adapter

![Original Bambu 4-in-1 PTFE Adapter](https://i.imgur.com/1ExvLVS.jpeg)

The newer clear adapter acted wonky for me.

About **90% of my issues cleared up** after switching to the old-style Bambu version.

It's about **$5** to avoid a massive fucking headache.

---

## 2. Reduce friction everywhere

The BMCU is **surprisingly sensitive to friction**, especially during loading and unloading.

Check:

- PTFE routing
- Tight bends
- PTFE fittings
- Tube supports
- The BMCU output tube
- The 4-in-1 adapter
- Your rewinder
- Your filament

The shortest PTFE path isn't necessarily the best.

> **The smoothest path usually wins.**

---

## 3. TRY ANOTHER GOD DAMN FILAMENT

I cannot stress this enough.

If you make one change and go from:

> **"Never loads"**

to:

> **"Loads half the time"**

don't immediately change a bunch of other shit.

Grab another spool.

You might already be **95% of the way there.**

---

## 4. Change ONE thing at a time

This setup has a lot of moving parts.

If you change your tube routing, reflash the BMCU, swap parts, and change filament all while chasing the same problem, you're just going to drive yourself insane.

> **Control your variables or the variables will control you.**

---

## 5. Once it works...

# STOP FUCKING WITH IT.

Seriously.

---

# My Setup

![My BMCU Setup](https://i.imgur.com/UxjbLiv.jpeg)

| Component | What I'm Using |
|---|---|
| Printer | **Bambu Lab P1S** |
| Multi-Filament System | **BMCU 370C DM** |
| P1S Firmware | **1.08** |
| BMCU Firmware | **ams_a_0.60f.bin** |
| Filament Dryer | **Creality Space Pi X4L** |
| PTFE Adapter | **Original Bambu 4-in-1 PTFE Adapter** |
| PTFE | **3 mm ID × 4 mm OD where practical** |
| Rewinder | **Space Pi X4/X4L Auto Rewinder Mod** |

---

# Firmware

## P1S Firmware

My P1S is currently downgraded to firmware:

```text
1.08
```

Do you actually need to downgrade?

**I honestly don't know.**

Somebody said to do it, I did it, it works, and I'm not touching it again.

> [!NOTE]
> Don't interpret this as proof that firmware 1.08 is required.
>
> This repository documents **what works on my setup**, not necessarily the only configuration that works.

---

## BMCU Firmware

After trying several different BMCU firmware versions, I landed on:

```text
ams_a_0.60f.bin
```

It gave me the most consistent loading and unloading behavior.

I'm **not** saying it's objectively the best firmware.

It's simply the one I stopped changing because it worked.

### Firmware Repository

[BMCU-C-PJARCZAK — High Force Load / P1S / AUTOLOAD / FILAMENT RGB ON / AMS_A](https://github.com/jarczakpawel/BMCU-C-PJARCZAK/tree/main/firmwares/high_force_load(P1S)/AUTOLOAD/FILAMENT_RGB_ON/AMS_A)

> [!TIP]
> If your BMCU is already working reliably, don't change firmware just because somebody on the internet — including me — is using a different version.

---

# PTFE Routing & Friction

If there's one thing I've learned from this project, it's that **PTFE routing matters way more than you'd expect.**

The BMCU is surprisingly sensitive to resistance while feeding and retracting filament.

A route that looks perfectly reasonable can cause intermittent failures.

## General Rules

- Avoid tight bends.
- Avoid unnecessary fittings.
- Support long PTFE runs.
- Make sure tubes are fully inserted into fittings.
- Watch for tubing being pulled sideways.
- Check for kinks and creases.
- Don't assume shorter is automatically better.
- Test using multiple filament spools.

The goal isn't necessarily:

> **Shortest PTFE path**

The goal is:

> **Lowest-friction PTFE path**

---

# 3 mm ID PTFE Tubing

Thanks to **u/meltman** for this one.

Using:

```text
3 mm ID × 4 mm OD
```

PTFE tubing instead of the more common:

```text
2.5 mm ID × 4 mm OD
```

noticeably reduced friction on my setup.

This was particularly helpful on the run between:

```text
BMCU → 4-in-1 Adapter
```

## The Tradeoff

The larger internal diameter means the walls are thinner.

That makes the tubing easier to:

- kink
- crease
- deform while cutting
- fuck up while routing

Order extra.

You'll probably ruin a piece or two.

Ask me how I know.

### Tubing I'm Using

[3 mm ID × 4 mm OD PTFE Tubing — Amazon](https://www.amazon.com/dp/B07B8CT1YH)

---

# Loading Behavior

Here's something I misunderstood for **way too long**:

## The filament does NOT load all the way to the 4-in-1 adapter when inserting a new spool.

I don't know if this is common knowledge or if I'm just an idiot, but I spent way too long thinking something was wrong.

On my setup, the filament feeds approximately:

```text
25–30 mm
~1 inch
```

past the BMCU fitting.

Then it stops and waits there until print time.

For the longest god damn time I thought something was wrong because it **"wasn't loading all the way."**

It wasn't broken.

That's just what it does.

> [!NOTE]
> This describes the behavior I've observed on **my configuration and firmware**. Other BMCU firmware versions may behave differently.

---

# Seat the Output PTFE Tube

This one caused way more trouble than it should have.

On the **output side of the BMCU**, the PTFE fitting going toward the printer is a push-to-connect fitting where the tube can seat **deeper than you initially think.**

![BMCU Output PTFE Fitting](https://i.imgur.com/36ZXX5M.jpeg)

Push the PTFE tube in until it's completely flush with the outlet.

It'll feel like it's already bottomed out.

**It probably isn't.**

It takes more force than you'd expect.

I was convinced I was going to break something.

## What I Did

This thing is cursed.

I shoved a piece of filament into the PTFE tube to keep it from collapsing.

Then I **lightly** grabbed the outside of the PTFE tube with a pair of side cutters a few millimeters above the fitting.

That gave me enough leverage to push the tube the rest of the way in.

> [!WARNING]
> I'm **not** saying this is the correct or officially recommended way to do it.
>
> I'm saying it's what finally got mine fully seated.
>
> Be careful not to cut, crush, or permanently deform the PTFE tube.

Getting the tube fully seated **substantially reduced my first-load failures.**

---

# Matte PLA

I don't know if this applies to every BMCU, but mine:

# HATES MATTE PLA.

It devours almost everything else but absolutely shits itself with matte.

All four channels behave the same way.

I love matte PLA because it hides layer lines so well, but with several brands I found myself having to help the filament through the feed path.

## Filament I've Tested

| Filament | Result |
|---|:---:|
| Elegoo Matte PLA | ❌ |
| SUNLU Matte PLA | ❌ |
| eSUN Matte PLA | ❌ |
| **Polymaker Matte PLA** | **✅** |

So far, **Polymaker Matte** is the only matte filament that has behaved consistently for me.

I'll update this as I try more.

> [!IMPORTANT]
> If you're troubleshooting feed failures, test with a completely different spool — preferably a different filament type — before changing hardware or firmware again.

---

# Space Pi X4L Auto Rewinder

![Space Pi X4L Auto Rewinder](https://i.imgur.com/qVBaaqd.jpeg)

I'm using the:

[Creality Space Pi X4 / X4L Auto Rewinder Mod — Printables](https://www.printables.com/model/1365518-creality-space-pi-x4-and-x4l-auto-rewinder-mod/files)

If possible, build the **metal spring version**.

It's currently located in the `Testing` folder.

You can buy the recommended tape measures on Amazon cheaply, and harvesting the springs is easy with a pair of side cutters.

The metal spring version has worked well for me.

---

# Side Mount & Tube Holder

## BMCU P1S Side Mount

I'm using:

[BMCU P1S Side Mount — MakerWorld](https://makerworld.com/en/models/2602983-bmcu-p1s-side-mount?from=search#profileId-2872297)

---

## PTFE Tube Holder

I'm also using:

[PTFE Tube Holder BMCU 370C — MakerWorld](https://makerworld.com/en/models/2400684-ptfe-tube-holder-bmcu-370c#profileId-2631287)

This helped reduce friction and feeding errors by keeping the PTFE routing under control.

---

# Space Pi X4L vs AMS 1 Risers

One happy accident I discovered is that the **Creality Space Pi X4L** is extremely close in footprint to the original **Bambu AMS 1**.

| Device | Dimensions |
|---|---:|
| Bambu AMS 1 | **368 × 283 × 224 mm** |
| Creality Space Pi X4L | **382 × 290 × 270 mm** |

That's only:

- **+14 mm wider**
- **+7 mm deeper**

The X4L is obviously taller, but for many risers the important dimensions are the footprint.

I measured mine, and the rubber feet on the Space Pi X4L sit **perfectly between the support rails** on the AMS riser I'm using.

It naturally centers itself without sliding around.

That means **many AMS 1 risers may work with the Space Pi X4L with little or no modification.**

> [!CAUTION]
> Check the dimensions before you commit to printing 15 hours of plastic.
>
> I can't guarantee every AMS riser on MakerWorld uses the same geometry.

## Riser I'm Using

[Low Profile AMS Riser with LED and Glass Lid Riser — MakerWorld](https://makerworld.com/en/models/182387-low-profile-ams-riser-with-led-and-glass-lid-riser#profileId-200898)

---

# Things I Wish Someone Told Me

## The BMCU is surprisingly sensitive to friction

Most of my loading and unloading problems ultimately came back to friction somewhere in the filament path.

---

## PTFE routing matters more than you think

A lot more.

---

## The shortest PTFE path isn't always the best

**The smoothest path usually wins.**

---

## A $5 adapter can make a bigger difference than a firmware flash

Hours of troubleshooting taught me that.

---

## Partial improvement is useful information

If something improves but doesn't completely fix the problem, you're probably moving in the right direction.

Keep iterating instead of immediately starting over.

---

## Bambu Studio may occasionally lose its mind

On older versions of Bambu Studio, I've occasionally had all of my filament seemingly disappear from the **Devices** tab.

Don't panic.

It comes back.

I haven't noticed this happening on newer versions.

---

## Filament itself can be the problem

Again:

# TRY ANOTHER GOD DAMN FILAMENT.

If one change gets you from **"never loads"** to **"loads half the time,"** don't immediately change another five things.

Grab another spool.

You might already have fixed the actual problem.

---

# Troubleshooting

If your BMCU isn't behaving, this is the order I'd troubleshoot it.

## Step 1 — Change Filament

Use a known-good spool.

Preferably **not matte PLA**.

If another filament suddenly works, stop tearing apart your hardware.

---

## Step 2 — Check the BMCU Output PTFE

Make sure the output PTFE tube is **fully seated** in the fitting.

Not:

> "That feels seated."

Actually seated.

---

## Step 3 — Check PTFE Routing

Look for:

- tight bends
- kinks
- creases
- unsupported sections
- side-loading at fittings
- unnecessary fittings
- excessive resistance

---

## Step 4 — Check the 4-in-1 Adapter

If you're using the newer clear adapter and experiencing intermittent problems, try the original Bambu 4-in-1 adapter.

This was one of the biggest improvements on my setup.

---

## Step 5 — Try Larger-ID PTFE

Consider:

```text
3 mm ID × 4 mm OD
```

particularly on the run:

```text
BMCU → 4-in-1 Adapter
```

---

## Step 6 — Check the Rewinder

Make sure the spool can unwind and rewind without creating excessive resistance.

A perfect BMCU filament path doesn't help much if the spool itself is fighting it.

---

## Step 7 — Firmware

Only after checking the mechanical filament path would I start experimenting with BMCU firmware.

Firmware is easy to blame.

Friction is easier to overlook.

---

## Step 8 — CHANGE ONE THING AT A TIME

Otherwise you won't know what fixed it.

> **Control your variables or the variables will control you.**

---

# Useful Links

| Resource | Link |
|---|---|
| BMCU Firmware | [BMCU-C-PJARCZAK](https://github.com/jarczakpawel/BMCU-C-PJARCZAK/tree/main/firmwares/high_force_load(P1S)/AUTOLOAD/FILAMENT_RGB_ON/AMS_A) |
| Space Pi X4/X4L Auto Rewinder | [Printables](https://www.printables.com/model/1365518-creality-space-pi-x4-and-x4l-auto-rewinder-mod/files) |
| BMCU P1S Side Mount | [MakerWorld](https://makerworld.com/en/models/2602983-bmcu-p1s-side-mount?from=search#profileId-2872297) |
| BMCU PTFE Tube Holder | [MakerWorld](https://makerworld.com/en/models/2400684-ptfe-tube-holder-bmcu-370c#profileId-2631287) |
| Low Profile AMS Riser | [MakerWorld](https://makerworld.com/en/models/182387-low-profile-ams-riser-with-led-and-glass-lid-riser#profileId-200898) |
| 3 mm ID × 4 mm OD PTFE | [Amazon](https://www.amazon.com/dp/B07B8CT1YH) |

---

# Updates

This is a living guide.

I'll continue adding information as I:

- test different filament
- experiment with PTFE routing
- find useful printed mods
- discover firmware differences
- break shit
- fix the shit I broke
- learn something that would've been extremely useful two months earlier

---

## July 5, 2026 — AMS Riser Compatibility

Discovered that the Space Pi X4L footprint is extremely close to the original AMS 1.

The rubber feet on my X4L fit perfectly between the rails of the AMS riser I'm using.

---

## July 5, 2026 — 3 mm ID PTFE

Thanks to **u/meltman** for suggesting larger-ID PTFE.

**3 mm ID × 4 mm OD PTFE** noticeably reduced friction, particularly between the BMCU and 4-in-1 adapter.

---

# Contributing

If you're running a **BMCU 370C DM on a Bambu Lab P1S** and you've figured out something I haven't, I'd love to hear about it.

## Open an Issue

If you've discovered a problem or solution, include as much of this information as possible:

- Printer model
- Printer firmware
- BMCU version
- BMCU firmware
- Filament brand/type
- PTFE configuration
- 4-in-1 adapter
- Rewinder setup
- Description of the problem
- What you've already tried
- What actually fixed it

The more information we collect, the easier it'll be to figure out which fixes are repeatable and which ones are just BMCU voodoo.

## Pull Requests

If you've:

- designed a useful modification
- discovered a repeatable fix
- tested another firmware configuration
- found better PTFE routing
- tested filament compatibility
- found something in this guide that's wrong

feel free to open a Pull Request.

The goal is for this repository to become **the resource I wish existed when I started this project.**

---

# Disclaimer

This is **not an official Bambu Lab, BMCU, Creality, MakerWorld, or Printables guide.**

I'm documenting:

- my hardware
- my firmware
- my testing
- my failures
- my questionable decisions
- what eventually worked

Something working on my machine doesn't guarantee it'll work on yours.

Be particularly careful when modifying hardware, flashing firmware, using tools around PTFE fittings, or following any of my more questionable troubleshooting techniques.

**Your hardware, firmware, filament, and tolerance for bullshit may vary.**

---

# If You Made It This Far...

Congratulations.

You have just witnessed the results of **two and a half months of troubleshooting.**

Go print your AMS Benchy.

Have a shot.

Then, for the love of God...

# Don't change anything that works.

If you've figured out something I haven't, open an Issue or PR.

I'd love for this repository to become the resource I wish existed when I started this project.

---

# One Last Thing...

## Once you have it working reliably...

# **STOP FUCKING WITH IT.**
