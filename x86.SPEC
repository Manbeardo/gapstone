****************
Platform: X86 16bit (Intel syntax)
Code:0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 0x05 0x23 0x01 0x00 0x00 0x36 0x8b 0x84 0x91 0x23 0x01 0x00 0x00 0x41 0x8d 0x84 0x39 0x89 0x67 0x00 0x00 0x8d 0x87 0x89 0x67 0x00 0x00 0xb4 0xc6 
Disasm:
0x1000:	lea	cx, dword ptr [si + 0x32]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 1, imm_size: 2
	modrm: 0x4c
	disp: 0x32
	op_count: 2
		operands[0].type: REG = cx
		operands[1].type: MEM
			operands[1].mem.base: REG = si
			operands[1].mem.disp: 0x32

0x1003:	or	byte ptr [bx + di], al
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x08 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x1
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
			operands[0].mem.index: REG = di
		operands[1].type: REG = al

0x1005:	fadd	dword ptr [bx + di + 0x34c6]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0xd8 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x81
	disp: 0x34c6
	op_count: 1
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
			operands[0].mem.index: REG = di
			operands[0].mem.disp: 0x34c6

0x1009:	adc	al, byte ptr [bx + si]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x12 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x0
	disp: 0x0
	op_count: 2
		operands[0].type: REG = al
		operands[1].type: MEM
			operands[1].mem.base: REG = bx
			operands[1].mem.index: REG = si

0x100b:	add	byte ptr [di], al
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x00 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x5
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = di
		operands[1].type: REG = al

0x100d:	and	ax, word ptr [bx + di]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x23 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x1
	disp: 0x0
	op_count: 2
		operands[0].type: REG = ax
		operands[1].type: MEM
			operands[1].mem.base: REG = bx
			operands[1].mem.index: REG = di

0x100f:	add	byte ptr [bx + si], al
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x00 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x0
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
			operands[0].mem.index: REG = si
		operands[1].type: REG = al

0x1011:	mov	ax, word ptr ss:[si + 0x2391]
	Prefix:0x01 0x00 0x00 0x00 0x00 
	Segment override: ss
	Opcode:0x8b 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x84
	disp: 0x2391
	op_count: 2
		operands[0].type: REG = ax
		operands[1].type: MEM
			operands[1].mem.base: REG = si
			operands[1].mem.disp: 0x2391

0x1016:	add	word ptr [bx + si], ax
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x01 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x0
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
			operands[0].mem.index: REG = si
		operands[1].type: REG = ax

0x1018:	add	byte ptr [bx + di + 0xff8d], al
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x00 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 1, imm_size: 2
	modrm: 0x41
	disp: 0xffffff8d
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
			operands[0].mem.index: REG = di
			operands[0].mem.disp: 0xffffffffffffff8d
		operands[1].type: REG = al

0x101b:	test	bh, byte ptr [bx + di]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x84 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x39
	disp: 0x0
	op_count: 2
		operands[0].type: REG = bh
		operands[1].type: MEM
			operands[1].mem.base: REG = bx
			operands[1].mem.index: REG = di

0x101d:	mov	word ptr [bx], sp
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x89 0x00 0x00 
	op_size: 2, addr_size: 2, disp_size: 1, imm_size: 2
	modrm: 0x67
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = bx
		operands[1].type: REG = sp

0x1020:	add	byte ptr [di + 0x8987], cl
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x00 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 2
	modrm: 0x8d
	disp: 0xffff8987
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = di
			operands[0].mem.disp: 0xffffffffffff8987
		operands[1].type: REG = cl

0x1024:	add	byte ptr [eax], al
	Prefix:0x01 0x00 0x00 0x00 0x00 
	Opcode:0x00 0x00 0x00 
	op_size: 1, addr_size: 4, disp_size: 4, imm_size: 2
	modrm: 0x0
	disp: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = eax
		operands[1].type: REG = al

