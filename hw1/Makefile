TARGET = 15 16 17 18 19 20
GPP = g++
CPPFLAGS = -O2 -std=c++11 -Wall

15=15.o
16=16.o
17=17.o
18=18.o
19=19.o
20=20.o
LIB=-lm -lbsm
.PHONY:clean

all: $(TARGET)


%.o: %.cpp
	@echo "making: " $@
	@$(GPP) $< -c $(CPPFLAG) 

clean:
	rm -rf *.o *.cpp~ *.graph *.graph~ Makefile~ *.h~
	@for bin in $(TARGET); do\
		echo "rm -rf $$bin"; \
		rm -rf $$bin; \
	done
