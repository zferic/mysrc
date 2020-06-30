IDIR = ./include
CC=gcc
CFLAGS=-I$(IDIR)
_DEPS = test.h test2.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

main: main.o square.o
	$(CC) -o $@ $^ $(CFLAGS)
%.o: %.c $(DEPS)
	$(CC) -c $< $(CFLAGS) -o $@

