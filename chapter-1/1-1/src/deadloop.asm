_main:
100000f90:	55 	pushq	%rbp
100000f91:	48 89 e5 	movq	%rsp, %rbp
100000f94:	c7 45 fc 00 00 00 00 	movl	$0, -4(%rbp)
100000f9b:	c7 45 f8 00 00 00 00 	movl	$0, -8(%rbp)
100000fa2:	8b 45 f8 	movl	-8(%rbp), %eax
100000fa5:	83 c0 01 	addl	$1, %eax
100000fa8:	89 45 f8 	movl	%eax, -8(%rbp)
100000fab:	e9 f2 ff ff ff 	jmp	-14 <_main+0x12>