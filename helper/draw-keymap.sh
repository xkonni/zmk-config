#!/bin/bash

# Generate keymap YAML and SVG using custom configuration
# Usage: ./keymap.sh [output_filename]

OUTPUT_FILE=${1:-"xk42_layout.svg"}

echo "Parsing keymap from ZMK config..."
keymap parse -z config/xk42.keymap -c 10 > xk42.yaml

echo "Generating keymap SVG: $OUTPUT_FILE"
keymap -c keymap_drawer.config.yaml draw xk42.yaml -j config/xk42.json -o "$OUTPUT_FILE"


if [ $? -eq 0 ]; then
    # rm  -v xk42.yaml
    echo "Successfully generated: $OUTPUT_FILE"
else
    echo "Error generating keymap"
    exit 1
fi

