#!/bin/bash

_build() {
    local TARGET=$1
    [ -z "$TARGET" ] && { echo "No target specified. Returning."; return 1; }
    echo "Building the project for target: $TARGET"
    west build \
    -p \
    -s /workspaces/zmk/app \
    -b $TARGET \
    --snippet studio-rpc-usb-uart \
    -d /workspaces/zmk/build/$TARGET \
    -- -DZMK_CONFIG=/workspaces/zmk-config/config \
       -DZMK_EXTRA_MODULES=/workspaces/zmk-config \
       -DCONFIG_ZMK_STUDIO=y \
       -DCONFIG_ZMK_STUDIO_LOCKING=n
}
case "$1" in
    "corne_left"|"corne_choc_pro_left")
        _build "corne_choc_pro_left"
        ;;
    "corne_right"|"corne_choc_pro_right")
        _build "corne_choc_pro_right"
        ;;
    "corne"|"corne_choc_pro")
        _build "corne_choc_pro_left"
        _build "corne_choc_pro_right"
        ;;
    "xk42_left"|"left")
        _build "xk42_left"
        ;;
    "xk42_right"|"right")
        _build "xk42_right"
        ;;
    "xk42")
        _build "xk42_left"
        _build "xk42_right"
        ;;
    *)
        echo "Unknown target: $1"
        echo "Usage: $0 [xk42_left|xk42_right|xk42]"
        exit 1
        ;;
esac