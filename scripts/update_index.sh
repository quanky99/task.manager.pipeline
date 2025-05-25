#!/bin/bash
todo_output=$(grep "ToDo Tasks:" $1 -A 10 | grep -v "Done Tasks")
done_output=$(grep "Done Tasks:" $1 -A 10)
test_output=$(cat $2)

function update_pre() {
  id=$1
  content=$2
  html=$3
  perl -0777 -i -pe "s|(<pre id=\"$id\">)(.*?)(</pre>)|\1\n$content\n\3|s" $html
}

update_pre "todo-tasks" "$todo_output" index.html
update_pre "done-tasks" "$done_output" index.html
update_pre "test-results" "$test_output" index.html

git config user.email "ci@github.com"
git config user.name "github-actions"
git add index.html
git commit -m "Update index.html with latest task and test results"
git push