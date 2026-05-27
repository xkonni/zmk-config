/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

/* Corne Choc Pro — actual matrix positions
 *
 * Rows 0 & 1: 6 keys per side + 2 center positions (encoder buttons).
 * Row 2:      6 keys per side, no center positions.
 *
 * ╭─────────────────────────┬─────┬─────────────────────────╮
 * │  0   1   2   3   4   5  | 6 7 │  8   9  10  11  12  13  │  (Row 0)
 * │ 14  15  16  17  18  19  |20 21│ 22  23  24  25  26  27  │  (Row 1)
 * │ 28  29  30  31  32  33  │     │ 34  35  36  37  38  39  │  (Row 2)
 * ╰───────────╮ 40  41  42  │     │ 43  44  45 ╭────────────╯  (Thumbs)
 *             ╰─────────────┴─────┴────────────╯
 */

/* Row 0 - Top */
#define LT5  0
#define LT4  1
#define LT3  2
#define LT2  3
#define LT1  4
#define LT0  5
/* 6, 7 = center (encoder buttons) */
#define RT0  8
#define RT1  9
#define RT2 10
#define RT3 11
#define RT4 12
#define RT5 13

/* Row 1 - Home row */
#define LM5 14
#define LM4 15
#define LM3 16
#define LM2 17
#define LM1 18
#define LM0 19
/* 20, 21 = center (encoder buttons) */
#define RM0 22
#define RM1 23
#define RM2 24
#define RM3 25
#define RM4 26
#define RM5 27

/* Row 2 - Bottom */
#define LB5 28
#define LB4 29
#define LB3 30
#define LB2 31
#define LB1 32
#define LB0 33
#define RB0 34
#define RB1 35
#define RB2 36
#define RB3 37
#define RB4 38
#define RB5 39

/* Thumbs */
#define LH2 40
#define LH1 41
#define LH0 42
#define RH0 43
#define RH1 44
#define RH2 45

#define KEYS_L LT5 LT4 LT3 LT2 LT1 LT0 LM5 LM4 LM3 LM2 LM1 LM0 LB5 LB4 LB3 LB2 LB1 LB0  // Left-hand keys.
#define KEYS_R RT5 RT4 RT3 RT2 RT1 RT0 RM5 RM4 RM3 RM2 RM1 RM0 RB5 RB4 RB3 RB2 RB1 RB0  // Right-hand keys.
#define THUMBS LH2 LH1 LH0 RH0 RH1 RH2
