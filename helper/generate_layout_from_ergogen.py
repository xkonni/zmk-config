#!/usr/bin/env python3
"""
Enhanced ZMK layout generator from Ergogen output
Creates both .dtsi and .json formats for split keyboard layouts
"""

import json
import sys
from pathlib import Path


def generate_layout(
    ergogen_output_path,
    output_dtsi_path=None,
    output_json_path=None,
    key_width=100,
    key_height=100,
    gap_mm=25,  # Reduced gap from 50mm to 25mm
    json_key_width=1,
    json_key_height=1,
    rotate_180=False,  # New parameter for 180-degree rotation
):
    """
    Generate a split keyboard layout from ergogen points.yaml

    Args:
        ergogen_output_path: Path to ergogen debug/points.yaml
        output_dtsi_path: Optional path to write generated .dtsi file
        output_json_path: Optional path to write keymap-drawer .json file
        key_width: Key width in DTS units (default 100)
        key_height: Key height in DTS units (default 100)
        gap_mm: Gap between left and right halves in mm (default 50)
        json_key_width: Key width for JSON format (default 1)
        json_key_height: Key height for JSON format (default 1)

    Returns:
        List of tuples: (width, height, x, y, rotation, rx, ry)
    """

    with open(ergogen_output_path, "r") as f:
        points = json.loads(f.read())

    # Filter matrix and thumb keys
    matrix_keys = {
        k: v for k, v in points.items() if k.startswith(("matrix_", "thumbfan_"))
    }

    if not matrix_keys:
        raise ValueError(f"No matrix or thumbfan keys found in {ergogen_output_path}")

    # Sort keys to match ZMK keymap order: row by row, left to right
    def sort_key(item):
        name = item[0]
        if "matrix_" in name:
            # Extract column and row from matrix_c#_r#
            parts = name.replace("matrix_", "").split("_")
            col = int(parts[0][1:])  # Remove 'c' prefix
            row = int(parts[1][1:])  # Remove 'r' prefix
            # Order: left side first (cols 1-6), then right side (cols 7-12), by row
            if col <= 6:
                return (0, row, col)  # Left side
            else:
                return (0, row, col)  # Right side
        elif "thumbfan_" in name:
            # Extract column from thumbfan_c#_r#
            parts = name.replace("thumbfan_", "").split("_")
            col = int(parts[0][1:])  # Remove 'c' prefix
            return (1, 0, col)  # Thumb keys after matrix
        return (2, 0, 0)  # Other keys last

    # Sort keys by original matrix position (this was working for key assignments)
    def sort_key(item):
        name = item[0]
        if "matrix_" in name:
            # Extract column and row from matrix_c#_r#
            parts = name.replace("matrix_", "").split("_")
            col = int(parts[0][1:])  # Remove 'c' prefix
            row = int(parts[1][1:])  # Remove 'r' prefix
            return (0, row, col)  # Matrix keys first
        elif "thumbfan_" in name:
            # Extract column from thumbfan_c#_r#
            parts = name.replace("thumbfan_", "").split("_")
            col = int(parts[0][1:])  # Remove 'c' prefix
            return (1, 0, col)  # Thumb keys after matrix
        return (2, 0, 0)  # Other keys last

    sorted_keys = sorted(matrix_keys.items(), key=sort_key)

    # Get coordinate bounds
    xs = [v["x"] for v in matrix_keys.values()]
    ys = [v["y"] for v in matrix_keys.values()]
    min_x, max_x = min(xs), max(xs)
    min_y = min(ys)

    # Scale factor for DTS coordinates: Piantor uses 100 units per ~19mm key
    # Ergonen coordinates are in mm, so multiply by (100 / 19.05) ≈ 5.25
    dts_scale = key_width / 19.05

    # Scale factor for JSON coordinates: much smaller values for tighter layout
    json_scale = json_key_width / 19.05  # Further reduced for tighter spacing

    # Convert gap from mm to DTS units
    gap = int(gap_mm * dts_scale)

    # Build left side coordinates (DTS format)
    coords_left_dts = []
    coords_left_json = []
    matrix_index = 0

    for key_name, key_data in sorted_keys:
        # Extract matrix position for QMK format
        if "matrix_" in key_name:
            # Extract column and row from matrix_c#_r#
            parts = key_name.replace("matrix_", "").split("_")
            col = int(parts[0][1:]) - 1  # Convert to 0-based
            row = int(parts[1][1:]) - 1  # Convert to 0-based
        elif "thumbfan_" in key_name:
            # Thumb keys go in row 3
            parts = key_name.replace("thumbfan_", "").split("_")
            col = int(parts[0][1:]) - 1  # Convert to 0-based
            row = 3  # Thumb row
        else:
            col = matrix_index % 6
            row = matrix_index // 6

        # DTS coordinates
        x_dts = int((key_data["x"] - min_x) * dts_scale)
        y_dts = int((key_data["y"] - min_y) * dts_scale)
        r_dts = int(key_data.get("r", 0) * 100) if key_data.get("r", 0) != 0 else 0
        rx_dts = int((key_data["x"] - min_x) * dts_scale) if r_dts != 0 else 0
        ry_dts = int((key_data["y"] - min_y) * dts_scale) if r_dts != 0 else 0
        coords_left_dts.append(
            (key_width, key_height, x_dts, y_dts, r_dts, rx_dts, ry_dts)
        )

        # JSON coordinates (smaller scale, inverted Y for keymap-drawer)
        x_json = (key_data["x"] - min_x) * json_scale
        y_json = (max(ys) - key_data["y"]) * json_scale  # Invert Y axis
        r_json = -key_data.get("r", 0)  # Negate rotation for correct display
        key_entry = {
            "row": 0,  # All keys in row 0 for piantor compatibility
            "col": matrix_index,
            "x": round(x_json, 2),
            "y": round(y_json, 2),
        }

        if r_json != 0:
            key_entry["r"] = round(r_json, 1)
            key_entry["rx"] = round(x_json, 2)
            key_entry["ry"] = round(y_json, 2)

        coords_left_json.append(key_entry)
        matrix_index += 1

    # Calculate board width for mirroring
    board_width_dts = int((max_x - min_x) * dts_scale) + key_width
    board_width_json = (max_x - min_x) * json_scale + json_key_width

    # Build complete layout for DTS: left + gap + right (mirrored)
    coords_all_dts = list(coords_left_dts)

    # Generate right side coordinates (mirrored but same key order)
    coords_right_json = []
    for i, ((w, h, x, y, r, rx, ry), json_coord) in enumerate(
        zip(coords_left_dts, coords_left_json)
    ):
        # DTS mirrored coordinates
        x_r = board_width_dts + gap + (board_width_dts - x - key_width)
        rx_r = (
            board_width_dts + gap + (board_width_dts - rx - key_width) if r != 0 else 0
        )
        coords_all_dts.append((w, h, x_r, y, -r, rx_r, ry))

        # JSON mirrored coordinates
        x_r_json = (
            board_width_json
            + (gap_mm * json_scale)
            + (board_width_json - json_coord["x"] - json_key_width)
        )

        key_entry_r = {
            "row": 0,  # All keys in row 0 for piantor compatibility
            "col": len(coords_left_json)
            + i,  # Sequential numbering for reversed right side
            "x": round(x_r_json, 2),
            "y": json_coord["y"],
        }

        if "r" in json_coord and json_coord["r"] != 0:
            key_entry_r["r"] = -json_coord["r"]  # Negate again for mirror
            key_entry_r["rx"] = round(x_r_json, 2)
            key_entry_r["ry"] = json_coord["y"]

        coords_right_json.append(key_entry_r)

    # Build JSON layout with proper keymap-drawer ordering:
    # Interleave left and right sides by physical row for correct key position mapping
    coords_all_json = []

    # Group keys by original matrix row (not JSON row which is always 0)
    left_by_matrix_row = {}
    right_by_matrix_row = {}

    # Parse original matrix positions from left side coordinates
    for i, key in enumerate(coords_left_json):
        # Extract original row from the sort order
        if i < 18:  # 6 cols * 3 rows = 18 matrix keys
            matrix_row = i // 6  # Row based on position
        else:  # thumb keys
            matrix_row = 3

        if matrix_row not in left_by_matrix_row:
            left_by_matrix_row[matrix_row] = []
        left_by_matrix_row[matrix_row].append(key)

    for i, key in enumerate(coords_right_json):
        # Extract original row from the sort order
        if i < 18:  # 6 cols * 3 rows = 18 matrix keys
            matrix_row = i // 6  # Row based on position
        else:  # thumb keys
            matrix_row = 3

        if matrix_row not in right_by_matrix_row:
            right_by_matrix_row[matrix_row] = []
        right_by_matrix_row[matrix_row].append(key)

    # Sort keys within each row by original column position
    for matrix_row in left_by_matrix_row:
        left_by_matrix_row[matrix_row].sort(key=lambda k: k["col"])
    for matrix_row in right_by_matrix_row:
        # For right side, reverse the key order within each row for proper mirroring
        right_by_matrix_row[matrix_row].sort(key=lambda k: k["col"])
        right_by_matrix_row[matrix_row].reverse()

    # Add keys row by row: left row, then right row (piantor style)
    position = 0
    for matrix_row in sorted(left_by_matrix_row.keys()):
        # Add left side of this row
        for key in left_by_matrix_row[matrix_row]:
            key_copy = key.copy()
            key_copy["col"] = position
            coords_all_json.append(key_copy)
            position += 1

        # Add right side of this row if it exists
        if matrix_row in right_by_matrix_row:
            for key in right_by_matrix_row[matrix_row]:
                key_copy_r = key.copy()  # Create new copy for right side key
                key_copy_r["col"] = position
                coords_all_json.append(key_copy_r)
                position += 1

    # Apply 180-degree rotation if requested (DTS only, JSON is fine)
    if rotate_180:
        # Find bounds for rotation
        xs_dts = [c[2] for c in coords_all_dts]
        ys_dts = [c[3] for c in coords_all_dts]
        max_x_dts = max(xs_dts)
        max_y_dts = max(ys_dts)

        # Rotate DTS coordinates: flip both X and Y
        coords_all_dts = [
            (
                w,
                h,
                max_x_dts - x,
                max_y_dts - y,
                r,
                max_x_dts - rx if rx != 0 else 0,
                max_y_dts - ry if ry != 0 else 0,
            )
            for w, h, x, y, r, rx, ry in coords_all_dts
        ]

    # Write output files
    if output_dtsi_path:
        write_dtsi(coords_all_dts, output_dtsi_path)

    if output_json_path:
        write_json(coords_all_json, output_json_path)

    return coords_all_dts, coords_all_json


