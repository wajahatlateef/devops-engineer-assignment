#!/bin/bash

LOG_FILE="health.log"

# 🔹 Function: Get timestamp
get_timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

# 🔹 Function: Log message
log_message() {
  local message=$1
  echo "$(get_timestamp) - $message" >> $LOG_FILE
}

# 🔹 Function: Check website status
check_website() {
  local url=$1

  status_code=$(curl -o /dev/null -s -w "%{http_code}" "$url")

  if [ "$status_code" -eq 200 ]; then
    log_message "$url is UP (Status: $status_code)"
  else
    log_message "$url is DOWN (Status: $status_code)"
  fi
}

# 🔹 Main function
main() {
  URL="https://example.com"
  check_website "$URL"
}

# 🔹 Execute
main