0x1027:	mov	ah, -0x3a
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0xb4 0x00 0x00 
	op_size: 1, addr_size: 2, disp_size: 2, imm_size: 1
	modrm: 0x0
	disp: 0x0
	imm_count: 1
		imms[1]: 0xffffffffffffffc6
	op_count: 2
		operands[0].type: REG = ah
		operands[1].type: IMM = 0xffffffffffffffc6

0x1029:

****************
Platform: X86 32 (AT&T syntax)
Code:0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 0x05 0x23 0x01 0x00 0x00 0x36 0x8b 0x84 0x91 0x23 0x01 0x00 0x00 0x41 0x8d 0x84 0x39 0x89 0x67 0x00 0x00 0x8d 0x87 0x89 0x67 0x00 0x00 0xb4 0xc6 
Disasm:
0x1000:	leal	dword ptr 8(%edx, %esi), %ecx
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 1, imm_size: 4
	modrm: 0x4c
	disp: 0x8
	sib: 0x32
	sib_index: esi, sib_scale: 1, sib_base: edx
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = edx
			operands[0].mem.index: REG = esi
			operands[0].mem.disp: 0x8
		operands[1].type: REG = ecx

0x1004:	addl	%ebx, %eax
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x01 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0xd8
	disp: 0x0
	sib: 0x0
	op_count: 2
		operands[0].type: REG = ebx
		operands[1].type: REG = eax

0x1006:	addl	$0x1234, %esi
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x81 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0xc6
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0x1234
	op_count: 2
		operands[0].type: IMM = 0x1234
		operands[1].type: REG = esi

0x100c:	addl	$0x123, %eax
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x05 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0x123
	op_count: 2
		operands[0].type: IMM = 0x123
		operands[1].type: REG = eax

0x1011:	movl	dword ptr %ss:0x123(%ecx, %edx, 4), %eax
	Prefix:0x01 0x00 0x00 0x00 0x00 
	Segment override: ss
	Opcode:0x8b 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x84
	disp: 0x123
	sib: 0x91
	sib_index: edx, sib_scale: 4, sib_base: ecx
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = ecx
			operands[0].mem.index: REG = edx
			operands[0].mem.scale: 4
			operands[0].mem.disp: 0x123
		operands[1].type: REG = eax

0x1019:	incl	%ecx
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x41 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	op_count: 1
		operands[0].type: REG = ecx

0x101a:	leal	dword ptr 0x6789(%ecx, %edi), %eax
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x84
	disp: 0x6789
	sib: 0x39
	sib_index: edi, sib_scale: 1, sib_base: ecx
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = ecx
			operands[0].mem.index: REG = edi
			operands[0].mem.disp: 0x6789
		operands[1].type: REG = eax

0x1021:	leal	dword ptr 0x6789(%edi), %eax
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x87
	disp: 0x6789
	sib: 0x0
	op_count: 2
		operands[0].type: MEM
			operands[0].mem.base: REG = edi
			operands[0].mem.disp: 0x6789
		operands[1].type: REG = eax

0x1027:	movb	$-0x3a, %ah
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0xb4 0x00 0x00 
	op_size: 1, addr_size: 4, disp_size: 4, imm_size: 1
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0xffffffffffffffc6
	op_count: 2
		operands[0].type: IMM = 0xffffffffffffffc6
		operands[1].type: REG = ah

0x1029:

****************
Platform: X86 32 (Intel syntax)
Code:0x8d 0x4c 0x32 0x08 0x01 0xd8 0x81 0xc6 0x34 0x12 0x00 0x00 0x05 0x23 0x01 0x00 0x00 0x36 0x8b 0x84 0x91 0x23 0x01 0x00 0x00 0x41 0x8d 0x84 0x39 0x89 0x67 0x00 0x00 0x8d 0x87 0x89 0x67 0x00 0x00 0xb4 0xc6 
Disasm:
0x1000:	lea	ecx, dword ptr [edx + esi + 8]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 1, imm_size: 4
	modrm: 0x4c
	disp: 0x8
	sib: 0x32
	sib_index: esi, sib_scale: 1, sib_base: edx
	op_count: 2
		operands[0].type: REG = ecx
		operands[1].type: MEM
			operands[1].mem.base: REG = edx
			operands[1].mem.index: REG = esi
			operands[1].mem.disp: 0x8