def write_dtsi(coords, output_path):
    """Write coordinates to a ZMK .dtsi file"""

    dtsi_content = """/*
* Copyright (c) 2020 The ZMK Contributors
*
* SPDX-License-Identifier: MIT
*/

#include <physical_layouts.dtsi>

/ {
    default_layout: keymap_layout_0 {
        compatible = "zmk,physical-layout";
        display-name = "Default";
        transform = <&default_transform>;
        kscan = <&kscan0>;

        keys =
"""

    for i, (w, h, x, y, r, rx, ry) in enumerate(coords):
        # Format values with parentheses for negative numbers (DTS requirement)
        r_str = f"({r})" if r < 0 else f"{r:6d}"
        rx_str = f"({rx})" if rx < 0 else f"{rx:5d}"
        ry_str = f"({ry})" if ry < 0 else f"{ry:5d}"

        if i == 0:
            # First entry uses = <...>
            line = f"            <&key_physical_attrs {w:4d} {h:4d} {x:5d} {y:5d} {r_str} {rx_str} {ry_str}>"
        else:
            # Subsequent entries use , <...>
            line = f"            , <&key_physical_attrs {w:4d} {h:4d} {x:5d} {y:5d} {r_str} {rx_str} {ry_str}>"

        if i == len(coords) - 1:
            line += ";"

        dtsi_content += line + "\n"

    dtsi_content += """    };
};
"""

    Path(output_path).write_text(dtsi_content)
    print(f"Generated {output_path}")
    print(f"Total keys: {len(coords)}")


