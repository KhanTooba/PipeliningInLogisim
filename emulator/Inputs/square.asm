.main:
	mov r3, 0
	mov r0, 16
	div r1, r0, 2
	.loop:
		mul r2, r1, r1
		cmp r2, r0
		beq .end
		sub r1, r1, 1
		cmp r1, 0
		beq .finish
		b .loop
	.end:
		mov r3, 1
	.finish: