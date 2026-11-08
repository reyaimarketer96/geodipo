#!/bin/bash
echo "=== Starting Geodipo RAG Server Worker ==="
nohup python3 server_worker.py > worker.log 2>&1 &
echo "Process started in background!"
echo "You can now safely disconnect or shut down your laptop."
echo "To view live logs: bash monitor.sh"
echo "To check progress percentage: bash status.sh"
