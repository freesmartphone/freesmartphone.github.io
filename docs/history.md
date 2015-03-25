# Project history

The roots of this project go back way beyond what is visible in the source code repository. The core concepts derived from solving needs that have appeared with the public availability of Linux-based mobile handhelds and smartphones in 2001.

## 2001 – 2006

Back in the early 2000s, when we built [OpenZaurus](http://www.openzaurus.org) and later [OpenEmbedded](http://www.openembedded.org), we tried to support as many devices as possible. Back then though, their Linux kernels exposed critical functionality (such as backlight, LEDs, suspend/resume/poweroff, and more), through a multitude of non-standardized interfaces. To cope with that, we built lots of device-specific daemons bearing little configurability and hardly any abstraction or interfaces to other processes.

In our sleepless nights though, we dreamed of an architecture that allowed certain daemons to communicate with properly specified "standard" APIs with their controlling processes. We hoped, we could get simple and easy interfaces to facilitate experimentation as well as research and education.

Alas, we were lacking the necessary prerequisites on many levels to create such a thing.

## 2007

When we started with the [Openmoko](http://www.openmoko.org) project, it took us a while to realize that although the Linux 2.6 kernels improved the situation somewhat (with the new class devices for e.g. LEDs and backlight control), not much had changed regarding the reusability of low level device managers. Platforms like Motorola's EZX were built on monolithic launcher processes that combined hardware control with application and business logic, hence creating an unmaintainable (closed source) mishmash.

Therefore we revisited the ideas and concepts from the early 2000s and these days, we finally had a proper interprocess communication tool to rely on. That tool was DBus, which although some years old, only then started to gain widespread adoption.

The freesmartphone.org project started to specify APIs for mobile systems with a particular focus on smartphones. In tandem, we created the first reference implementation [frameworkd](https://github.com/freesmartphone/framework) to evaluate our APIs.

## 2008

After a successful release of the first reference implementation in distributions such as OpenEZX and Openmoko, there was only one thing to desire – performance! frameworkd was written in [Python](http://www.python.org), a great language, but – especially on low power systems – coming with a bit too much overhead.

Therefore we wrote the 2nd reference implementation to conform with a refined set of DBus APIs. [Vala](http://www.vala-project.org), the language of choice for that was – again – a bit controversial, but turned out to work really well.

## 2009 – 2010

In 2009, Openmoko had to shut down its doors and one of the major driving forces behind freesmartphone.org and _the_ reference hardware platform lost more and more ground. We tried to bring FSO on other hardware platforms, such as HTC, Nokia N900, and Palm Pre, but due to the closed nature and the time-consuming reverse engineering process, we never got far enough that we could advertise any of those devices as fully working with our FSO middleware.

## 2011 – 2014

2011 brought even more problems for FSO: The wide spread distribution of low-cost (extremely closed source) Android handsets steered many contributors and potential users away from open alternatives, such as ours.

With HP killing WebOS and Nokia pulling all their resources out of open source (see also [this article](http://www.vanille.de/it-has-seen-a-crazy-year/), most of our potential target platforms went completely unsupported. Many people were frustrated and lost interest.

With my doughter Lara Marie being born in July, FSO temporarily lost its creator and main author – for something like over three years.

Not much happened apart from improved support for a bunch of new (half open, reverse engineered) devices during these years.

## 2015

In 2015, I came back. Having spend the last years mostly with iOS, I finally started revitalizing the freesmartphone.org initiative. (In a purely coincidental happening, the server on which we hosted freesmartphone.org shut down, thus I *had* to act).

I'm looking out for new potential hardware platforms, for funding, and for contributions. Until then, I'm working on improving the documentation, fixing bugs, lowering the barrier of entry (read: dependency hell), and checking what comes along.