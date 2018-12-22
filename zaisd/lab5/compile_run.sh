#!/bin/bash

clear; g++ main.cpp -o build/p.bin \
	&& echo "- - - - - - - - - - test encoding" \
	&& build/p.bin e sample.txt \
	&& echo "- - - - - - - - - - test decoding" \
	&& build/p.bin d build/coding_table.txt build/encoded.bin \
	&& echo "- - - - - - - - - - results of compression:" \
	&& echo "original: " && xxd sample.txt && echo "compressed" && xxd build/encoded.bin \
	&& echo "sizes: " && echo "original" && wc -c < sample.txt && echo "compressed" && wc -c < build/encoded.bin