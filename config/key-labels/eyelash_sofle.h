/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 *
 * eyelash_sofle layout - 6 columns per side, 5 rows (4 main + thumbs)
 * Positions 6, 19, 32, 45 are rotary encoder clicks (skipped in numbering).
 * (TP) = trackpoint (right); 59-63 are its directional inputs (up/dn/l/r/click)
 *
 * ╭──────────────────────────────────────────────────────────╮
 * │  0   1   2   3   4   5  │ (TP) │  7   8   9  10  11  12  │
 * │ 13  14  15  16  17  18  │      │ 20  21  22  23  24  25  │
 * │ 26  27  28  29  30  31  │      │ 33  34  35  36  37  38  │
 * │ 39  40  41  42  43  44  │      │ 46  47  48  49  50  51  │
 * │     53  54  55  56  57  │      │ 59  60  61  62  63      │
 * ╰──────────────────────────────────────────────────────────╯
 */

#pragma once

/* Row 0 - Top */
#define LT6  0
#define LT5  1
#define LT4  2
#define LT3  3
#define LT2  4
#define LT1  5
/* 6 = left encoder */
#define RT1  7
#define RT2  8
#define RT3  9
#define RT4 10
#define RT5 11
#define RT6 12

/* Row 1 - Upper Middle */
#define LM6 13
#define LM5 14
#define LM4 15
#define LM3 16
#define LM2 17
#define LM1 18
/* 19 = left encoder */
#define RM1 20
#define RM2 21
#define RM3 22
#define RM4 23
#define RM5 24
#define RM6 25

/* Row 2 - Lower Middle */
#define LH6 26
#define LH5 27
#define LH4 28
#define LH3 29
#define LH2 30
#define LH1 31
/* 32 = left encoder */
#define RH1 33
#define RH2 34
#define RH3 35
#define RH4 36
#define RH5 37
#define RH6 38

/* Row 3 - Bottom */
#define LB6 39
#define LB5 40
#define LB4 41
#define LB3 42
#define LB2 43
#define LB1 44
/* 45 = left encoder */
#define RB1 46
#define RB2 47
#define RB3 48
#define RB4 49
#define RB5 50
#define RB6 51

/* Thumbs */
/* 52 = optional left scroll wheel button press (not used) */
/* 58 = right trackpoint (sits top-center; excluded from THUMBS) */
#define LTH4 53
#define LTH3 54
#define LTH2 55
#define LTH1 56
#define LTH0 57
/* Trackpoint directional inputs (right thumb row) */
#define RTH0 59
#define RTH1 60
#define RTH2 61
#define RTH3 62
#define RTH4 63

#define KEYS_L LT1 LT2 LT3 LT4 LT5 LT6  LM1 LM2 LM3 LM4 LM5 LM6  LH1 LH2 LH3 LH4 LH5 LH6  LB1 LB2 LB3 LB4 LB5 LB6
#define KEYS_R RT1 RT2 RT3 RT4 RT5 RT6  RM1 RM2 RM3 RM4 RM5 RM6  RH1 RH2 RH3 RH4 RH5 RH6  RB1 RB2 RB3 RB4 RB5 RB6
#define THUMBS LTH4 LTH3 LTH2 LTH1 LTH0  RTH0 RTH1 RTH2 RTH3 RTH4
