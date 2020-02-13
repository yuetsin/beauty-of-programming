	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movl	$0, -4(%rbp)
	movq	$0, -16(%rbp)
	movq	$0, -24(%rbp)
	callq	_clock
	movq	%rax, -16(%rbp)
	movb	_i(%rip), %cl
	andb	$-16, %cl
	orb	$1, %cl
	movb	%cl, _i(%rip)
LBB0_1:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB0_3 Depth 2
	movb	_i(%rip), %al
	andb	$15, %al
	movzbl	%al, %ecx
	cmpl	$9, %ecx
	jg	LBB0_10
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	movb	_i(%rip), %al
	andb	$15, %al
	orb	$16, %al
	movb	%al, _i(%rip)
LBB0_3:                                 ##   Parent Loop BB0_1 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movb	_i(%rip), %al
	shrb	$4, %al
	movzbl	%al, %ecx
	cmpl	$9, %ecx
	jg	LBB0_8
## %bb.4:                               ##   in Loop: Header=BB0_3 Depth=2
	movb	_i(%rip), %al
	andb	$15, %al
	movzbl	%al, %eax
	cltd
	movl	$3, %ecx
	idivl	%ecx
	movb	_i(%rip), %sil
	shrb	$4, %sil
	movzbl	%sil, %edi
	movl	%edi, %eax
	movl	%edx, -28(%rbp)         ## 4-byte Spill
	cltd
	idivl	%ecx
	movl	-28(%rbp), %ecx         ## 4-byte Reload
	cmpl	%edx, %ecx
	jne	LBB0_6
## %bb.5:                               ##   in Loop: Header=BB0_3 Depth=2
	movb	_i(%rip), %al
	andb	$15, %al
	movzbl	%al, %esi
	movb	_i(%rip), %al
	shrb	$4, %al
	movzbl	%al, %edx
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	%eax, -32(%rbp)         ## 4-byte Spill
LBB0_6:                                 ##   in Loop: Header=BB0_3 Depth=2
	jmp	LBB0_7
LBB0_7:                                 ##   in Loop: Header=BB0_3 Depth=2
	movb	_i(%rip), %al
	shrb	$4, %al
	addb	$1, %al
	movb	_i(%rip), %cl
	andb	$15, %al
	shlb	$4, %al
	andb	$15, %cl
	orb	%al, %cl
	movb	%cl, _i(%rip)
	jmp	LBB0_3
LBB0_8:                                 ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_9
LBB0_9:                                 ##   in Loop: Header=BB0_1 Depth=1
	movb	_i(%rip), %al
	andb	$15, %al
	addb	$1, %al
	movb	_i(%rip), %cl
	andb	$15, %al
	andb	$-16, %cl
	orb	%al, %cl
	movb	%cl, _i(%rip)
	jmp	LBB0_1
LBB0_10:
	callq	_clock
	movq	%rax, -24(%rbp)
	movq	-16(%rbp), %rdi
	movq	-24(%rbp), %rsi
	callq	__Z7secondsmm
	leaq	L_.str.1(%rip), %rdi
	movb	$1, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3               ## -- Begin function _Z7secondsmm
LCPI1_0:
	.quad	4696837146684686336     ## double 1.0E+6
	.section	__TEXT,__literal16,16byte_literals
	.p2align	4
LCPI1_1:
	.long	1127219200              ## 0x43300000
	.long	1160773632              ## 0x45300000
	.long	0                       ## 0x0
	.long	0                       ## 0x0
LCPI1_2:
	.quad	4841369599423283200     ## double 4503599627370496
	.quad	4985484787499139072     ## double 1.9342813113834067E+25
	.section	__TEXT,__text,regular,pure_instructions
	.globl	__Z7secondsmm
	.weak_definition	__Z7secondsmm
	.p2align	4, 0x90
__Z7secondsmm:                          ## @_Z7secondsmm
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movsd	LCPI1_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rsi
	movq	-8(%rbp), %rdi
	subq	%rdi, %rsi
	movq	%rsi, %xmm1
	movaps	LCPI1_1(%rip), %xmm2    ## xmm2 = [1127219200,1160773632,0,0]
	punpckldq	%xmm2, %xmm1    ## xmm1 = xmm1[0],xmm2[0],xmm1[1],xmm2[1]
	movapd	LCPI1_2(%rip), %xmm2    ## xmm2 = [4.503599627370496E+15,1.9342813113834067E+25]
	subpd	%xmm2, %xmm1
	haddpd	%xmm1, %xmm1
	divsd	%xmm0, %xmm1
	movaps	%xmm1, %xmm0
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
.zerofill __DATA,__bss,_i,1,0           ## @i
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"A = %d, B = %d\n"

L_.str.1:                               ## @.str.1
	.asciz	"solution #2 time elapsed: %f s\n"


.subsections_via_symbols
