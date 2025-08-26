# somm24nm
SO/FSO  Simulating a uniprocessor scheduler, contiguous memory allocation system

******
******

## Prerequisites

On Ubuntu you need the following packages installed: 
_build-essential_, _cmake_, _doxygen_, and _git_.

```
sudo apt install build-essential cmake doxygen git
```
In other Linux distributions you need equivalent packages installed.

******

## Generating documentation

The code is documented in **doxygen**. So, you can easily generate **html** documentation pages.

```
cd «directory-of-your-choice»
cd somm22nm/doc
doxygen
```
Then, you can display the pages running (inside the **doc** directory)

```
firefox html/index.html &
```

Of course, you can replace _firefox_ with your favorite browser.

******

## Preparing the compilation environment

In a terminal, enter the base directory of your project, create the **build** directory,
and use _cmake_ to prepare _make_

```
cd «directory-of-your-choice»
cd «your-project»
mkdir build
cd build
cmake ../src
```

If you prefer _ninja_, instead of _make_,

```
cd «directory-of-your-choice»
cd «your-project»
mkdir build
cd build
cmake -G Ninja ../src
```

******

## Building the code

In a terminal, enter the **build** directory of your project and run _make_ or _ninja_

```
cd «directory-of-your-choice»
cd «your-project»«your-project»«your-project»/build
make
```
or

```
cd «directory-of-your-choice»
cd «your-project»/build
ninja
```

******

## Testing the code

After building the code, a program will be put in the <tt>«your-project»/bin</tt> directory. 
It is a default test program delivered with the base code.

You may edit it (<tt>main.cpp</tt>) to write your own tests.

Alternatively, you can write new test programs.
In this case, do not forget to add them to the main <tt>CMakeList.txt</tt> file.


