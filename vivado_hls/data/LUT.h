#ifndef LUTs_h
#define LUTs_h
#include <stdint.h>

NUM_LINKS = 2
NUM_DEV_LINKS = 0

static const uint24_t coeff[NUM_LINKS][2] = {
{0xb7506a, 0x8910c0},
{0xad5074, 0x8110c0}
};

//static const uint24_t dcoeff[NUM_DEV_LINKS[3] = {};

//static const uint24_t coeff[2] = {0xb7506a, 0x8910c0, 0xad5074, 0x8110c0};

#endif
