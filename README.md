# ZMK Config

Personal ZMK firmware configuration for four split keyboards, based on ZMK v0.3.
Each keyboard is available in a standard BLE variant and a dongle variant (USB dongle
as central, wireless peripherals). Dongle keymaps reference the regular keymap at
build-time and are therefore always identical.

## Keyboards

| Keyboard | Keys | Regular | Dongle |
|---|---|---|---|
| **xk42** | 42-key split | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_xk42.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_xk42.yml) | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_xk42_dongle.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_xk42_dongle.yml) |
| **Piantor Pro BT** | 42-key split | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_piantor.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_piantor.yml) | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_piantor_dongle.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_piantor_dongle.yml) |
| **Corne Choc Pro BT** | 46-key split | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_corne.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_corne.yml) | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_corne_dongle.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_corne_dongle.yml) |
| **Eyelash Sofle** | 58-key split | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_eyelash_sofle.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_eyelash_sofle.yml) | |

## ZMK modules

- [nice-view-glyphs](https://github.com/xkonni/nice-view-glyphs) — custom glyphs for nice!view
- [nice-view-battery](https://github.com/infely/nice-view-battery) — battery widget for nice!view
- [zmk-dongle-display](https://github.com/englmaxi/zmk-dongle-display) — dongle display support

## xk42

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-xk42/xk42.png" alt="xk42 Keymap" />

</details>

## Piantor Pro BT

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-piantor/piantor_pro_bt.png" alt="Piantor Keymap" />

</details>

## Corne Choc Pro BT

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-corne/corne_choc_pro.png" alt="Corne Keymap" />

</details>

## Eyelash Sofle

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-eyelash_sofle/eyelash_sofle.png" alt="Eyelash Sofle Keymap" />

</details>