def write_json(coords, output_path):
    """Write coordinates to a keymap-drawer JSON file in piantor format"""

    json_data = {
        "id": "xk42",
        "name": "XK42",
        "layouts": {"default_layout": {"name": "default_layout", "layout": coords}},
    }

    Path(output_path).write_text(json.dumps(json_data, indent=2))
    print(f"Generated {output_path}")
    print(f"JSON layout keys: {len(coords)}")


if __name__ == "__main__":
    # Default paths
    base_path = Path(__file__).parent
    ergogen_path = base_path / "ergogen-2026-02-19" / "debug" / "points.yaml"
    output_dtsi_path = base_path / "boards" / "arm" / "xk42" / "xk42-layouts.dtsi"
    output_json_path = base_path / "config" / "xk42.json"

    if len(sys.argv) > 1:
        ergogen_path = Path(sys.argv[1])

    if len(sys.argv) > 2:
        output_dtsi_path = Path(sys.argv[2])

    if len(sys.argv) > 3:
        output_json_path = Path(sys.argv[3])

    if not ergogen_path.exists():
        print(f"Error: {ergogen_path} not found")
        sys.exit(1)

    try:
        coords_dts, coords_json = generate_layout(
            str(ergogen_path),
            str(output_dtsi_path),
            str(output_json_path),
            rotate_180=True,
        )

        print(f"\nDTS Layout dimensions:")
        xs = [c[2] for c in coords_dts]
        ys = [c[3] for c in coords_dts]
        print(f"  X range: {min(xs)} - {max(xs)} units")
        print(f"  Y range: {min(ys)} - {max(ys)} units")

        print(f"\nJSON Layout dimensions:")
        xs_json = [c["x"] for c in coords_json]
        ys_json = [c["y"] for c in coords_json]
        print(f"  X range: {min(xs_json):.2f} - {max(xs_json):.2f}")
        print(f"  Y range: {min(ys_json):.2f} - {max(ys_json):.2f}")
        print(f"  Matrix positions: {len(coords_json)} keys total")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
