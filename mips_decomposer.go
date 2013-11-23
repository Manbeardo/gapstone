package gapstone

// #cgo CFLAGS: -I/usr/include/capstone
// #cgo LDFLAGS: -lcapstone
// #include <stdlib.h>
// #include <capstone.h>
import "C"
import "unsafe"
import "reflect"

//import "fmt"

type MipsInstruction struct {
	Operands []MipsOperand
}

func (insn MipsInstruction) OpCount(optype uint) int {
	count := 0
	for _, op := range insn.Operands {
		if op.Type == optype {
			count++
		}
	}
	return count
}

type MipsOperand struct {
	Type uint
	Reg  uint // Only ONE of these four will be set
	Imm  int64
	Mem  MipsMemoryOperand
}

type MipsMemoryOperand struct {
	Base uint
	Disp int64
}

func fillMipsHeader(raw C.cs_insn, insn *Instruction) {
	mips := new(MipsInstruction)
	cs_mips := (*C.cs_mips)(unsafe.Pointer(&raw.anon0[0]))

	// Cast the op_info to a []C.cs_mips_op
	var ops []C.cs_mips_op
	oih := (*reflect.SliceHeader)(unsafe.Pointer(&ops))
	oih.Data = uintptr(unsafe.Pointer(&cs_mips.operands[0]))
	oih.Len = int(cs_mips.op_count)
	oih.Cap = int(cs_mips.op_count)

	// Create the Go object for each operand
	for _, cop := range ops {

		if cop._type == MIPS_OP_INVALID {
			break
		}

		gop := new(MipsOperand)
		gop.Type = uint(cop._type)

		switch cop._type {
		// fake a union by setting only the correct struct member
		case MIPS_OP_IMM:
			gop.Imm = int64(*(*C.int64_t)(unsafe.Pointer(&cop.anon0[0])))
		case MIPS_OP_REG:
			gop.Reg = uint(*(*C.uint)(unsafe.Pointer(&cop.anon0[0])))
		case MIPS_OP_MEM:
			gmop := new(MipsMemoryOperand)
			cmop := (*C.mips_op_mem)(unsafe.Pointer(&cop.anon0[0]))
			gmop.Base = uint(cmop.base)
			gmop.Disp = int64(cmop.disp)
			gop.Mem = *gmop
		}

		mips.Operands = append(mips.Operands, *gop)

	}
	insn.Mips = *mips
}

func DecomposeMips(raws []C.cs_insn) []Instruction {
	decomposed := []Instruction{}
	for _, raw := range raws {
		decomp := new(Instruction)
		fillGenericHeader(raw, decomp)
		fillMipsHeader(raw, decomp)
		decomposed = append(decomposed, *decomp)
	}
	return decomposed
}