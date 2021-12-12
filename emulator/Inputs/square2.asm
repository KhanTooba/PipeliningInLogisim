.main:
.encode mov r3, 0
.encode mov r0, 16
.encode div r1, r0, 2
	.loop:
.encode mul r2, r1, r1
.encode cmp r2, r0
.encode beq .end
.encode sub r1, r1, 1
.encode cmp r1, 0
.encode beq .finish
.encode b .loop
	.end:
.encode mov r3, 1
	.finish: