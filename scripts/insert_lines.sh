#!/bin/bash

# Function to prompt user for input with auto-completion
prompt_for_input() {
    local prompt=$1
    local input_variable_name=$2
    read -e -p "$prompt: " input_value
    # shellcheck disable=SC2140
    eval "$input_variable_name"="'$input_value'"
}

# Initialize variables
src_file=""
start_line=""
end_line=""
dest_file=""
insert_line=""

# Prompt for file names and line ranges
prompt_for_input "Enter the source file name/path" src_file
prompt_for_input "Enter the start line in the source file" start_line
prompt_for_input "Enter the end line in the source file" end_line
prompt_for_input "Enter the destination file name/path" dest_file
prompt_for_input "Enter the line number in the destination file where the content should be inserted" insert_line

# Create a temporary file to hold the extracted lines
temp_file=$(mktemp)

# Extract the specified line range from the source file
sed -n "${start_line},${end_line}p" "$src_file" > "$temp_file"

# Split the destination file into two parts: before and after the insert line
head -n $((insert_line - 1)) "$dest_file" > "${dest_file}.before"
tail -n +$insert_line "$dest_file" > "${dest_file}.after"

# Concatenate the parts with the extracted lines in between
cat "${dest_file}.before" "$temp_file" "${dest_file}.after" > "${dest_file}.new"

# Replace the original destination file with the new one
mv "${dest_file}.new" "$dest_file"

# Clean up temporary files
rm -f "$temp_file" "${dest_file}.before" "${dest_file}.after"

echo "Content inserted successfully."
