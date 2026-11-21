# ZMK Config

Personal ZMK firmware configuration for five split keyboards, based on ZMK v0.3.
Each keyboard is available in a standard BLE variant and a dongle variant (USB dongle
as central, wireless peripherals). Dongle keymaps reference the regular keymap at
build-time and are therefore always identical. Regular builds run on pushes to `main`,
`v0.3`, `dev`, and `dev-v0.3`; releases are published from `main`. Dongle builds are
manual.

## Keyboards

| Keyboard | Keys | Build | Build & release | Last release workflow run | Dongle build (manual) |
|---|---|---|---|---|---|
| **Piantor Pro BT** | 42-key split | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_piantor.yml) | [Build & release](https://github.com/xkonni/zmk-config/actions/workflows/build_release_piantor.yml) | <!-- RELEASE-DATE:piantor -->—<!-- /RELEASE-DATE:piantor --> | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_piantor_dongle.yml) |
| **Totemist** | 36-key split | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_totemist.yml) | [Build & release](https://github.com/xkonni/zmk-config/actions/workflows/build_release_totemist.yml) | <!-- RELEASE-DATE:totemist -->—<!-- /RELEASE-DATE:totemist --> | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_totemist_dongle.yml) |
| **xk42** | 42-key split | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_xk42.yml) | [Build & release](https://github.com/xkonni/zmk-config/actions/workflows/build_release_xk42.yml) | <!-- RELEASE-DATE:xk42 -->—<!-- /RELEASE-DATE:xk42 --> | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_xk42_dongle.yml) |
| **Corne Choc Pro BT** | 46-key split | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_corne.yml) | [Build & release](https://github.com/xkonni/zmk-config/actions/workflows/build_release_corne.yml) | <!-- RELEASE-DATE:corne -->—<!-- /RELEASE-DATE:corne --> | [Build](https://github.com/xkonni/zmk-config/actions/workflows/build_corne_dongle.yml) |
| **Eyelash Sofle** | 58-key split | [![](https://github.com/xkonni/zmk-config/actions/workflows/build_release_eyelash_sofle.yml/badge.svg)](https://github.com/xkonni/zmk-config/actions/workflows/build_release_eyelash_sofle.yml) | |

## ZMK modules

- [nice-view-glyphs](https://github.com/xkonni/nice-view-glyphs) — custom glyphs for nice!view
- [nice-view-battery](https://github.com/infely/nice-view-battery) — battery widget for nice!view
- [zmk-dongle-display](https://github.com/englmaxi/zmk-dongle-display) — dongle display support
- [zmk-keyboards-totem](https://github.com/victorlucachi/zmk-keyboards-totem) — Totem shield definitions

## Piantor Pro BT

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-piantor/piantor_pro_bt.png" alt="Piantor Keymap" />

</details>

## Totemist

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-totemist/totem.png" alt="Totemist Keymap" />

</details>

## xk42

<details>
<summary>View Keymap</summary>

<img src="https://github.com/xkonni/zmk-config/releases/download/latest-xk42/xk42.png" alt="xk42 Keymap" />

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