0x1004:	add	eax, ebx
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x01 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0xd8
	disp: 0x0
	sib: 0x0
	op_count: 2
		operands[0].type: REG = eax
		operands[1].type: REG = ebx

0x1006:	add	esi, 0x1234
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x81 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0xc6
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0x1234
	op_count: 2
		operands[0].type: REG = esi
		operands[1].type: IMM = 0x1234

0x100c:	add	eax, 0x123
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x05 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0x123
	op_count: 2
		operands[0].type: REG = eax
		operands[1].type: IMM = 0x123

0x1011:	mov	eax, dword ptr ss:[ecx + edx*4 + 0x123]
	Prefix:0x01 0x00 0x00 0x00 0x00 
	Segment override: ss
	Opcode:0x8b 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x84
	disp: 0x123
	sib: 0x91
	sib_index: edx, sib_scale: 4, sib_base: ecx
	op_count: 2
		operands[0].type: REG = eax
		operands[1].type: MEM
			operands[1].mem.base: REG = ecx
			operands[1].mem.index: REG = edx
			operands[1].mem.scale: 4
			operands[1].mem.disp: 0x123

0x1019:	inc	ecx
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x41 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	op_count: 1
		operands[0].type: REG = ecx

0x101a:	lea	eax, dword ptr [ecx + edi + 0x6789]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x84
	disp: 0x6789
	sib: 0x39
	sib_index: edi, sib_scale: 1, sib_base: ecx
	op_count: 2
		operands[0].type: REG = eax
		operands[1].type: MEM
			operands[1].mem.base: REG = ecx
			operands[1].mem.index: REG = edi
			operands[1].mem.disp: 0x6789

0x1021:	lea	eax, dword ptr [edi + 0x6789]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8d 0x00 0x00 
	op_size: 4, addr_size: 4, disp_size: 4, imm_size: 4
	modrm: 0x87
	disp: 0x6789
	sib: 0x0
	op_count: 2
		operands[0].type: REG = eax
		operands[1].type: MEM
			operands[1].mem.base: REG = edi
			operands[1].mem.disp: 0x6789

0x1027:	mov	ah, -0x3a
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0xb4 0x00 0x00 
	op_size: 1, addr_size: 4, disp_size: 4, imm_size: 1
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	imm_count: 1
		imms[1]: 0xffffffffffffffc6
	op_count: 2
		operands[0].type: REG = ah
		operands[1].type: IMM = 0xffffffffffffffc6

0x1029:

****************
Platform: X86 64 (Intel syntax)
Code:0x55 0x48 0x8b 0x05 0xb8 0x13 0x00 0x00 
Disasm:
0x1000:	push	rbp
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x55 0x00 0x00 
	op_size: 8, addr_size: 8, disp_size: 4, imm_size: 4
	modrm: 0x0
	disp: 0x0
	sib: 0x0
	op_count: 1
		operands[0].type: REG = rbp

0x1001:	mov	rax, qword ptr [rip + 0x13b8]
	Prefix:0x00 0x00 0x00 0x00 0x00 
	Opcode:0x8b 0x00 0x00 
	op_size: 8, addr_size: 8, disp_size: 4, imm_size: 4
	modrm: 0x5
	disp: 0x13b8
	sib: 0x0
	op_count: 2
		operands[0].type: REG = rax
		operands[1].type: MEM
			operands[1].mem.base: REG = rip
			operands[1].mem.disp: 0x13b8

0x1008:

