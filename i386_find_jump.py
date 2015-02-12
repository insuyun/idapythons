push_esp_ret = FindBinary(MinEA(), SEARCH_DOWN|SEARCH_CASE, "\x54\xc3")
if push_esp_ret != 0xffffffff:
	print "push esp; ret : 0x%x" % push_esp_ret
jmp_esp = FindBinary(MinEA(), SEARCH_DOWN|SEARCH_CASE, "\xff\xe4")
if jmp_esp != 0xffffffff:
	print "jmp_esp : 0x%x" % jmp_esp 
call_esp = FindBinary(MinEA(), SEARCH_DOWN|SEARCH_CASE, "\xff\xd4")
if call_esp != 0xffffffff:
	print "call esp : 0x%x" % call_esp 
