#!/bin/bash

# Function to prompt user for input with auto-completion
prompt_for_input() {
    local prompt=$1
    local input_variable_name=$2
    read -e -p "$prompt: " input_value
    eval $input_variable_name="'$input_value'"
}

# Store the current working directory
current_dir=$(pwd)

# Prompt for file names and line ranges
prompt_for_input "Enter the first file name" file1
prompt_for_input "Enter the START_LINE for the first file" start_line1
prompt_for_input "Enter the END_LINE for the first file" end_line1
prompt_for_input "Enter the second file name" file2
prompt_for_input "Enter the START_LINE for the second file" start_line2
prompt_for_input "Enter the END_LINE for the second file" end_line2

# Create temporary files
temp_file1=$(mktemp)
temp_file2=$(mktemp)

# Extract the specified line ranges
sed -n "${start_line1},${end_line1}p" "$file1" > "$temp_file1"
sed -n "${start_line2},${end_line2}p" "$file2" > "$temp_file2"

# Run vimdiff on the temporary files
vimdiff "$temp_file1" "$temp_file2"

# Clean up temporary files
rm -f "$temp_file1" "$temp_file2"

echo "Comparison complete and temporary files cleaned up."
