# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build

# Include any dependencies generated for this target.
include group/jdt/CMakeFiles/jdt.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include group/jdt/CMakeFiles/jdt.dir/compiler_depend.make

# Include the progress variables for this target.
include group/jdt/CMakeFiles/jdt.dir/progress.make

# Include the compile flags for this target's objects.
include group/jdt/CMakeFiles/jdt.dir/flags.make

group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_init.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o -MF CMakeFiles/jdt.dir/jdt_init.cpp.o.d -o CMakeFiles/jdt.dir/jdt_init.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_init.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_init.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_init.cpp > CMakeFiles/jdt.dir/jdt_init.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_init.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_init.cpp -o CMakeFiles/jdt.dir/jdt_init.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_term.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o -MF CMakeFiles/jdt.dir/jdt_term.cpp.o.d -o CMakeFiles/jdt.dir/jdt_term.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_term.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_term.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_term.cpp > CMakeFiles/jdt.dir/jdt_term.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_term.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_term.cpp -o CMakeFiles/jdt.dir/jdt_term.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_print.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o -MF CMakeFiles/jdt.dir/jdt_print.cpp.o.d -o CMakeFiles/jdt.dir/jdt_print.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_print.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_print.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_print.cpp > CMakeFiles/jdt.dir/jdt_print.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_print.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_print.cpp -o CMakeFiles/jdt.dir/jdt_print.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_load.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o -MF CMakeFiles/jdt.dir/jdt_load.cpp.o.d -o CMakeFiles/jdt.dir/jdt_load.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_load.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_load.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_load.cpp > CMakeFiles/jdt.dir/jdt_load.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_load.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_load.cpp -o CMakeFiles/jdt.dir/jdt_load.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_random_fill.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o -MF CMakeFiles/jdt.dir/jdt_random_fill.cpp.o.d -o CMakeFiles/jdt.dir/jdt_random_fill.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_random_fill.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_random_fill.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_random_fill.cpp > CMakeFiles/jdt.dir/jdt_random_fill.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_random_fill.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_random_fill.cpp -o CMakeFiles/jdt.dir/jdt_random_fill.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_next_submission.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o -MF CMakeFiles/jdt.dir/jdt_next_submission.cpp.o.d -o CMakeFiles/jdt.dir/jdt_next_submission.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_next_submission.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_next_submission.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_next_submission.cpp > CMakeFiles/jdt.dir/jdt_next_submission.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_next_submission.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_next_submission.cpp -o CMakeFiles/jdt.dir/jdt_next_submission.cpp.s

group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o: group/jdt/CMakeFiles/jdt.dir/flags.make
group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_fetch_next.cpp
group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o: group/jdt/CMakeFiles/jdt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o -MF CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o.d -o CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o -c /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_fetch_next.cpp

group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jdt.dir/jdt_fetch_next.cpp.i"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_fetch_next.cpp > CMakeFiles/jdt.dir/jdt_fetch_next.cpp.i

group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jdt.dir/jdt_fetch_next.cpp.s"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt/jdt_fetch_next.cpp -o CMakeFiles/jdt.dir/jdt_fetch_next.cpp.s

# Object files for target jdt
jdt_OBJECTS = \
"CMakeFiles/jdt.dir/jdt_init.cpp.o" \
"CMakeFiles/jdt.dir/jdt_term.cpp.o" \
"CMakeFiles/jdt.dir/jdt_print.cpp.o" \
"CMakeFiles/jdt.dir/jdt_load.cpp.o" \
"CMakeFiles/jdt.dir/jdt_random_fill.cpp.o" \
"CMakeFiles/jdt.dir/jdt_next_submission.cpp.o" \
"CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o"

# External object files for target jdt
jdt_EXTERNAL_OBJECTS =

/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_init.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_term.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_print.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_load.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_random_fill.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_next_submission.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/jdt_fetch_next.cpp.o
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/build.make
/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a: group/jdt/CMakeFiles/jdt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Linking CXX static library /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a"
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && $(CMAKE_COMMAND) -P CMakeFiles/jdt.dir/cmake_clean_target.cmake
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/jdt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
group/jdt/CMakeFiles/jdt.dir/build: /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/lib/libjdt.a
.PHONY : group/jdt/CMakeFiles/jdt.dir/build

group/jdt/CMakeFiles/jdt.dir/clean:
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt && $(CMAKE_COMMAND) -P CMakeFiles/jdt.dir/cmake_clean.cmake
.PHONY : group/jdt/CMakeFiles/jdt.dir/clean

group/jdt/CMakeFiles/jdt.dir/depend:
	cd /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/src/group/jdt /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt /home/tiago/github/UA-LECI/3ano/1semestre/SO/P/Projeto/build/group/jdt/CMakeFiles/jdt.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : group/jdt/CMakeFiles/jdt.dir/depend

