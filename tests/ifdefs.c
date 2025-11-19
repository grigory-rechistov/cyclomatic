#ifdef YABA
int foobar();
#endif

#if defined DOOBA
int barbaz();
#endif

void
set_rack_modes(fed_inst_t* parm)
{
    if (features)
    {
        static const isa2op_t isa2op[] = {
            {FED_ISA_SET_PPRO_UD3, FED_OPERAND_MODE},
            {FED_ISA_SET_GO, FED_OPERAND_P99},
#ifdef(FED_ISA_SET_ICACHE_PREFETCH_DEFINED)
            {FED_ISA_SET_ICACHE_PREFETCH, FED_OPERAND_PREFETCH_THAT},
#endif
#if defined(FED_ISA_SET_MOVRS_DEFINED)
            {FED_ISA_SET_MOVKIND, FED_OPERAND_PREFETCH_FOOBAR},
#endif
        };
    }
}
