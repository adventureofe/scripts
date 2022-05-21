(defun c-gen () 
    (interactive)
     ;; get file name
    (setq project-name (read-string "enter project name: "))

    ;; make directories
    (make-directory project-name)
    (make-directory (concat project-name "/src"))
    (make-directory (concat project-name "/headers"))

    ;; generate readme
    (find-file (concat project-name "/readme.org"))
    (insert  "* " project-name "\n")
    (insert "By theadventureofe(John Gormley)\n")
    (insert "project description\n")
    (insert "the_adventure_of_e λ")
    (save-buffer)
    (kill-buffer)

    ;; generate main.c
    (find-file (concat project-name "/main.c"))

    (insert "/*\n    " project-name "\n")
    (insert "    By theadventureofe(John Gormley)\n")
    (insert "    project description\n")
    (insert "    the_adventure_of_e λ*/\n\n")

    (insert "#include <stdlib.h>\n")
    (insert "#include <stdio.h>\n\n")

    (insert "// print all included cmd args (removes compiler warning)\n")
    (insert "void arg_print(int argc, char** argv)\n")
    (insert "{\n")
    (insert "    for(int i = 1; i < argc; i++)\n")
    (insert "        printf(\"arg[%d]: %s\", i, argv[i]);\n")
    (insert "}\n\n")

    (insert "int main (int argc, char** argv)\n")
    (insert "{\n")
    (insert "    arg_print(argc, argv);\n")
    (insert "    printf(\"Hello, World!\\n\");\n")
    (insert "    return EXIT_SUCCESS;\n")
    (insert "}")
    
    (save-buffer)
    (kill-buffer)

    ;; generate makefile
    (find-file (concat project-name "/Makefile"))
    (insert "CC = clang\n")
    (insert "CFLAGS = -Wall -Wextra -pedantic\n")
    (insert "EXEC = " project-name "\n\n")

    (insert "output: main.o\n")
    (insert "\t$(CC) $(CFLAGS) main.o -o $(EXEC)\n\n")

    (insert "main.o: main.c\n")
    (insert "\t$(CC) -c $(CFLAGS) main.c\n\n")
    
    (insert "clean:\n")
    (insert "\trm *.o " project-name)
    (save-buffer)
    (kill-buffer)
)

(c-gen)
