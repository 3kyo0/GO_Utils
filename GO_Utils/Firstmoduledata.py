import Utils
import idautils
import struct

def findFirstModuleData(addr, bt):
    #addr_st = "".join(["%s "% x.encode('hex') for x in ("%x" % addr).decode('hex')[::-1]])
    #print addr_st
    possible_addr = idautils.XrefsTo(addr).next().frm
    if Utils.is_hardcoded_slice(possible_addr, bt):
        return possible_addr
    return None

def isGo17(addr, bt):
    addr += bt.size * 27
    return Utils.is_hardcoded_slice(addr, bt)

def getTypeinfo17(addr, bt):
    addr2 = addr + bt.size * 25
    robase = bt.ptr(addr2)
    addr += bt.size * 27
    beg = bt.ptr(addr)
    size = bt.ptr(addr+bt.size)
    return beg, beg+size*4, robase


def getTypeinfo(addr, bt):
    addr += bt.size * 25
    beg = bt.ptr(addr)
    size = bt.ptr(addr+bt.size)
    return beg, beg+size*bt.size

"""1.7
type moduledata struct {
3	pclntable    []byte
6	ftab         []functab
9	filetab      []uint32
10	findfunctab  uintptr
12	minpc, maxpc uintptr

14	text, etext           uintptr
16	noptrdata, enoptrdata uintptr
18	data, edata           uintptr
20	bss, ebss             uintptr
22	noptrbss, enoptrbss   uintptr
25	end, gcdata, gcbss    uintptr
27	types, etypes         uintptr

	typelinks []int32 // offsets from types
	itablinks []*itab

	modulename   string
	modulehashes []modulehash

	gcdatamask, gcbssmask bitvector

	typemap map[typeOff]*_type // offset to *_rtype in previous module

	next *moduledata
}
"""

"""1.6
type moduledata struct {
3	pclntable    []byte
6	ftab         []functab
9	filetab      []uint32
10	findfunctab  uintptr
12	minpc, maxpc uintptr

14	text, etext           uintptr
16	noptrdata, enoptrdata uintptr
18	data, edata           uintptr
20	bss, ebss             uintptr
22	noptrbss, enoptrbss   uintptr
25	end, gcdata, gcbss    uintptr

	typelinks []*_type

	modulename   string
	modulehashes []modulehash

	gcdatamask, gcbssmask bitvector

	next *moduledata
}
"""
"""1.5
type moduledata struct {
3	pclntable    []byte
6	ftab         []functab
9	filetab      []uint32
10	findfunctab  uintptr
12	minpc, maxpc uintptr

14	text, etext           uintptr
16	noptrdata, enoptrdata uintptr
18	data, edata           uintptr
20	bss, ebss             uintptr
22	noptrbss, enoptrbss   uintptr
25	end, gcdata, gcbss    uintptr

	typelinks []*_type

	modulename   string
	modulehashes []modulehash

	gcdatamask, gcbssmask bitvector

	next *moduledata
}
"""