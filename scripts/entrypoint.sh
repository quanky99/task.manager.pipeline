#!/bin/bash
python3 app/todo.py | tee output.txt
python3 app/todo-test.py | tee test_output.txt
bash scripts/update_index.sh output.txt test_output.txt