.main:
.encode mov r0, 6
.encode mov r1, 1
.encode mov r2, 1
	.loop:
.encode cmp r2, r0
.encode bgt .break
.encode mul r1, r1, r2
.encode add r2, r2, 1
.encode b .loop
	.break:
		.print r1
