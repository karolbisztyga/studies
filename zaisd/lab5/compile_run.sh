#!/bin/bash

clear; g++ main.cpp -o build/p.bin \
	&& echo "- - - - - - - - - - test encoding" \
	&& build/p.bin e sample.txt \
	&& echo "- - - - - - - - - - test decoding" 
	#&& build/p.bin d build/coding_table.txt build/encoded.bin
