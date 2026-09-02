/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

/* totem 38-key layout
 * Rows 0-1: 5 keys per side (no outer column)
 * Row 2: 6 keys per side (outer column present)
 * Row 3: 3 thumb keys per side
 *
 * ╭──────────────────────┬──────────────────────╮
 * │  0   1   2   3   4   │  5   6   7   8   9   │  (Row 0 - top)
 * │ 10  11  12  13  14   │ 15  16  17  18  19   │  (Row 1 - middle)
 * │ 20  21  22  23  24  25 │ 26  27  28  29  30  31 │  (Row 2 - bottom)
 * ╰──────────╮  32  33  34 │ 35  36  37 ╭─────────╯  (Row 3 - thumbs)
 *            ╰─────────────┴────────────╯
 */

/* Row 0 - Top */
#define LT4  0
#define LT3  1
#define LT2  2
#define LT1  3
#define LT0  4
#define RT0  5
#define RT1  6
#define RT2  7
#define RT3  8
#define RT4  9

/* Row 1 - Middle */
#define LM4 10
#define LM3 11
#define LM2 12
#define LM1 13
#define LM0 14
#define RM0 15
#define RM1 16
#define RM2 17
#define RM3 18
#define RM4 19

/* Row 2 - Bottom */
#define LB5 20
#define LB4 21
#define LB3 22
#define LB2 23
#define LB1 24
#define LB0 25
#define RB0 26
#define RB1 27
#define RB2 28
#define RB3 29
#define RB4 30
#define RB5 31

/* Row 3 - Thumbs */
#define LH2 32
#define LH1 33
#define LH0 34
#define RH0 35
#define RH1 36
#define RH2 37

#define KEYS_L LT0 LT1 LT2 LT3 LT4 LM0 LM1 LM2 LM3 LM4 LB0 LB1 LB2 LB3 LB4  // Left-hand keys.
#define KEYS_R RT0 RT1 RT2 RT3 RT4 RM0 RM1 RM2 RM3 RM4 RB0 RB1 RB2 RB3 RB4  // Right-hand keys.
#define THUMBS LH2 LH1 LH0 RH0 RH1 RH2
