inline __int64 GetCPUTickCount() {
    __asm
    {
        rdtsc;
    }
}