#!/bin/bash

BUILD_DIR="/workspaces/zmk-config/build"

_build() {
    local BOARD=$1
    local SHIELD=$2
    local BUILD_NAME=$3
    [ -z "$BOARD" ] && { echo "No board specified. Returning."; return 1; }
    echo "Building the project for board: $BOARD, shield: $SHIELD"
    west build \
    -p \
    -s /workspaces/zmk/app \
    -b $BOARD \
    --snippet studio-rpc-usb-uart \
    -d $BUILD_DIR/$BUILD_NAME \
    -- -DZMK_CONFIG=/workspaces/zmk-config/config \
       -DZMK_EXTRA_MODULES=/workspaces/zmk-config \
       -DSHIELD="$SHIELD" \
       -DCONFIG_ZMK_STUDIO=y \
       -DCONFIG_ZMK_STUDIO_LOCKING=n

    if [ $? -eq 0 ]; then
        mkdir -p $BUILD_DIR
        cp $BUILD_DIR/$BUILD_NAME/zephyr/zmk.uf2 $BUILD_DIR/$BUILD_NAME.uf2
        echo "Copied firmware to $BUILD_DIR/$BUILD_NAME.uf2"
    fi
}
case "$1" in
    "corne_left"|"corne_choc_pro_left")
        _build "corne_choc_pro_left" "" "corne_left"
        ;;
    "corne_right"|"corne_choc_pro_right")
        _build "corne_choc_pro_right" "" "corne_right"
        ;;
    "corne"|"corne_choc_pro")
        _build "corne_choc_pro_left" "" "corne_left"
        _build "corne_choc_pro_right" "" "corne_right"
        ;;
    "xk42_left"|"left")
        _build "nice_nano_v2" "xk42_left nice_view" "xk42_left"
        ;;
    "xk42_right"|"right")
        _build "nice_nano_v2" "xk42_right nice_view" "xk42_right"
        ;;
    "xk42")
        _build "nice_nano_v2" "xk42_left nice_view" "xk42_left"
        _build "nice_nano_v2" "xk42_right nice_view" "xk42_right"
        ;;
    *)
        echo "Unknown target: $1"
        echo "Usage: $0 [xk42_left|xk42_right|xk42|corne_left|corne_right|corne]"
        exit 1
        ;;
esac