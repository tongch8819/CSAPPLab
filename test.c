/***********************
 > FileName: test.c
 > Author: Tong Cheng
 > Email: tong.cheng.8819@qq.com 
 > Timestamp: Thu 28 Jan 2021 04:16:52 PM CST
**********************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
	int i;
	for (i = 0; i < len; i++) 
		printf(" %.2x", start[i]);
	printf("\n");
}

void show_int(int x) {
	show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x) {
	show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x) {
	show_bytes((byte_pointer) &x, sizeof(void *));
}

int main(int argc, char *argv[]){
	// int num = 200 * 300 * 400 * 500;
	// printf("200 * 300 * 400 * 500 equals: %d\n", num);

	// float f1, f2;
	// f1 = (3.14 + 1e20) - 1e20;
	// f2 = 3.14 + (1e20 - 1e20);
	// printf("f1: %f\n", f1);
	// printf("f2: %f\n", f2);

	// show_int(12345);
	// const char *m = "mnopqr";
	// show_bytes((byte_pointer) m, strlen(m));

	float a = 15213;
	show_bytes((byte_pointer) &a, sizeof(float));
	return 0;
}
