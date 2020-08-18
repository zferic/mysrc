IDIR = ./include
CC=gcc
CFLAGS=-I$(IDIR)
_DEPS = test.h test2.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

main: main.o square.o
	$(CC) -o $@ $^ $(CFLAGS)
#define a rule for all files ending in the .o suffix here for main.o and square.o
%.o: %.c $(DEPS)
	$(CC) -c $< $(CFLAGS) -o $@

.PHONY: clean

clean:
	rm -f main *.o *~ 
