/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

/* Corne Choc Pro 42-key layout - based on actual matrix transform
 *
 * ╭────────────────────────┬────────────────────────╮
 * │  0   1   2   3   4   5 │  7   8   9  10  11  12 │  (Row 0)
 * │ 14  15  16  17  18  19 │ 21  22  23  24  25  26 │  (Row 1)
 * │ 28  29  30  31  32  33 │ 35  36  37  38  39  40 │  (Row 2)
 * ╰───────────┮ 44  45  46 │ 48  49  50 ╭───────────╯  (Row 3 - thumbs)
 *             ╰────────────┴────────────╯
 */

/* Row 0 - Top */
#define LT5  0
#define LT4  1
#define LT3  2
#define LT2  3
#define LT1  4
#define LT0  5
#define RT0  7
#define RT1  8
#define RT2  9
#define RT3 10
#define RT4 11
#define RT5 12

/* Row 1 - Middle */
#define LM5 14
#define LM4 15
#define LM3 16
#define LM2 17
#define LM1 18
#define LM0 19
#define RM0 21
#define RM1 22
#define RM2 23
#define RM3 24
#define RM4 25
#define RM5 26

/* Row 2 - Bottom */
#define LB5 28
#define LB4 29
#define LB3 30
#define LB2 31
#define LB1 32
#define LB0 33
#define RB0 35
#define RB1 36
#define RB2 37
#define RB3 38
#define RB4 39
#define RB5 40

/* Row 3 - Thumbs */
#define LH2 45
#define LH1 46
#define LH0 47
#define RH0 50
#define RH1 51
#define RH2 52

#define KEYS_L LT0 LT1 LT2 LT3 LT4 LM0 LM1 LM2 LM3 LM4 LB0 LB1 LB2 LB3 LB4  // Left-hand keys.
#define KEYS_R RT0 RT1 RT2 RT3 RT4 RM0 RM1 RM2 RM3 RM4 RB0 RB1 RB2 RB3 RB4  // Right-hand keys.
#define THUMBS LH2 LH1 LH0 RH0 RH1 RH2
