# Generate C++ project

# By theadventureofe(John Gormley)

# A python script that generates a C++ project with all the bells and whistles

# the_adventure_of_e λ

import os

project_name = input("Enter C++ project name:")

# Create directories
os.mkdir(project_name)
os.mkdir(project_name + "/src")
os.mkdir(project_name + "/headers")

# Create readme.org for github
f = open(project_name + "/readme.org", "a")
f.write( "/*\n" + project_name + "\n" + 
"By theadventureofe(John Gormley)\n" +
"*project description*\n" +
"the_adventure_of_e λ\n*/\n")
f.close()

# Create main.cpp with hello, world! program
f = open(project_name + "/main.cpp", "a")
f.write(
"/* " + project_name + "\n\n" + 
"By theadventureofe(John Gormley)\n\n" +
"*project description*\n\n" +
"the_adventure_of_e λ\n*/\n\n" +
         
"#include <iostream>\n\n" +
         
"int main (int argc, char** argv){\n\n" +

"  for(int i = 1; i < argc; i++){\n\n" +
"    std::cout << \"arg[\" << i << \"]: \" << argv[i] << \"\\n\";\n" +
"  }\n\n" +

"  std::cout << \"Hello, World!\\n\";\n" +
"  return 0;\n" +
"}\n")
f.close();

# Create a makefile
f = open(project_name + "/Makefile", "a")
f.write("output: main.o\n" +
        "\tclang++ main.o -o " + project_name + " -W -Wall -Wextra -pedantic\n\n" +

        "main.o: main.cpp\n" +
        "\tclang++ -c main.cpp -W -Wall -Wextra -pedantic\n\n" +

        "clean:\n" +
        "\trm *.o " + project_name)
f.close();
